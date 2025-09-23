logFolder=./Record/
clogFolder=./Record/Compile/
clogFile=${clogFolder}compile_log
logFile=${logFolder}vector_log
sourceFile=test_nfgen
protocol=replicated-ring-party.x


if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
else
    rm -r ${logFolder}*
fi

if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
else
    rm -r ${clogFolder}*
fi


# task_list=(mul gt eq)
# data_type_list=(sint sfix)
# n_list=(10 100 1000)
# repeats_list=(1000 100 10)

# compile
python compile.py ${sourceFile} > ${taskCompile} &
wait;

# execute
./Eval/local_exec.sh ${sourceFile} ${protocol} ${logFolder} ${logFile}
wait;


# # compile
# for data_type in ${data_type_list[*]}; do
#     for task in ${task_list[*]}; do  
#         # compile
#         start=0
#         for (( i=0; i<${#n_list[@]}; i++ )); do
#             n=${n_list[$i]}; repeat=${repeats_list[$i]}
#             taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
#             python compile.py -R 128 -Z 3 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
#         done
#         start=$((start+length))
#         wait;
#     done
# done
# wait;

# execution
# for data_type in ${data_type_list[*]}; do
#     for task in ${task_list[*]}; do  
#         start=0
#         for (( i=0; i<${#n_list[@]}; i++ )); do
#             n=${n_list[$i]}; repeat=${repeats_list[$i]}
#             ./Eval/basic/local_exec.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} ${protocol} ${logFolder} ${logFile}-${task}-${data_type}
#         done
#         start=$((start+length))
#         wait;
#     done
# done
# wait;