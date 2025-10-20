logFolder=./Record_neuron/
clogFolder=./Record_neuron/Compile/
clogFile=${clogFolder}compile_log
logFile=${logFolder}execution_log
sourceFile=test_neuron_rounds
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

neuron_list=(000 001 002 010 011 012 100 110 120)

# compile
for neuron in ${neuron_list[@]}; do
    python compile.py -R 144 ${sourceFile} ${neuron} > ${clogFile}-${neuron} &
    wait;

    ./Eval/local_exec.sh ${sourceFile}-${neuron} ${protocol} ${logFolder} ${logFile}-${neuron}
    wait;
done