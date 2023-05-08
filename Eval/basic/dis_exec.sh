task=$1
protocol=$2
logFolder=$3
logFile=$4
party=$5

if [ -z "$6" ]; then
    batch_size=-1;
else
    # echo ">>>>>>>>>>> batch-size: "$6 >> ${logFile}
    batch_size=$6;
    batch_size=$((batch_size*100))
    # batch_size=$(( $6 * $6 ));
    # batch_size=100000;
    echo ">>>>>>>>>>> batch-size: "$batch_size >> ${logFile}
fi

logTmp=${logFolder}tmp.txt

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi
wait;

if [ ${party} == 0 ]; then
    echo -e "Test $1 using protocol $2" >> ${logFile}
fi

if [ ${party} == 0 ]; then
    ./${protocol} -p ${party} ${task} --ip-file-name HOST --batch-size ${batch_size} >> ${logFile} 2>&1;
else
    ./${protocol} -p ${party} ${task} --ip-file-name HOST --batch-size ${batch_size} >> ${logTmp};
fi
wait;

if [ ${party} == 0 ]; then
    echo "Success" >> ${logFile}
fi
