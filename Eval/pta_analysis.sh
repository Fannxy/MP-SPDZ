logFolder=./Record/pta_analysis_bk/
clogFolder=./Record/analysis_compile/
clogFile=${clogFolder}compile_log
sourceFile=pta_baseline
protocol=replicated-ring-party.x


if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
fi


# N=1; REPEAT=1;
# M_list=(1024 16384 32768)
# parallel_list=(16 32 64)
# task_list=(max)

# # compile multithreaded version
# for M in ${M_list[*]}; do
#     for task in ${task_list[*]}; do
#         for parallel in ${parallel_list[*]}; do
#             clog=${clogFile}-${task}-${M}-${M}-${REPEAT}-${parallel};
#             python compile.py -l -R 64 -Z 3 ${sourceFile} ${task} $M $M $REPEAT $parallel > ${clog} &
#         done;
#         wait;
#     done;
# done;

# # synchronized with other machines.
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
# wait;
# cd ./MP-SPDZ/;

# ./Eval/control/setup_ssl.sh;

# # execute multithreaded
# for task in ${task_list[*]}; do
#     recordFolder=${logFolder}Record_${task}
#     logFile=${recordFolder}/Record-baseline
#     if [ ! -d ${recordFolder} ]; then
#         mkdir ${recordFolder};
#     fi
#     for parallel in ${parallel_list[*]}; do
#         for M in ${M_list[*]}; do
#             elog=${logFile}-multithread-${task}-n=${M}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
#             # ./Eval/basic/local_exec.sh ${sourceFile}-multithread-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${logFolder} ${elog}
#             ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${M}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}
#             wait;
#         done;
#     done;
# done;


N=1; REPEAT=1;
M_list=(1048576 268435456)
parallel_list=(16 64)
task_list=(average new_search metric)

# compile multithreaded version
for M in ${M_list[*]}; do
    for task in ${task_list[*]}; do
        for parallel in ${parallel_list[*]}; do
            clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel};
            python compile.py -l -R 64 -Z 3 ${sourceFile} ${task} $N $M $REPEAT $parallel > ${clog} &
            wait;
        done;
    done;
done;

# synchronized with other machines.
cd ..
scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
wait;
cd ./MP-SPDZ/;

./Eval/control/setup_ssl.sh;

# execute multithreaded
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
            # ./Eval/basic/local_exec.sh ${sourceFile}-multithread-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${logFolder} ${elog}
            ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}
            wait;
        done;
    done;
done;


# N=1; REPEAT=1;
# M_list=(1073741824)
# parallel_list=(256)
# task_list=(average)

# # compile multithreaded version
# for task in ${task_list[*]}; do
#     for M in ${M_list[*]}; do
#         for parallel in ${parallel_list[*]}; do
#             clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel};
#             python compile.py -l -R 64 -Z 3 ${sourceFile} ${task} $N $M $REPEAT $parallel > ${clog} &
#             wait;
#         done;
#     done;
# done;

# # synchronized with other machines.
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
# wait;
# cd ./MP-SPDZ/;

# ./Eval/control/setup_ssl.sh;

# # execute multithreaded
# for task in ${task_list[*]}; do
#     recordFolder=${logFolder}Record_${task}
#     logFile=${recordFolder}/Record-baseline
#     if [ ! -d ${recordFolder} ]; then
#         mkdir ${recordFolder};
#     # else
#     #     rm -r ${recordFolder}*
#     fi
#     for parallel in ${parallel_list[*]}; do
#         for M in ${M_list[*]}; do
#             elog=${logFile}-multithread-${task}-n=${N}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
#             # ./Eval/basic/local_exec.sh ${sourceFile}-multithread-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${logFolder} ${elog}
#             ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}
#             wait;
#         done;
#     done;
# done;



# REPEAT=1;
# M_list=(1024 16384 32768 65536)
# parallel_list=(256)
# task_list=(max)
# # compile multithreaded version
# for task in ${task_list[*]}; do
#     for M in ${M_list[*]}; do
#         for parallel in ${parallel_list[*]}; do
#             clog=${clogFile}-${task}-${M}-${M}-${REPEAT}-${parallel};
#             python compile.py -l -R 64 -Z 3 ${sourceFile} ${task} $M $M $REPEAT $parallel > ${clog} &
#             wait;
#         done;
#     done;
# done;

# # synchronized with other machines.
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
# wait;
# cd ./MP-SPDZ/;

# ./Eval/control/setup_ssl.sh;

# # execute multithreaded
# for task in ${task_list[*]}; do
#     recordFolder=${logFolder}Record_${task}
#     logFile=${recordFolder}/Record-baseline
#     if [ ! -d ${recordFolder} ]; then
#         mkdir ${recordFolder};
#     # else
#     #     rm -r ${recordFolder}*
#     fi
#     for parallel in ${parallel_list[*]}; do
#         for M in ${M_list[*]}; do
#             elog=${logFile}-multithread-${task}-n=${M}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
#             ./Eval/basic/dis_exec.sh ${sourceFile}-${task}-${M}-${M}-${REPEAT}-${parallel} ${protocol} ${recordFolder} ${elog}
#             wait;
#         done;
#     done;
# done;
