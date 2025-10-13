logFolder=./Record_accuracy/
clogFolder=./Record/Compile/
clogFile=${clogFolder}compile_log
logFile=${logFolder}execution_log
sourceFile=accuracy_test
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

# compile
python compile.py -R 144 ${sourceFile} > ${clogFile} &
wait;

# execute
./Eval/local_exec.sh ${sourceFile} ${protocol} ${logFolder} ${logFile}
wait;