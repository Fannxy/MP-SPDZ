prot=$1; func=$2; party=$3;
MAIN_FOLDER=/root/RoundRole/MP-SPDZ
logFolder=$MAIN_FOLDER/Record
execLog=${logFolder}/log-${prot}-${func}

# mkdir $logFolder if it dose not exist
if [ ! -d $logFolder ]; then
    mkdir $logFolder
fi

# run the program.
if [ ${party} == 2 ]; then
    ./${prot} -p 0 ${func} -v &>> ${execLog}-0 & 
    ./${prot} -p 1 ${func} -v &>> ${execLog}-1 &
    wait;
    party_logs=(${execLog}-0 ${execLog}-1);
elif [ ${party} == 3 ]; then
    ./${prot} -p 0 ${func} -v &>> ${execLog}-0 &
    ./${prot} -p 1 ${func} -v &>> ${execLog}-1 &
    ./${prot} -p 2 ${func} -v &>> ${execLog}-2 &
    wait;

    party_logs=(${execLog}-0 ${execLog}-1 ${execLog}-2);
fi

./Eval/clean_ports.sh

> ${execLog};
for log in ${party_logs[@]}
do
    echo "==================== ${log} ====================" >> ${execLog}
    cat ${log} >> ${execLog}
    rm ${log}
done