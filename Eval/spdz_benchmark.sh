logFolder=./Record/benchmark_spdz_origional/
clogFolder=./Record/bso_compile/
clogFile=${clogFolder}compile_log
sourceFile=benchmark_spdz_origional
protocol=replicated-ring-party.x

BuildFlag=False
CompileOnly=True

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
fi

# N_list=(1 1 1 1)
# M_list=(16777216 268435456 1073741824)
# parallel_list=(1 1 1 1)

N_list=(1)
M_list=(16777216)
parallel_list=(1)
param_len=${#M_list[@]}
task_list=(cipher_index)
REPEAT=1

if [ $BuildFlag = True ]; then
    
    cd ..
    scp -r ./MP-SPDZ/CONFIG.mine spdz1:~/MP-SPDZ/ &
    scp -r ./MP-SPDZ/CONFIG.mine spdz2:~/MP-SPDZ
    wait;
    cd ./MP-SPDZ/;

    make -j 8 replicated-ring-party.x &
    ssh spdz1 "cd ./MP-SPDZ/; make -j 8 replicated-ring-party.x" &
    ssh spdz2 "cd ./MP-SPDZ/; make -j 8 replicated-ring-party.x" &
    wait;

fi

# compile the baseline functions.
for ((i=0; i<param_len; i++)); do
    M=${M_list[i]}; N=${N_list[i]}; parallel=${parallel_list[i]};
    for task in ${task_list[*]}; do
        clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel};
        bc_file=./Programs/Schedules/${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel}.sch 
        if [ -f ${bc_file} ]; then
            continue
        fi
        python compile.py -R 256 -l ${sourceFile} ${task} $N $M $REPEAT $parallel > ${clog} 2>&1 &
        wait;
    done;
done;

if [ $CompileOnle = True ]; then
    exit;
fi

# synchronized with other machines.
cd ..
scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
wait;
cd ./MP-SPDZ/;

./Eval/control/setup_ssl.sh;


# execute.
for ((i=0; i<param_len; i++)); do
    M=${M_list[i]}; N=${N_list[i]}; parallel=${parallel_list[i]};
    for task in ${task_list[*]}; do

        recordFolder=${logFolder}Record_${task}
        logFile=${recordFolder}/Record-bso-baseline
        if [ ! -d ${recordFolder} ]; then
            mkdir ${recordFolder};
        fi
        elog=${logFile}-${task}-n=${N}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
        ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}  
        wait;
    done;
done;