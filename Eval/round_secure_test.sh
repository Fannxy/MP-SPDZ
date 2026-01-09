set -e

nth=$1
N=1
variant="secure"

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")

protocol=${programs[${nth}]}
script=${scripts[${nth}]}

MP_SPDZ_DIR=/root/MP-SPDZ/
logFolder=/root/MP-SPDZ/Results/${protocol}/accuracy/${variant}_approx_logs/
clogFolder=${logFolder}Compile/
clogFile=${clogFolder}${variant}_approx_compile_log
logFile=${logFolder}${variant}_approx_execution_log
sourceFile=multivariate_approx_comparison

target_funcs=("func1" "func2" "func3" "func4" "func5" "func6" "func7" "func8" "func9" "func10" "func11" "func12" "func13" "func14" "func15")
# target_funcs=("func1")

mkdir -p ${logFolder}
mkdir -p ${clogFolder}

for func in "${target_funcs[@]}"; do
    echo "Testing ${func} (${variant}) ..."
    if [ ${nth} == 0 ] || [ ${nth} == 1 ] || [ ${nth} == 5 ]; then
        python compile.py -R 288 --optimize-hard --flow-optimization -b 1000000 ${sourceFile} ${func} ${N} ${nth} ${variant} > ${clogFile}_${func} &
    else
        python compile.py -F 128 --optimize-hard --flow-optimization -b 1000000 ${sourceFile} ${func} ${N} ${nth} ${variant} > ${clogFile}_${func} &
    fi
    wait
done

for func in "${target_funcs[@]}"; do
    echo "Executing ${func} (${variant}) ..."
    compiled_name=${sourceFile}-${func}-${N}-${nth}-${variant}
    ./Eval/local_exec.sh ${compiled_name} ${protocol} ${logFolder} ${logFile}_${func} ${nth}
    wait
done
