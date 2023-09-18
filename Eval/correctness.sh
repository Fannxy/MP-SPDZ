logFolder=./Record/corr_test/
clogFolder=./Record/corr_compile/
clogFile=${clogFolder}compile_log
logFile=${logFolder}test_cipher_index
sourceFile=pta_correctness
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


N=10; REPEAT=10
M_list=(100)
parallel_list=(3)


# compile multithreaded version
for parallel in ${parallel_list[*]}; do
    for M in ${M_list[*]}; do
        clog=${clogFile}-multithread-${N}-${M}-${REPEAT}-${parallel};
        python compile.py -l -R 64 -Z 3 ${sourceFile} multithread $N $M $REPEAT $parallel > ${clog} &
    done;
    wait;
done;
wait;

# execute multithreaded
for parallel in ${parallel_list[*]}; do
    for M in ${M_list[*]}; do
        elog=${logFile}-multithread-${N}-${M}-${REPEAT}-${parallel};
        ./Eval/basic/local_exec.sh ${sourceFile}-multithread-${N}-${M}-${REPEAT}-${parallel} ${protocol} ${logFolder} ${elog}
        wait;
    done;
done;