set -e

nth=$1
N=1

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")

protocol=${programs[${nth}]}
script=${scripts[${nth}]}

MP_SPDZ_DIR=/root/MP-SPDZ/
logFolder=/root/MP-SPDZ/Results/${protocol}/accuracy/baseline_logs/
clogFolder=/root/MP-SPDZ/Results/${protocol}/accuracy/baseline_logs/Compile/
clogFile=${clogFolder}baseline_compile_log
logFile=${logFolder}baseline_execution_log
sourceFile=multivariate_baseline_performance

target_funcs=("func1" "func2" "func3" "func4" "func5" "func6" "func7" "func8" "func9" "func10" "func11" "func12" "func13" "func14" "func15")


mkdir -p ${logFolder}
mkdir -p ${clogFolder}


for func in "${target_funcs[@]}"; do
    echo "Testing ${func} ..."
    if [ ${nth} == 0 ]; then
        python compile.py -R 288 --optimize-hard --flow-optimization -b 1000000 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    elif [ ${nth} == 1 ]; then
        python compile.py -R 288 --optimize-hard --flow-optimization -b 1000000 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    elif [ ${nth} == 5 ]; then
        python compile.py -R 288 --optimize-hard --flow-optimization -b 1000000 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    else
        python compile.py -F 128 --optimize-hard --flow-optimization -b 1000000 ${sourceFile} ${func} ${N} ${nth} > ${clogFile}_${func} &
    fi
    wait;
done

for func in "${target_funcs[@]}"; do
    echo "Executing ${func} ..."
    
    # execute
    ./Eval/local_exec.sh ${sourceFile}-${func}-${N}-${nth} ${protocol} ${logFolder} ${logFile}_${func} ${nth}
    wait;
done