set -e

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")
nth=5

protocol=${programs[${nth}]}
script=${scripts[${nth}]}

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/baseline_logs/
clogFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/baseline_logs/Compile/
clogFile=${clogFolder}baseline_compile_log
logFile=${logFolder}baseline_execution_log
sourceFile=multivariate_accuracy_baseline

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

# target_funcs=("func1")
target_funcs=("func1" "func2" "func3" "func4" "func5" "func6" "func7" "func8" "func9" "func15")

# ./Eval/network_start.sh ${bandwidth} ${latency} ${logFolder}

for func in "${target_funcs[@]}"; do
    echo "Testing ${func} ..."
    if [ ${nth} == 0 ]; then
        python compile.py -R 288 ${sourceFile} ${func} ${nth} > ${clogFile}_${func} &
    elif [ ${nth} == 1 ]; then
        python compile.py -R 288 ${sourceFile} ${func} ${nth} > ${clogFile}_${func} &
    elif [ ${nth} == 5 ]; then
        python compile.py -R 288 ${sourceFile} ${func} ${nth} > ${clogFile}_${func} &
    else
        python compile.py -F 128 ${sourceFile} ${func} ${nth} > ${clogFile}_${func} &
    fi
done
wait;

for func in "${target_funcs[@]}"; do
    echo "Executing ${func} ..."
    
    # execute
    ./Eval/local_exec.sh ${sourceFile}-${func}-${nth} ${protocol} ${logFolder} ${logFile}_${func} ${nth}
    wait;


    # for i in $(seq 1 3); do
    #     echo "Executing on h${i} ..."
    #     if [ $i -eq 1 ]; then
    #         ssh -n h${i} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${i-1} ${sourceFile}-${func} -v >> ${logFile}_${func}.log 2>&1" &
    #     else
    #         ssh -n h${i} "cd ${MP_SPDZ_DIR} && ./${protocol} -p ${i-1} ${sourceFile}-${func} -v" &
    #     fi
    # done
    # wait;
done

# # compile
# python compile.py -R 144 ${sourceFile} > ${clogFile} &
# wait;

# # execute
# ./Eval/local_exec.sh ${sourceFile} ${protocol} ${logFolder} ${logFile}
# wait;