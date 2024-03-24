logFolder=./Record/pta_analysis/
clogFolder=./Record/analysis_compile/
monitorFolder=./Record/Monitor/log
clogFile=${clogFolder}compile_log
sourceFile=pta_baseline
protocol=replicated-ring-party.x

exec_perf='/usr/lib/linux-tools/4.15.0-20-generic/perf'


if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
fi


N=1; REPEAT=1;
M_list=(1073741824)
parallel_list=(256)
task_list=(cipher_index)

# compile multithreaded version
for M in ${M_list[*]}; do
    for task in ${task_list[*]}; do
        for parallel in ${parallel_list[*]}; do
            clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel};
            memlog=${monitorFolder}-compile-${task}-N=${N}-M=${M}-c=${parallel}2;
            ./Eval/control/mem_monitor.sh ${memlog} &
            monitor_id=$!
            echo "here"
            python compile.py -l -R 64 -Z 3 ${sourceFile} ${task} $N $M $REPEAT $parallel > ${clog}
            # wait;
            echo "after compile"
            kill ${monitor_id};
        done;
    done;
done;

# synchronized with other machines.
cd ..
scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ/
wait;
cd ./MP-SPDZ/;

./Eval/control/setup_ssl.sh;

for task in ${task_list[*]}; do
    recordFolder=${logFolder}Record_${task}
    logFile=${recordFolder}/Record-baseline
    if [ ! -d ${recordFolder} ]; then
        mkdir ${recordFolder};
    # else
    #     rm -r ${recordFolder}*
    fi
    for parallel in ${parallel_list[*]}; do
        for M in ${M_list[*]}; do
            elog=${logFile}-multithread-${task}-n=${N}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
            memlog=${monitorFolder}-exec-${task}-N=${N}-M=${M}-c=${parallel};
            ./Eval/control/mem_monitor.sh ${memlog} &
            monitor_id=$!
            ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}
            kill ${monitor_id};
        done;
    done;
done;
