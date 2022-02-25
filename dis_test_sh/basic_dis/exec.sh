party=$1
protocol=$2
sourceFile=$3
logFolder=$4

echo "Test $3 using protocol $2"
logFile=${logFolder}log-$3.txt
logTmp=${logFolder}tmp.txt

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi
wait;

if [ ${party} == 0 ]; then
    echo -e "\n\nTest $3 using protocol $2 \n" >> ${logFile}
fi

if [ ${party} == 0 ]; then
    echo "here --- " 
    ${protocol} -p ${party} ${sourceFile} --ip-file-name HOST >> ${logFile} &
    else
    ${protocol} -p ${party} ${sourceFile} --ip-file-name HOST >> ${logTmp};
fi
wait;

if [ ${party} == 0 ]; then
    echo "Success" >> ${logFile}
fi

