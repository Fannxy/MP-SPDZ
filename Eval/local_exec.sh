task=$1; protocol=$2; logFolder=$3; logFile=$4; nth=$5

echo -e "Test $1 using protocol $2"

logTmp=/dev/null

echo -e "\n\nTest $1 using protocol $2 \n" >> ${logFile}

if [ $nth -eq 5 ]; then
    ./${protocol} -p 0 ${task} -v >> ${logFile} 2>&1 & ./${protocol} -p 1 -v ${task} >> ${logTmp} & ./${protocol} -p 2 ${task} -v >> ${logTmp} & ./${protocol} -p 3 ${task} -v >> ${logTmp} &
else
    # for performance test, ssh to the virtual hosts and run the programs!
    ./${protocol} -p 0 ${task} -v >> ${logFile} 2>&1 & ./${protocol} -p 1 -v ${task} >> ${logTmp} & ./${protocol} -p 2 ${task} -v >> ${logTmp} &
fi
wait;
echo -e "Success" >> ${logFile}
