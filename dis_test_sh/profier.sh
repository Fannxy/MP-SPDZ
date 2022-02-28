logFolder=./Record/dis_profiler/
compileLog=${logFolder}compile_log
logTmp=${logFolder}tmp
logEx=${logFolder}exe_log
sourceFile=non_linear_profiler

protocol=./ps-rep-ring-party.x
echo -e "Test protocol - ${protocol}\n" >> ${logEx};
kArray=($(seq 3 2 20));
mArray=($(seq 2 15 100));
m1Array=($(seq 2 15 63));
m2Array=($(seq 77 15 100));

# for k in ${kArray[@]}
#     do 
#         for m in ${m1Array[@]}
#             do 
#                 cd ./MP-SPDZ/
#                 ./compile.py -R 256 ${sourceFile} 0 $k $m 0 >> ${compileLog} &
#                 cd ..
#                 compile_command="cd ./MP-SPDZ/; ./compile.py -R 256 ${sourceFile} 0 $k $m 0;"
#                 ssh mp-spdz131 ${compile_command} & 
#                 ssh mp-spdz132 ${compile_command} &
#             done
#         wait;
#         for m in ${m2Array[@]}
#             do 
#                 cd ./MP-SPDZ/
#                 ./compile.py -R 256 ${sourceFile} 0 $k $m 0 >> ${compileLog} &
#                 cd ..
#                 compile_command="cd ./MP-SPDZ/; ./compile.py -R 256 ${sourceFile} 0 $k $m 0;"
#                 ssh mp-spdz131 ${compile_command} & 
#                 ssh mp-spdz132 ${compile_command} &
#             done
#         wait;
#     done


# for k in ${kArray[@]}
#     do 
#         for m in ${mArray[@]}
#             do 
#                 echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFile}; 
#                 # party-0
#                 cd ./MP-SPDZ 
#                 ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} & 
#                 # party-1
#                 ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} " &
#                 # party-2
#                 ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} " &
#                 cd ..
#                 wait;
#                 echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logFile};
#             done
#     done
#     wait;



protocol=./replicated-field-party.x
echo -e "Test protocol - ${protocol}\n" >> ${logEx};

# compile in single machine.
for k in ${kArray[@]}
    do 
        for m in ${m1Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m2Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
    done

# synchronize
scp -p 3333 -r ./MP-SPDZ/Programs/ mp-spdz131:~/MP-SPDZ/ & 
scp -p 3333 -r ./MP-SPDZ/Programs/ mp-spdz132:~/MP-SPDZ/
wait;


for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFile}; 
                # party-0
                cd ./MP-SPDZ 
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
                cd ..
                wait;
                echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logFile};
            done
    done

# protocol=./shamir-party.x
# echo -e "Test protocol - ${protocol}\n" >> ${logEx};

# for k in ${kArray[@]}
#     do 
#         for m in ${mArray[@]}
#             do 
#                 echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFile}; 
#                 # party-0
#                 cd ./MP-SPDZ 
#                 ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} & 
#                 # party-1
#                 ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
#                 # party-2
#                 ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
#                 cd ..
#                 wait;
#                 echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logFile};
#             done
#     done
