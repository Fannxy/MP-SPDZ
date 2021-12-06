echo "Test $1 using protocol $2"
if [ ! -n "$3" ] ;then
    logFile=./record/log-$2.txt
else
    logFile=./record/log-$3.txt
fi

logTmp=./record/tmp.txt

echo "\n\nTest $1 using protocol $2 \n" >> ${logFile}

./$2 -p 0 $1 > ${logFile} & ./$2 -p 1 $1 >> ${logTmp} & ./$2 -p 2 $1 >> ${logTmp} &
wait
echo "Success" >> ${logFile}