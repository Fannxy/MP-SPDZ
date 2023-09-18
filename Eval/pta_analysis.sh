logFolder=./Record/pta_analysis/
clogFolder=./Record/analysis_compile/
clogFile=${clogFolder}compile_log
sourceFile=pta_baseline
protocol=replicated-ring-party.x
task=cipher_index

recordFolder=${logFolder}Record_${task}
logFile=${logFolder}Record-baseline

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

if [ ! -d ${recordFolder} ]; then
    mkdir ${recordFolder};
else
    rm -r ${recordFolder}*
fi

N=1; REPEAT=10
M_list=(1048576 4194304 16777216 67108864 268435456 1073741824)
parallel_list=(128 256)


# compile multithreaded version
for parallel in ${parallel_list[*]}; do
    for M in ${M_list[*]}; do
        clog=${clogFile}-multithread-${N}-${M}-${REPEAT}-${parallel};
        python compile.py -l -R 64 -Z 3 ${sourceFile} multithread $N $M $REPEAT $parallel > ${clog} &
    done;
    wait;
done;
wait;

# # execute multithreaded
# for parallel in ${parallel_list[*]}; do
#     for M in ${M_list[*]}; do
#         elog=${logFile}-multithread-${task}-n=${N}-m=${M}-k=1-R=${REPEAT}-c=${parallel};
#         ./Eval/basic/local_exec.sh ${sourceFile}-multithread-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${logFolder} ${elog}
#         wait;
#     done;
# done;


# # compile simple for version
# for M in ${M_list[*]}; do
#     clog=${clogFile}-for-${N}-${M}-${REPEAT}
#     python compile.py -l -R 64 -Z 3 ${sourceFile} for $N $M $REPEAT 1 > ${clog} &
# done;
# wait;

# # execute for
# for M in ${M_list[*]}; do
#     elog=${logFile}-for-${N}-${M}-${REPEAT}
#     ./Eval/basic/local_exec.sh ${sourceFile}-for-${N}-${M}-${REPEAT} ${protocol} ${logFolder} ${elog}
#     wait;
# done;
