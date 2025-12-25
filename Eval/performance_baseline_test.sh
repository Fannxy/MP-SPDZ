set -e

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")
nth=5

protocol=${programs[${nth}]}
script=${scripts[${nth}]}
parties_num=3
if [ ${nth} -eq 5 ]; then
    parties_num=4
fi

network=LAN
bandwidth=100 # in Mbps
latency=100ms # in ms
if [ "$network" == "LAN" ]; then
    bandwidth=10000 # in Mbps
    latency=0.5ms # in ms
fi
N=100

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/${network}/baseline_logs/
clogFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/${network}/baseline_logs/Compile/
clogFile=${clogFolder}baseline_compile_log-${N}
logFile=${logFolder}baseline_execution_log-${N}
sourceFile=multivariate_baseline_performance

# --- 你的所有文件夹创建逻辑保持不变 ---
if [ ! -d /root/llm-project/NFGen+KAN/Results/ ]; then
    mkdir /root/llm-project/NFGen+KAN/Results/;
fi
if [ ! -d /root/llm-project/NFGen+KAN/Results/${protocol}/ ]; then
    mkdir /root/llm-project/NFGen+KAN/Results/${protocol}/;
fi
if [ ! -d /root/llm-project/NFGen+KAN/Results/${protocol}/${network}/ ]; then
    mkdir /root/llm-project/NFGen+KAN/Results/${protocol}/${network}/;
fi
if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
else
    rm -r ${logFolder}*
fi
if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
else
    rm -r ${clogFolder}*
fi

target_funcs=("func1" "func2" "func3" "func4" "func5" "func6" "func7" "func8" "func9" "func15")

./Eval/network_start.sh ${bandwidth} ${latency} ${logFolder} ${parties_num}

HOSTS_FILE_CONTENT=$(cat <<EOF
10.0.0.11
10.0.0.12
10.0.0.13
EOF
)
if [ ${nth} -eq 5 ]; then
    HOSTS_FILE_CONTENT=$(cat <<EOF
10.0.0.11
10.0.0.12
10.0.0.13
10.0.0.14
EOF
)
fi
echo "$HOSTS_FILE_CONTENT" > ${MP_SPDZ_DIR}Hosts
echo "Created hosts.txt for MP-SPDZ"

./Scripts/setup-ssl.sh ${parties_num}

for func in "${target_funcs[@]}"; do
    echo "Testing ${func} ..."
    if [ ${nth} == 0 ]; then
        python compile.py -R 288 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    elif [ ${nth} == 1 ]; then
        python compile.py -R 288 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    elif [ ${nth} == 5 ]; then
        python compile.py -R 288 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    else
        python compile.py -F 128 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    fi
done
wait;

for func in "${target_funcs[@]}"; do
    echo "-------------------------------------"
    echo "Executing MPC for function: ${func}"
    
    # 在这个循环里，我们将为 h1, h2, h3 分别启动一个后台进程
    for i in $(seq 1 ${parties_num}); do
        player_id=$((i-1))
        host="h${i}"
        
        echo "Starting Player ${player_id} on ${host} for ${func} in background..."
        
        if [ ${player_id} -eq 0 ]; then
            ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile}-${func}-${N}-${nth} -v" >> ${logFile}_${func}.log 2>&1 &
        else
            ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile}-${func}-${N}-${nth} -v" &
        fi
    done
    
    echo "All players for ${func} started. Waiting for computation to complete..."
    wait
    echo "Execution for ${func} completed."
done

echo "-------------------------------------"
echo "All tests finished."