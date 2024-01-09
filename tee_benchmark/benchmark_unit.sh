prot=$1; func=$2;
logFolder=./tee_benchmark/Record/
# exec_perf='/usr/lib/linux-tools/4.15.0-20-generic/perf'

declare -A protocol
protocol["repring"]=./replicated-ring-party.x
protocol["repfield"]=./replicated-field-party.x
protocol["psrepring"]=./ps-rep-ring-party.x
protocol["psrepfield"]=./ps-rep-field-party.x
protocol["semi2k"]=./semi2k-party.x
protocol["semi"]=./semi-party.x
protocol["spdz"]=./spdz2k-party.x
protocol["mascot"]=./mascot-party.x

declare -A parties
parties["repring"]=3; parties["repfield"]=3; 
parties["psrepring"]=3; parties["psrepfield"]=3;
parties["semi2k"]=2; parties["semi"]=2;
parties["spdz"]=2; parties["mascot"]=2;

declare -A modular
modular["repring"]=r; modular["repfield"]=f; 
modular["psrepring"]=r; modular["psrepfield"]=f;
modular["semi2k"]=r; modular["semi"]=f;
modular["spdz"]=r; modular["mascot"]=f;

declare -A benchmark
benchmark["lr"]=breast_logistic
benchmark["oppe"]=sigmoid
benchmark["oram"]=oram
benchmark["comp"]=comp

compileLog=${logFolder}comp_log

if [ ${modular[$prot]} == "r" ]; then 
    ./compile.py -R 64 ${benchmark[$func]} > ${compileLog}
fi
if [ ${modular[$prot]} == "f" ]; then 
    ./compile.py ${benchmark[$func]} > ${compileLog}
fi

logFile=${logFolder}${func}_${prot}_log
logTmp=${logFolder}tmp

if [ ${parties[$prot]} == 2 ]; then
    ./${protocol[$prot]} -p 0 ${benchmark[$func]} &>> ${logFile}0 & 
    # pid=$!  
    # ${exec_perf} record -g -F 180 -p $pid -o ./Perf/${prot}.data &
    ./${protocol[$prot]} -p 1 ${benchmark[$func]} &>> ${logFile}1;
fi
wait;
if [ ${parties[$prot]} == 3 ]; then
    ./${protocol[$prot]} -p 0 ${benchmark[$func]} &>> ${logFile} & 
    # pid=$!  
    # ${exec_perf} record -g -F 180 -p $pid -o ./Perf/${prot}.data &
    ./${protocol[$prot]} -p 1 ${benchmark[$func]} &>> ${logTmp} &
    ./${protocol[$prot]} -p 2 ${benchmark[$func]} &>> ${logTmp};
fi
wait;
