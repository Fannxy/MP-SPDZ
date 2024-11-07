prot=$1; func=$2; party=$3;
MAIN_FOLDER=/root/RoundRole/MP-SPDZ
logFolder=$MAIN_FOLDER/Record
execLog=${logFolder}/log-${prot}-${func}
NETWORK_INTERFACE0=

# mkdir $logFolder if it dose not exist
if [ ! -d $logFolder ]; then
    mkdir $logFolder
fi

scp -r ./Eval aby31:${MAIN_FOLDER}/ &
scp -r ./Eval aby32:${MAIN_FOLDER}/ &

# run the program.
if [ ${party} == 2 ]; then
    # ./${prot} -p 0 ${func} -v &>> ${execLog}-0 & 
    command="./${prot} -p 0 ${func} -v &>> ${execLog}-0"
    ./Eval/monitor_dis_run_profiler.py --keyword ${prot}-${func} --command "${command}" --record_folder ${logFolder} --interface &
    # ./${prot} -p 1 ${func} -v &>> ${execLog}-1 &
    ssh aby31 "cd ${MAIN_FOLDER}/; ./${prot} -p 1 ${func} -v &>> ${execLog}-1" &
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