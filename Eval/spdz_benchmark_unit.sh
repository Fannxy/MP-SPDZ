task=$1

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

parallel_list=(1 1 1 1)
N_list=(1 1 1 1)

declare -A ringsize
ringsize["cipher_index"]=256;
ringsize["max"]=64;
ringsize["average"]=64;
ringsize["metric"]=64;
echo "MOD = -DRING_SIZE=${ringsize[$task]}" > config.mine


declare -A MLists
MLists["cipher_index"]="1048576"
MLists["max"]="1024 4096 16384 32768"
MLists["average"]="1048576 16777216 268435456 1073741824"
MLists["metric"]="1048576 16777216 268435456 1073741824"


# M_list=(${MLists[$task]})
read -a M_list <<< ${MLists[$task]}
param_len=${#M_list[@]}
REPEAT=1

if [ $BuildFlag = True ]; then
    
    # cd ..
    # scp -r ./MP-SPDZ/CONFIG.mine spdz1:~/MP-SPDZ/ &
    # scp -r ./MP-SPDZ/CONFIG.mine spdz2:~/MP-SPDZ
    # wait;
    # cd ./MP-SPDZ/;

    make -j 8 replicated-ring-party.x &
    # ssh spdz1 "cd ./MP-SPDZ/; make -j 8 replicated-ring-party.x" &
    # ssh spdz2 "cd ./MP-SPDZ/; make -j 8 replicated-ring-party.x" &
    # wait;

fi

# compile the baseline functions.
for ((i=0; i<param_len; i++)); do
    M=${M_list[i]}; N=${N_list[i]}; parallel=${parallel_list[i]};
    clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel};
    bc_file=./Programs/Schedules/${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel}.sch 
    # if [ -f ${bc_file} ]; then
    #     continue
    # fi
    python compile.py -R ${ringsize[$task]} -l ${sourceFile} ${task} $N $M $REPEAT $parallel > ${clog} 2>&1 &
    wait;
done;

if [ $CompileOnly = True ]; then
    exit;
fi

# local run
for ((i=0; i<param_len; i++)); do
    M=${M_list[i]}; N=${N_list[i]}; parallel=${parallel_list[i]};
    for task in ${task_list[*]}; do

        recordFolder=${logFolder}Record_${task}
        logFile=${recordFolder}/Record-bso-baseline
        if [ ! -d ${recordFolder} ]; then
            mkdir ${recordFolder};
        fi
        elog=${logFile}-${task}-n=${N}-m=${M}-k=1-R=${REPEAT}-c=${parallel};

        ./Eval/basic/local_exec.sh ${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}

        wait;
    done;
done;


# # synchronized with other machines.
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
# wait;
# cd ./MP-SPDZ/;

# ./Eval/control/setup_ssl.sh;


# # execute.
# for ((i=0; i<param_len; i++)); do
#     M=${M_list[i]}; N=${N_list[i]}; parallel=${parallel_list[i]};
#     for task in ${task_list[*]}; do

#         recordFolder=${logFolder}Record_${task}
#         logFile=${recordFolder}/Record-bso-baseline
#         if [ ! -d ${recordFolder} ]; then
#             mkdir ${recordFolder};
#         fi
#         elog=${logFile}-${task}-n=${N}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
#         ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}  
#         wait;
#     done;
# done;