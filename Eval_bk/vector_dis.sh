logFolder=./Record/Vector_latency_50ms/
clogFolder=./Record/basic_compile/
clogFile=${clogFolder}compile_log
logFile=${logFolder}vector_log
sourceFile=bb_profiler
# sourceFile=basic_profiler

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

# compile
# task_list=(gt eq mul)
task_list=(mul gt eq)

n_list=(10 13 17 23 30 40 54 71 95 126 167 222 294 390 517 686 910 1206 1599 2120 2811 3727 4941 6551 8685 11513 15264 20235 26826 35564 47148 62505 82864 109854 145634 193069 255954 339322 449843 596362 790604 1048113 1389495 1842069 2442053 3237457 4291934 5689866 7543120 10000000)
repeats_list=(100 77 59 44 34 25 19 15 11 8 6 5 4 3 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1)

n_list1=(10 13 17 23 30 40 54 71 95 126 167 222 294 390 517 686 910 1206 1599 2120 2811 3727 4941 6551 8685 11513 15264 20235 26826 35564 47148 62505 82864 109854)
n_list2=(145634 193069 255954 339322 449843 596362 790604 1048113)
n_list3=(1389495 1842069 2442053 3237457 4291934)
n_list4=(3237457 4291934)
n_list5=(5689866)
n_list6=(7543120)
n_list7=(10000000)

# compiled_n_lists=($n_list1 $n_list2 $n_list3 $n_list4)
compiled_n_lists=(  
    "${n_list1[*]}"  
    "${n_list2[*]}"  
    "${n_list3[*]}"  
    "${n_list4[*]}"  
    "${n_list5[*]}"  
    "${n_list6[*]}"  
    "${n_list7[*]}"  
)
# compiled_n_lists=(  
#     "${n_list[*]}"  
# )

data_type_list=(sint sfix)

# for data_type in ${data_type_list[*]}; do
#     for task in ${task_list[*]}; do  
#         # compile
#         start=0
#         for sub_list in "${compiled_n_lists[@]}"; do
#             sub_list=($sub_list)
#             length=${#sub_list[*]}
#             sub_repeats=("${repeats_list[@]:$start:$length}")
#             for (( i=0; i<${#sub_list[@]}; i++ )); do
#                 n=${sub_list[$i]}
#                 repeat=${sub_repeats[$i]}
#                 taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
#                 ./compile.py -R 128 -Z 3 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
#             done
#             start=$((start+length))
#             wait;
#         done
#         wait;
#     done
# done
# wait;

# # synchronize the compiled file
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ/
# wait;
# cd ./MP-SPDZ/;

# execution
for data_type in ${data_type_list[*]}; do
    for task in ${task_list[*]}; do  
        # evaluation
        for (( i=0; i<${#n_list[@]}; i++ )); do
            n=${n_list[$i]}
            repeat=${repeats_list[$i]}
            ssh spdz00 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} replicated-ring-party.x ${logFolder} ${logFile}-${task}-${data_type} 0 ${n}" &
            ssh spdz1 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} replicated-ring-party.x ${logFolder} ${logFile}-${task}-${data_type} 1 ${n}" &
            ssh spdz2 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} replicated-ring-party.x ${logFolder} ${logFile}-${task}-${data_type} 2 ${n}" &
            wait;
        done
        wait;
    done
done



# basic_test
# compile
# for list in "${comliped_n_lists[@]}"
#     do
#         for (( i=0; i<${#n_list1[@]}; i++ ))
#             do  
#                 n=${n_list1[$i]}
#                 taskCompile=${clogFile}-${n}
#                 ./compile.py -R 128 ${sourceFile} ${n}  > ${taskCompile} &
#             done
#         wait;
#     done;

# for (( i=0; i<${#n_list2[@]}; i++ ))
#     do  
#         n=${n_list2[$i]}
#         taskCompile=${clogFile}-${n}
#         ./compile.py -R 128 ${sourceFile} ${n}  > ${taskCompile} &
#     done
# wait;

# # synchronize the compiled file
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ/
# wait;
# cd ./MP-SPDZ/;

# # evaluation
# for (( i=0; i<${#n_list[@]}; i++ ))
#     do
#         n=${n_list[$i]}
#         repeat=${repeats_list[$i]}
#         ./Eval/basic/dis_exec.sh ${sourceFile}-${n} replicated-ring-party.x ${logFolder} ${clogFile}-${n} 0 ${n} &
#         ssh spdz1 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-${n} replicated-ring-party.x ${logFolder} ${logFile}-${n} 1 ${n}" &
#         ssh spdz2 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-${n} replicated-ring-party.x ${logFolder} ${logFile}-${n} 2 ${n}" &
#         wait;
#     done
#     wait;
# done
# wait;