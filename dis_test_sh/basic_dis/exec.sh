party=$1
protocol=$2
sourceFile=$3
logFolder=$4

echo "Test $3 using protocol $2"
logFile=${logFolder}log-$3.txt
logTmp=${logFolder}tmp.txt

if [ ${party} == 0]; then
    echo "\n\nTest $3 using protocol $2 \n" >> ${logFile}
fi

if [ ${party} == 0]; then
    ${protocol} -p ${party} ${sourceFile} >> ${logFile};
    else
    ${protocol} -p ${party} ${sourceFile} >> ${logTmp};
fi
wait;

if [ ${party} == 0]; then
    echo "Success" >> ${logFile}
fi

