task=$1; protocol=$2; logFolder=$3; logFile=$4

echo -e "Test $1 using protocol $2"
logTmp=${logFolder}tmp.txt
echo -e "\n\nTest $1 using protocol $2 \n" >> ${logFile}

./Eval/basic/dis_exec_unit.sh ${task} ${protocol} ${logFolder} ${logFile} 0 &
ssh spdz1 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec_unit.sh ${task} ${protocol} ${logFolder} ${logFile} 1" >> /dev/null &
ssh spdz2 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec_unit.sh ${task} ${protocol} ${logFolder} ${logFile} 2" >> /dev/null &
wait;