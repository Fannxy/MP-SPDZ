echo "==== Test basic building blocks ===="
mode=$1

logFolder=~/MP-SPDZ/Record/dis_basic_profiler/
logFile=${logFolder}profiler
logTmp=${logFolder}tmp
sourceFile=bb_profiler
compileLog=${logFolder}compile

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

protocol=./replicated-ring-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};

if [ ${mode} == "compile" ]; then
    echo "compile here" ;
    # compile_command_main="cd ./MP-SPDZ/ ./compile.py -R 256 ${sourceFile} ring >> ${compileLog};"

    cd ./MP-SPDZ/
    ./compile.py -R 256 ${sourceFile} ring >> ${compileLog} & 
    cd ..

    compile_command="cd ./MP-SPDZ/; ./compile.py -R 256 ${sourceFile} ring;"
    ssh mp-spdz131 ${compile_command} & 
    ssh mp-spdz132 ${compile_command}
fi
wait;

if [ ${mode} == "exec" ]; then
    cd ./MP-SPDZ 
    ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-ring ${logFolder} & 
    cd ..
    ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-ring ${logFolder}" &
    ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-ring ${logFolder}"
fi
wait;