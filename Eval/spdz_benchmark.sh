logFolder=./Record/benchmark_spdz_origional/
clogFolder=./Record/bso_compile/
clogFile=${clogFolder}compile_log
sourceFile=benchmark_spdz_origional
protocol=replicated-ring-party.x

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
fi

N_list=(1 1)
M_list=(1024 16384)
parallel_list=(16 64)
param_len=${#M_list[@]}
task_list=(cipher_index)
REPEAT=1

# compile the baseline functions.
for ((i=0; i<param_len; i++)); do
    M=${M_list[i]}; N=${N_list[i]}; parallel=${parallel_list[i]};
    for task in ${task_list[*]}; do
        clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel};
        python compile.py -l -R 64 -Z 3 ${sourceFile} ${task} $N $M $REPEAT $parallel > ${clog} &
        wait;
    done;
done;

# synchronized with other machines.
cd ..
scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
wait;
scp -r ./MP-SPDZ/*.x spdz1:~/MP-SPDZ/  &
scp -r ./MP-SPDZ/*.x spdz2:~/MP-SPDZ/
wait;
scp -r ./MP-SPDZ/*.so spdz1:~/MP-SPDZ/  &
scp -r ./MP-SPDZ/*.so spdz2:~/MP-SPDZ/
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
            echo "in this line!"
            mkdir ${recordFolder};
        fi
        elog=${logFile}-${task}-n=${N}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
        ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}  
        wait;
    done;
done;

# for M in ${M_list[*]}; do
#     for task in ${task_list[*]}; do
#         for parallel in ${parallel_list[*]}; do
#             clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel};
#             python compile.py -l -R 64 -Z 3 ${sourceFile} ${task} $N $M $REPEAT $parallel > ${clog} &
#             wait;
#         done;
#     done;
# done;
