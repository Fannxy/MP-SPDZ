#!/bin/bash
set -e

# 用于offline测量各种MPC操作的时间
# 这个脚本会运行operation_timing.mpc来测量各种基本操作的时间

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
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/${network}/operation_timings/
clogFolder=${logFolder}Compile/
clogFile=${clogFolder}operation_compile_log
logFile=${logFolder}operation_execution_log
sourceFile=operation_timing

# 创建必要的目录
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
    mkdir -p ${logFolder};
else
    rm -rf ${logFolder}*
fi
if [ ! -d ${clogFolder} ]; then
    mkdir -p ${clogFolder};
else
    rm -rf ${clogFolder}*
fi

# 操作类型列表
operations=("add" "sub" "mult" "div" "pow" "sqrt" "exp" "log" "sin" "cos" "compare" "if_else")

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

# 编译所有操作类型
for op in "${operations[@]}"; do
    echo "Compiling ${op} ..."
    if [ ${nth} == 0 ]; then
        python compile.py -R 288 ${sourceFile} ${op} ${N} > ${clogFile}_${op} 2>&1 &
    elif [ ${nth} == 1 ]; then
        python compile.py -R 288 ${sourceFile} ${op} ${N} > ${clogFile}_${op} 2>&1 &
    elif [ ${nth} == 5 ]; then
        python compile.py -R 288 ${sourceFile} ${op} ${N} > ${clogFile}_${op} 2>&1 &
    else
        python compile.py -F 128 ${sourceFile} ${op} ${N} > ${clogFile}_${op} 2>&1 &
    fi
done
wait

# 执行所有操作类型
for op in "${operations[@]}"; do
    echo "-------------------------------------"
    echo "Measuring timing for operation: ${op}"
    
    for i in $(seq 1 ${parties_num}); do
        player_id=$((i-1))
        host="h${i}"
        
        echo "Starting Player ${player_id} on ${host} for ${op}..."
        
        if [ ${player_id} -eq 0 ]; then
            ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile}-${op}-${N} -v" >> ${logFile}_${op}.log 2>&1 &
        else
            ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile}-${op}-${N} -v" &
        fi
    done
    
    wait
    echo "Measurement for ${op} completed."
done

echo "-------------------------------------"
echo "All operation timings measured."

