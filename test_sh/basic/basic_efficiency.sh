logFolder=$4

echo "Test $1 using protocol $2"
if [ ! -n "$3" ] ;then
    logFile=${logFolder}log-$2.txt
else
    logFile=${logFolder}log-$3.txt
fi

logTmp=${logFolder}tmp.txt

echo "\n\nTest $1 using protocol $2 \n" >> ${logFile}

./$2 -p 0 $1 >> ${logFile} & ./$2 -p 1 $1 >> ${logTmp} & ./$2 -p 2 $1 >> ${logTmp} &
wait
echo "Success" >> ${logFile}