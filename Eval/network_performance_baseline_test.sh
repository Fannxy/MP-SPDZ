set -e

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")
nth=0

protocol=${programs[${nth}]}
script=${scripts[${nth}]}
parties_num=3
if [ ${nth} -eq 5 ]; then
    parties_num=4
fi

network=WAN
bandwidth=100 # in Mbps
latency=100ms # in ms
if [ "$network" == "LAN" ]; then
    bandwidth=10000 # in Mbps
    latency=0.1ms # in ms
fi
N=100

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/${network}/network_baseline_logs/
clogFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/${network}/network_baseline_logs/Compile/
clogFile=${clogFolder}network_baseline_compile_log
logFile=${logFolder}network_baseline_execution_log

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

target_networks=("adult" "breast_cancer")

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

for network_type in "${target_networks[@]}"; do
    echo "Testing ${network_type} ..."
    if [ ${network_type} == "adult" ]; then
        sourceFiles=(easy_adult)
    elif [ ${network_type} == "breast_cancer" ]; then
        sourceFiles=(breast_logistic breast_tree)
    fi
    for sourceFile in "${sourceFiles[@]}"; do
        if [ ${nth} == 0 ] || [ ${nth} == 1 ] || [ ${nth} == 5 ]; then
            python compile.py -R 288 ${sourceFile} > ${clogFile}_${sourceFile} &
        else
            python compile.py -F 128 ${sourceFile} > ${clogFile}_${sourceFile} &
        fi
    done
done
wait;

for network_type in "${target_networks[@]}"; do
    echo "-------------------------------------"
    echo "Executing MPC for network: ${network_type}"
    
    if [ ${network_type} == "adult" ]; then
        sourceFiles=(easy_adult)
    elif [ ${network_type} == "breast_cancer" ]; then
        sourceFiles=(breast_logistic breast_tree)
    fi
    
    for sourceFile in "${sourceFiles[@]}"; do
        echo "Starting all players for ${sourceFile}..."
        # 先启动所有players（并行），然后再等待
        for i in $(seq 1 ${parties_num}); do
            player_id=$((i-1))
            host="h${i}"
            
            if [ ${player_id} -eq 0 ]; then
                ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -b 1000 -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile} -v" >> ${logFile}_${sourceFile}.log 2>&1 &
            else
                ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -b 1000 -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile} -v" &
            fi
        done
        
        echo "All players for ${sourceFile} started. Waiting for computation to complete..."
        wait
        echo "Execution for ${sourceFile} completed."
    done
    
    echo "Execution for ${network_type} completed."
done

echo "-------------------------------------"
echo "All tests finished."