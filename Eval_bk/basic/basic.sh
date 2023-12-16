task=$1
protocol=$2
logFolder=$3
logFile=$4

echo "Test $1 using protocol $2"

logTmp=${logFolder}tmp.txt

echo "\n\nTest $1 using protocol $2 \n" >> ${logFile}

./${protocol} -p 0 ${task} >> ${logFile} 2>&1 & ./${protocol} -p 1 ${task} >> ${logTmp} & ./${protocol} -p 2 ${task} >> ${logTmp} &
wait
echo "Success" >> ${logFile}
