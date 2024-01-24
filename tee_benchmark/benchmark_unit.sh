prot=$1; func=$2;
logFolder=./tee_benchmark/Record/

declare -A protocol
protocol["repring"]=./replicated-ring-party.x
protocol["repfield"]=./replicated-field-party.x
protocol["psrepring"]=./ps-rep-ring-party.x
protocol["psrepfield"]=./ps-rep-field-party.x
protocol["semi2k"]=./semi2k-party.x
protocol["semi"]=./semi-party.x
protocol["spdz"]=./spdz2k-party.x
protocol["mascot"]=./mascot-party.x
protocol["semi-offline"]=./semi-offline.x
protocol["semi2k-offline"]=./semi2k-offline.x

declare -A parties
parties["repring"]=3; parties["repfield"]=3; 
parties["psrepring"]=3; parties["psrepfield"]=3;
parties["semi2k"]=2; parties["semi"]=2;
parties["spdz"]=2; parties["mascot"]=2;
parties["semi2k-offline"]=2; parties["semi-offline"]=2;

declare -A modular
modular["repring"]=r; modular["repfield"]=f; 
modular["psrepring"]=r; modular["psrepfield"]=f;
modular["semi2k"]=r; modular["semi"]=f;
modular["spdz"]=r; modular["mascot"]=f;
modular["semi2k-offline"]=r; modular["semi-offline"]=f;

declare -A benchmark
benchmark["lr"]=breast_logistic
benchmark["oppe"]=sigmoid
benchmark["oram"]=oram_tutorial
benchmark["comp"]=comp
benchmark["nn"]=benchmark_net

compileLog=${logFolder}comp_log

if [ ${modular[$prot]} == "r" ]; then 
    ./compile.py -R 64 ${benchmark[$func]} > ${compileLog}
fi
if [ ${modular[$prot]} == "f" ]; then 
    ./compile.py ${benchmark[$func]} > ${compileLog}
fi

cp -r ./Programs /Programs

logFile=${logFolder}${func}_${prot}_log.txt
logTmp=${logFolder}${func}_${prot}_tmp

if [ ${parties[$prot]} == 2 ]; then
    ./${protocol[$prot]} -p 0 ${benchmark[$func]} -v --encrypted &>> ${logFile} & 
    ./${protocol[$prot]} -p 1 ${benchmark[$func]} -v --encrypted &>> ${logTmp};
    # ./${protocol[$prot]} -p 0 ${benchmark[$func]} -v &>> ${logFile} & 
    # ./${protocol[$prot]} -p 1 ${benchmark[$func]} -v &>> ${logTmp};
fi
wait;
if [ ${parties[$prot]} == 3 ]; then
    ./${protocol[$prot]} -p 0 ${benchmark[$func]} -v &>> ${logFile} & 
    ./${protocol[$prot]} -p 1 ${benchmark[$func]} -v &>> ${logTmp} &
    ./${protocol[$prot]} -p 2 ${benchmark[$func]} -v &>> ${logTmp};
fi
wait;
