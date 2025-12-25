set -e

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")
nth=0

protocol=${programs[${nth}]}
script=${scripts[${nth}]}

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/network_baseline_logs/
clogFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/network_baseline_logs/Compile/
clogFile=${clogFolder}network_baseline_compile_log
logFile=${logFolder}network_baseline_execution_log

if [ ! -d /root/llm-project/NFGen+KAN/Results/ ]; then
    mkdir /root/llm-project/NFGen+KAN/Results/;
fi

if [ ! -d /root/llm-project/NFGen+KAN/Results/${protocol}/ ]; then
    mkdir /root/llm-project/NFGen+KAN/Results/${protocol}/;
fi

if [ ! -d /root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/ ]; then
    mkdir /root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/;
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

# 清理可能存在的旧进程
echo "Cleaning up any existing ${protocol} processes..."
pkill -f "${protocol}" || true
sleep 3

target_networks=("adult" "breast_cancer")

for network in "${target_networks[@]}"; do
    echo "Testing ${network} ..."

    if [ ${network} == "adult" ]; then
        sourceFiles=(easy_adult)
        for sourceFile in "${sourceFiles[@]}"; do
            if [ ${nth} == 0 ] || [ ${nth} == 1 ] || [ ${nth} == 5 ]; then
                python compile.py -R 288 ${sourceFile} > ${clogFile}_${sourceFile} &
            else
                python compile.py -F 128 ${sourceFile} > ${clogFile}_${sourceFile} &
            fi
        done
    elif [ ${network} == "breast_cancer" ]; then
        sourceFiles=(breast_logistic breast_tree)
        for sourceFile in "${sourceFiles[@]}"; do
            if [ ${nth} == 0 ] || [ ${nth} == 1 ] || [ ${nth} == 5 ]; then
                python compile.py -R 288 ${sourceFile} > ${clogFile}_${sourceFile} &
            else
                python compile.py -F 128 ${sourceFile} > ${clogFile}_${sourceFile} &
            fi
        done
    fi
done
wait;

for network in "${target_networks[@]}"; do
    echo "Executing ${network} ..."
    
    if [ ${network} == "adult" ]; then
        sourceFiles=(easy_adult)
    elif [ ${network} == "breast_cancer" ]; then
        sourceFiles=(breast_logistic breast_tree)
    fi

    for sourceFile in "${sourceFiles[@]}"; do
        echo "Starting execution for ${sourceFile}..."
        
        # 清理可能存在的旧进程
        pkill -f "${protocol}.*${sourceFile}" || true
        sleep 2
        
        # 确保端口释放
        if [ $nth -eq 5 ]; then
            ./${protocol} -p 0 ${sourceFile} -v >> ${logFile}_${sourceFile}.log 2>&1 & ./${protocol} -p 1 -v ${sourceFile} & ./${protocol} -p 2 ${sourceFile} -v & ./${protocol} -p 3 ${sourceFile} -v &
        else
            # for performance test, ssh to the virtual hosts and run the programs!
            ./${protocol} -p 0 ${sourceFile} -v >> ${logFile}_${sourceFile}.log 2>&1 & ./${protocol} -p 1 -v ${sourceFile} & ./${protocol} -p 2 ${sourceFile} -v &
        fi
        wait;
        echo "Execution for ${sourceFile} completed."
    done
done