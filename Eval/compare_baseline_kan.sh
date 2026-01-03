#!/bin/bash
set -e

# 主脚本：比较baseline和KAN的估计时间
# 用法: ./compare_baseline_kan.sh [protocol_idx] [network] [N] [skip_measurement]

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")

# 参数设置
nth=5
network=LAN
N=100  # 默认100个输入
skip_measurement="true"  # 是否跳过操作时间测量

protocol=${programs[${nth}]}
script=${scripts[${nth}]}
parties_num=3
if [ ${nth} -eq 5 ]; then
    parties_num=4
fi

bandwidth=100 # in Mbps
latency=100ms # in ms
if [ "$network" == "LAN" ]; then
    bandwidth=10000 # in Mbps
    latency=0.5ms # in ms
fi

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/${network}/comparison_logs/
clogFolder=${logFolder}Compile/
clogFile=${clogFolder}comparison_compile_log-${N}
logFile=${logFolder}comparison_execution_log-${N}
sourceFile=compare_baseline_kan

operation_timings_file=/root/llm-project/NFGen+KAN/Results/${protocol}/${network}/operation_timings.json

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

target_funcs=("func1" "func2" "func3" "func4" "func5" "func6" "func7" "func8" "func9" "func10" "func11" "func12" "func13" "func14" "func15")

echo "======================================"
echo "Baseline vs KAN 时间比较"
echo "======================================"
echo "协议: ${protocol}"
echo "网络: ${network}"
echo "函数列表: ${target_funcs[@]}"
echo "输入数量: ${N}"
echo "======================================"

# 步骤1: 测量操作时间（如果需要）
if [ "$skip_measurement" != "true" ] && [ ! -f "${operation_timings_file}" ]; then
    echo "步骤1: 测量操作时间..."
    cd ${MP_SPDZ_DIR}
    bash ./Eval/measure_operation_timings.sh ${nth} ${network} 100
    
    echo "步骤1.1: 解析操作时间..."
    python3 ${MP_SPDZ_DIR}Eval/parse_operation_timings.py ${protocol} ${network} 100 ${operation_timings_file}
    
    if [ ! -f "${operation_timings_file}" ]; then
        echo "错误: 无法生成操作时间文件"
        exit 1
    fi
    echo "操作时间已保存到: ${operation_timings_file}"
elif [ "$skip_measurement" == "true" ]; then
    echo "跳过操作时间测量（使用已有数据）"
elif [ -f "${operation_timings_file}" ]; then
    echo "使用已有的操作时间文件: ${operation_timings_file}"
fi

# 步骤2: 设置网络环境
cd ${MP_SPDZ_DIR}
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

# 循环处理每个函数
for func_name in "${target_funcs[@]}"; do
    echo ""
    echo "======================================"
    echo "处理函数: ${func_name}"
    echo "======================================"
    
    # 步骤3: 编译比较程序
    echo "步骤2: 编译比较程序..."
    cd ${MP_SPDZ_DIR}
    if [ ${nth} == 0 ]; then
        python compile.py -R 288 ${sourceFile} ${func_name} ${nth} ${network} ${N} > ${clogFile}_${func_name} 2>&1
    elif [ ${nth} == 1 ]; then
        python compile.py -R 288 ${sourceFile} ${func_name} ${nth} ${network} ${N} > ${clogFile}_${func_name} 2>&1
    elif [ ${nth} == 5 ]; then
        python compile.py -R 288 ${sourceFile} ${func_name} ${nth} ${network} ${N} > ${clogFile}_${func_name} 2>&1
    else
        python compile.py -F 128 ${sourceFile} ${func_name} ${nth} ${network} ${N} > ${clogFile}_${func_name} 2>&1
    fi

    # 步骤4: 执行比较程序
    echo "步骤3: 执行比较程序（密文计算）..."
    echo "-------------------------------------"

    for i in $(seq 1 ${parties_num}); do
        player_id=$((i-1))
        host="h${i}"
        
        echo "Starting Player ${player_id} on ${host}..."
        
        if [ ${player_id} -eq 0 ]; then
            ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile}-${func_name}-${nth}-${network}-${N} -v" >> ${logFile}_${func_name}.log 2>&1 &
        else
            ssh ${host} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${player_id} --ip-file-name ${MP_SPDZ_DIR}Hosts ${sourceFile}-${func_name}-${nth}-${network}-${N} -v" &
        fi
    done

    wait

    # 步骤5: 解析结果并输出
    echo "======================================"

    # 从日志中提取结果
    if [ -f "${logFile}_${func_name}.log" ]; then
        # 提取选择的方法
        selected_method=$(grep "选择的方法:" ${logFile}_${func_name}.log | tail -1 | awk -F': ' '{print $2}')
        selected_time=$(grep "选择的估计时间:" ${logFile}_${func_name}.log | tail -1 | awk -F': ' '{print $2}' | awk '{print $1}')
        baseline_time=$(grep "Baseline估计时间:" ${logFile}_${func_name}.log | tail -1 | awk -F': ' '{print $2}' | awk '{print $1}')
        kan_time=$(grep "KAN估计时间:" ${logFile}_${func_name}.log | tail -1 | awk -F': ' '{print $2}' | awk '{print $1}')
        
        echo "Baseline估计时间: ${baseline_time} 秒"
        echo "KAN估计时间: ${kan_time} 秒"
        echo ""
        
        if [ "$selected_method" == "1" ]; then
            echo ">>> 选择结果: Baseline (更快)"
            echo ">>> 估计时间: ${selected_time} 秒"
        elif [ "$selected_method" == "0" ]; then
            echo ">>> 选择结果: KAN (更快)"
            echo ">>> 估计时间: ${selected_time} 秒"
        else
            echo ">>> 无法确定选择结果"
        fi
        
        # 显示完整日志的最后几行
        echo ""
        echo "完整日志（最后20行）:"
        echo "-------------------------------------"
        tail -20 ${logFile}_${func_name}.log
    else
        echo "错误: 无法找到日志文件 ${logFile}_${func_name}.log"
    fi
    
    echo ""
    echo "函数 ${func_name} 处理完成"
    echo "======================================"
done

echo ""
echo "======================================"
echo "所有函数处理完成。"
echo "日志保存在: ${logFolder}"
echo "======================================"

