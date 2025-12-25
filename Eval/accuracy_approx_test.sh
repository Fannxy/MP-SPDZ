set -e

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")
nth=5

protocol=${programs[${nth}]}
script=${scripts[${nth}]}

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/approx_logs/
clogFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/approx_logs/Compile/
clogFile=${clogFolder}approx_compile_log
logFile=${logFolder}approx_execution_log
sourceFile=multivariate_accuracy_approx

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
# else
#     rm -r ${logFolder}*
fi

if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
# else
#     rm -r ${clogFolder}*
fi

target_funcs=("func4" "func12")
# target_funcs=("func1" "func2" "func3" "func4" "func5" "func6" "func7" "func8" "func9" "func15")
# target_funcs=("func1" "func2" "func3" "func4" "func5" "func6" "func7" "func8" "func9" "func10" "func11" "func12" "func13" "func14" "func15")

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
done