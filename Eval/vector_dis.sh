logFolder=./Record/Vector/
clogFile=${logFolder}compile_log
logFile=${logFolder}vector_log
# sourceFile=bb_profiler
sourceFile=basic_profiler

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
else
    rm -r ${logFolder}*
fi

# compile
# task_list=(gt eq mul add)
# task_list=(eq mul)
task_list=(gt)

# insert config info
n_list=(10 13 17 23 30 40 54 71 95 126 167 222 294 390 517 686 910 1206 1599 2120 2811 3727 4941 6551 8685 11513 15264 20235 26826 35564 47148 62505 82864 109854 145634 193069 255954 339322 449843 596362 790604 1048113 1389495 1842069 2442053)
n_list1=(10 13 17 23 30 40 54 71 95 126 167 222 294 390 517 686 910 1206 1599 2120 2811 3727 4941 6551 8685 11513 15264 20235 26826 35564 47148 62505 82864 109854)
n_list2=(145634 193069 255954 339322 449843 596362 790604 1048113 1389495 1842069 2442053)
# n_list3=(3237457)
# n_list3=(3237457 4291934 5689866)
# n_list4=(7543120 10000000)
repeats_list=(1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1)
data_type_list=(sint)
# data_type_list=(sint)

# basic_test
# compile
for (( i=0; i<${#n_list1[@]}; i++ ))
    do  
        n=${n_list1[$i]}
        taskCompile=${clogFile}-${n}
        ./compile.py -R 128 ${sourceFile} ${n}  > ${taskCompile} &
    done
wait;

for (( i=0; i<${#n_list2[@]}; i++ ))
    do  
        n=${n_list2[$i]}
        taskCompile=${clogFile}-${n}
        ./compile.py -R 128 ${sourceFile} ${n}  > ${taskCompile} &
    done
wait;

# synchronize the compiled file
cd ..
scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ/
wait;
cd ./MP-SPDZ/;

# evaluation
for (( i=0; i<${#n_list[@]}; i++ ))
    do
        n=${n_list[$i]}
        repeat=${repeats_list[$i]}
        ./Eval/basic/dis_exec.sh ${sourceFile}-${n} replicated-ring-party.x ${logFolder} ${clogFile}-${n} 0 ${n} &
        ssh spdz1 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-${n} replicated-ring-party.x ${logFolder} ${logFile}-${n} 1 ${n}" &
        ssh spdz2 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-${n} replicated-ring-party.x ${logFolder} ${logFile}-${n} 2 ${n}" &
        wait;
    done
    wait;
done
wait;

# for data_type in ${data_type_list[*]}
#     do
#         for task in ${task_list[*]}
#             do  
#                 # compile
#                 for (( i=0; i<${#n_list1[@]}; i++ ))
#                     do  
#                         n=${n_list1[$i]}
#                         repeat=${repeats_list[$i]}
#                         taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
#                         ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
#                     done
#                 wait;
#                 for (( i=0; i<${#n_list2[@]}; i++ ))
#                     do  
#                         n=${n_list2[$i]}
#                         repeat=1
#                         taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
#                         ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
#                     done
#                 wait;
#                 # for (( i=0; i<${#n_list3[@]}; i++ ))
#                 #     do  
#                 #         n=${n_list3[$i]}
#                 #         repeat=1
#                 #         taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
#                 #         ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile}
#                 #         wait;
#                 #     done
#                 # wait;
#                 # for (( i=0; i<${#n_list4[@]}; i++ ))
#                 #     do  
#                 #         n=${n_list4[$i]}
#                 #         repeat=1
#                 #         taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
#                 #         ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile}
#                 #         wait;
#                 #     done
#                 # wait;

#                 # synchronize the compiled file
#                 cd ..
#                 scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
#                 scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ/
#                 wait;
#                 cd ./MP-SPDZ/;

#                 # evaluation
#                 for (( i=0; i<${#n_list[@]}; i++ ))
#                     do
#                         n=${n_list[$i]}
#                         repeat=${repeats_list[$i]}
#                         ./Eval/basic/dis_exec.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} replicated-ring-party.x ${logFolder} ${logFile}-${task}-${data_type} 0 ${n} &
#                         ssh spdz1 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} replicated-ring-party.x ${logFolder} ${logFile}-${task}-${data_type} 1 ${n}" &
#                         ssh spdz2 "cd ./MP-SPDZ/; ./Eval/basic/dis_exec.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} replicated-ring-party.x ${logFolder} ${logFile}-${task}-${data_type} 2 ${n}" &
#                         wait;
#                     done
#                     wait;
#             done
#             wait;
#         wait;
#     done
# wait