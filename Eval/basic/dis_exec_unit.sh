task=$1; protocol=$2; logFolder=$3; logFile=$4; party=$5;

logTmp=${logFolder}/tmp.txt

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi
wait;

if [ ${party} == 0 ]; then
    echo -e "Test $1 using protocol $2" >> ${logFile}
fi

if [ ${party} == 0 ]; then
    ulimit -n 65536; ./${protocol} ${task} -p ${party} -ip HOST >> ${logFile} 2>&1;
else
    ulimit -n 65536; ./${protocol} ${task} -p ${party} -ip HOST >> ${logTmp};
fi
wait;

if [ ${party} == 0 ]; then
    echo "Success" >> ${logFile}
fi
