logFolder=./Record/Vector/
clogFile=${logFolder}compile_log
logFile=${logFolder}vector_log
sourceFile=bb_profiler

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
else
    rm -r ${logFolder}*
fi


# compile
task_list=(gt eq mul add)

# insert config info
n_list=(10 13 17 23 30 40 54 71 95 126 167 222 294 390 517 686 910 1206 1599 2120 2811 3727 4941 6551 8685 11513 15264 20235 26826 35564 47148 62505 82864 109854 145634 193069 255954 339322 449843 596362 790604 1048113 1389495 1842069 2442053 3237457 4291934 5689866 7543120 10000000)
n_list1=(10 13 17 23 30 40 54 71 95 126 167 222 294 390 517 686 910 1206 1599 2120 2811 3727 4941 6551 8685 11513 15264 20235 26826 35564 47148 62505 82864 109854)
n_list2=(145634 193069 255954 339322 449843 596362 790604 1048113 1389495 1842069 2442053)
n_list3=(3237457 4291934 5689866)
n_list4=(7543120 10000000)
repeats_list=(100 77 59 44 34 25 19 15 11 8 6 5 4 3 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1)
data_type_list=(sfix sint)
# data_type_list=(sint)

for data_type in ${data_type_list[*]}
    do
        for task in ${task_list[*]}
            do  
                # compile
                for (( i=0; i<${#n_list1[@]}; i++ ))
                    do  
                        n=${n_list1[$i]}
                        repeat=${repeats_list[$i]}
                        taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
                        ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
                    done
                wait;
                for (( i=0; i<${#n_list2[@]}; i++ ))
                    do  
                        n=${n_list2[$i]}
                        repeat=1
                        taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
                        ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
                    done
                wait;
                for (( i=0; i<${#n_list3[@]}; i++ ))
                    do  
                        n=${n_list3[$i]}
                        repeat=1
                        taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
                        ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
                    done
                wait;
                for (( i=0; i<${#n_list4[@]}; i++ ))
                    do  
                        n=${n_list4[$i]}
                        repeat=1
                        taskCompile=${clogFile}-${task}-${n}-${repeat}-${data_type}
                        ./compile.py -R 128 ${sourceFile} ring ${task} ${n} ${repeat} ${data_type} > ${taskCompile} &
                    done
                wait;
                
                # evaluation
                for (( i=0; i<${#n_list[@]}; i++ ))
                    do
                        n=${n_list[$i]}
                        repeat=${repeats_list[$i]}
                        sh ./Eval/basic/basic.sh ${sourceFile}-ring-${task}-${n}-${repeat}-${data_type} replicated-ring-party.x ${logFolder} ${logFile}-${task}-${data_type};
                        wait;
                    done
                    wait;
            done
            wait;
        wait;
    done
wait