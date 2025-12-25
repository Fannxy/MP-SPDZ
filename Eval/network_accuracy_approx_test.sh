set -e

programs=("replicated-ring-party.x" "ps-rep-ring-party.x" "replicated-field-party.x" "ps-rep-field-party.x" "shamir-party.x" "rep4-ring-party.x")
scripts=("ring.sh" "ps-rep-ring.sh" "rep-field.sh" "ps-rep-field.sh" "shamir.sh" "rep4-ring.sh")
nth=3

protocol=${programs[${nth}]}
script=${scripts[${nth}]}

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
logFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/network_approx_logs/
clogFolder=/root/llm-project/NFGen+KAN/Results/${protocol}/accuracy/network_approx_logs/Compile/
clogFile=${clogFolder}network_approx_compile_log
logFile=${logFolder}network_approx_execution_log
sourceFile=network_accuracy_approx

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

target_networks=("adult" "breast_cancer")

for network in "${target_networks[@]}"; do
    echo "Testing ${network} ..."
    if [ ${nth} == 0 ]; then
        python compile.py -R 288 ${sourceFile} ${network} ${nth} > ${clogFile}_${network} &
    elif [ ${nth} == 1 ]; then
        python compile.py -R 288 ${sourceFile} ${network} ${nth} > ${clogFile}_${network} &
    elif [ ${nth} == 5 ]; then
        python compile.py -R 288 ${sourceFile} ${network} ${nth} > ${clogFile}_${network} &
    else
        python compile.py -F 128 ${sourceFile} ${network} ${nth} > ${clogFile}_${network} &
    fi
done
wait;

for network in "${target_networks[@]}"; do
    echo "Executing ${network} ..."
    
    # execute
    ./Eval/local_exec.sh ${sourceFile}-${network}-${nth} ${protocol} ${logFolder} ${logFile}_${network} ${nth}
    wait;
done