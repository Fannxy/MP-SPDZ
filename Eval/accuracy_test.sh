logFolder=./Record_accuracy_baseline/
clogFolder=./Record_accuracy_baseline/Compile/
clogFile=${clogFolder}compile_log
logFile=${logFolder}execution_log
sourceFile=multivariate_accuracy_baseline
protocol=replicated-ring-party.x


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

for func in "${target_funcs[@]}"; do
    echo "Testing ${func} ..."
    
    # compile
    python compile.py -R 144 ${sourceFile} -D ${func} > ${clogFile}_${func} &
    # wait;
done
wait;

for func in "${target_funcs[@]}"; do
    echo "Executing ${func} ..."
    
    # execute
    ./Eval/local_exec.sh ${sourceFile}-${func} ${protocol} ${logFolder} ${logFile}_${func}
    wait;
done

# # compile
# python compile.py -R 144 ${sourceFile} > ${clogFile} &
# wait;

# # execute
# ./Eval/local_exec.sh ${sourceFile} ${protocol} ${logFolder} ${logFile}
# wait;