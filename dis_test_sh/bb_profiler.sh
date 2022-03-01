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

# protocol=./replicated-ring-party.x
# protocol=./ps-rep-ring-party.x
# echo -e "Protocol - ${protocol}" >> ${logFile};

# if [ ${mode} == "compile" ]; then
#     echo "compile here" ;

#     cd ./MP-SPDZ/
#     ./compile.py -R 256 ${sourceFile} others >> ${compileLog} & 
#     cd ..

#     compile_command="cd ./MP-SPDZ/; ./compile.py -R 256 ${sourceFile} others;"
#     ssh mp-spdz131 ${compile_command} & 
#     ssh mp-spdz132 ${compile_command}
# fi
# wait;

# if [ ${mode} == "exec" ]; then
#     cd ./MP-SPDZ 
#     ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-others ${logFolder} & 
#     ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-others ${logFolder}" &
#     ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-others ${logFolder}"
# fi
# wait;

# echo "compile here" ;
# cd ./MP-SPDZ/
# ./compile.py -R 256 ${sourceFile} others >> ${compileLog} & 
# cd ..
# compile_command="cd ./MP-SPDZ/; ./compile.py -R 256 ${sourceFile} others;"
# ssh mp-spdz131 ${compile_command} & 
# ssh mp-spdz132 ${compile_command}
# wait;


# cd ./MP-SPDZ 
# ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-others ${logFolder} & 
# ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-others ${logFolder}" &
# ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-others ${logFolder}"
# wait;


# protocol=./rep-field-party.x
# echo -e "Protocol - ${protocol}" >> ${logFile};

# echo "compile here" ;
# cd ./MP-SPDZ/
# ./compile.py ${sourceFile} field >> ${compileLog} & 
# cd ..
# compile_command="cd ./MP-SPDZ/; ./compile.py ${sourceFile} field;"
# ssh mp-spdz131 ${compile_command} & 
# ssh mp-spdz132 ${compile_command}
# wait;


# protocol=./replicated-field-party.x
# echo -e "Protocol - ${protocol}" >> ${logFile};

# cd ./MP-SPDZ 
# ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-field ${logFolder} & 
# ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-field ${logFolder}" &
# ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-field ${logFolder}"
# wait;


echo "compile here" ;
cd ./MP-SPDZ/
./compile.py ${sourceFile} field >> ${compileLog}
cd ..
# compile_command="cd ./MP-SPDZ/; ./compile.py ${sourceFile} field;"
# ssh mp-spdz131 ${compile_command} & 
# ssh mp-spdz132 ${compile_command}
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;


protocol=./ps-rep-field-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};

cd ./MP-SPDZ 
./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-field ${logFolder} & 
ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-field ${logFolder}" &
ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-field ${logFolder}"
wait;


# protocol=./shamir-party.x
# echo -e "Protocol - ${protocol}" >> ${logFile};

# cd ./MP-SPDZ 
# ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-field ${logFolder} & 
# ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-field ${logFolder}" &
# ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-field ${logFolder}"
# wait;
