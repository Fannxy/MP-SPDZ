sourceFile=candidate_test
benchmarkFile=benchmark_nonlinear
func_array=(sigmoid soft_plus selu isru bs_dis)
candidate_list=($(seq 0 1 6))

# # Exp - 1
# sprotocol=repring
# protocol=./replicated-ring-party.x
# logFolder=~/MP-SPDZ/Record/CandidateBenchmark/${sprotocol}/

# if [ ! -d ${logFolder} ]; then
#     mkdir ${logFolder};
# fi
# rm -r ${logFolder}*;

# cd ./MP-SPDZ/
# for func in ${func_array[*]}
#     do
#         for i in ${candidate_list[*]}
#             do  
#                 echo ${i}
#                 logFile=${logFolder}compile_${func}_${i};
#                 # compile
#                 ./compile.py -R 256 ${sourceFile} ${func}_${i} ring ${sprotocol} > ${logFile} &
#             done
#         blogFile=${logFolder}compile_${func}_seq;
#         ./compile.py -R 256 ${benchmarkFile} ${func} ring > ${blogFile} &
#         wait;
#     done
#     wait;
# cd ..
# wait;

# # synchronize
# scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
# scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
# wait;

# for func in ${func_array[*]}
#     do
#         for i in ${candidate_list[*]}
#             do
#                 # party-0
#                 cd ./MP-SPDZ
#                 ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}_${i}-ring-${sprotocol} ${logFolder} ${sprotocol} & 
#                 # party-1
#                 ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}_${i}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
#                 # party-2
#                 ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}_${i}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
#                 cd ..
#                 wait;
#             done

#         # execution benchmark
#         cd ./MP-SPDZ/
#         ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${benchmarkFile}-${func}-ring ${blogFolder} ${sprotocol} & 
#         # party-1
#         ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${benchmarkFile}-${func}-ring ${blogFolder} ${sprotocol}" &
#         # party-2
#         ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${benchmarkFile}-${func}-ring ${blogFolder} ${sprotocol}" &
#         cd ..
#         wait;
#     done
# wait;


# # Exp-2
# # replicated prime protocol
# sprotocol=repprime
# protocol=./replicated-field-party.x
# logFolder=~/MP-SPDZ/Record/CandidateBenchmark/${sprotocol}/

# if [ ! -d ${logFolder} ]; then
#     mkdir ${logFolder};
# fi

# rm -r ${logFolder}*;


# cd ./MP-SPDZ/
# for func in ${func_array[*]}
#     do
#         for i in ${candidate_list[*]}
#             do  
#                 echo ${i}
#                 logFile=${logFolder}compile_${func}_${i};
#                 # compile
#                 ./compile.py ${sourceFile} ${func}_${i} field ${sprotocol} > ${logFile} &
#             done
#         blogFile=${logFolder}compile_${func}_seq;
#         ./compile.py ${benchmarkFile} ${func} field > ${blogFile} &
#         wait;
#     done
#     wait;
# cd ..
# wait;

# # synchronize
# scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
# scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
# wait;

# for func in ${func_array[*]}
#     do
#         for i in ${candidate_list[*]}
#             do
#                 # party-0
#                 cd ./MP-SPDZ
#                 ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}_${i}-field-${sprotocol} ${logFolder} ${sprotocol} & 
#                 # party-1
#                 ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}_${i}-field-${sprotocol} ${logFolder} ${sprotocol}" &
#                 # party-2
#                 ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}_${i}-field-${sprotocol} ${logFolder} ${sprotocol}" &
#                 cd ..
#                 wait;
#             done

#         # execution benchmark
#         cd ./MP-SPDZ/
#         ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${benchmarkFile}-${func}-field ${blogFolder} ${sprotocol} & 
#         # party-1
#         ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${benchmarkFile}-${func}-field ${blogFolder} ${sprotocol}" &
#         # party-2
#         ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${benchmarkFile}-${func}-field ${blogFolder} ${sprotocol}" &
#         cd ..
#         wait;
#     done
# wait;


# # Exp-3
# # ps replicated prime protocol
# sprotocol=psrepprime
# protocol=./ps-rep-field-party.x
# logFolder=~/MP-SPDZ/Record/CandidateBenchmark/${sprotocol}/

# if [ ! -d ${logFolder} ]; then
#     mkdir ${logFolder};
# fi

# rm -r ${logFolder}*;


# cd ./MP-SPDZ/
# for func in ${func_array[*]}
#     do
#         for i in ${candidate_list[*]}
#             do  
#                 echo ${i}
#                 logFile=${logFolder}compile_${func}_${i};
#                 # compile
#                 ./compile.py ${sourceFile} ${func}_${i} others ${sprotocol} > ${logFile} &
#             done
#         blogFile=${logFolder}compile_${func}_seq;
#         ./compile.py ${benchmarkFile} ${func} others > ${blogFile} &
#         wait;
#     done
#     wait;
# cd ..
# wait;

# # synchronize
# scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
# scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
# wait;

# for func in ${func_array[*]}
#     do
#         for i in ${candidate_list[*]}
#             do
#                 # party-0
#                 cd ./MP-SPDZ
#                 ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}_${i}-others-${sprotocol} ${logFolder} ${sprotocol} & 
#                 # party-1
#                 ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}_${i}-others-${sprotocol} ${logFolder} ${sprotocol}" &
#                 # party-2
#                 ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}_${i}-others-${sprotocol} ${logFolder} ${sprotocol}" &
#                 cd ..
#                 wait;
#             done

#         # execution benchmark
#         cd ./MP-SPDZ/
#         ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${benchmarkFile}-${func}-others ${blogFolder} ${sprotocol} & 
#         # party-1
#         ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${benchmarkFile}-${func}-others ${blogFolder} ${sprotocol}" &
#         # party-2
#         ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${benchmarkFile}-${func}-others ${blogFolder} ${sprotocol}" &
#         cd ..
#         wait;
#     done
# wait;



# Exp-4
# ps replicated ring protocol
sprotocol=psrepring
protocol=./ps-rep-ring-party.x
logFolder=~/MP-SPDZ/Record/CandidateBenchmark/${sprotocol}/

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

rm -r ${logFolder}*;


cd ./MP-SPDZ/
for func in ${func_array[*]}
    do
        for i in ${candidate_list[*]}
            do  
                echo ${i}
                logFile=${logFolder}compile_${func}_${i};
                # compile
                ./compile.py -R 256 ${sourceFile} ${func}_${i} others ${sprotocol} > ${logFile} &
            done
        blogFile=${logFolder}compile_${func}_seq;
        ./compile.py -R 256 ${benchmarkFile} ${func} others > ${blogFile} &
        wait;
    done
    wait;
cd ..
wait;

# synchronize
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;

for func in ${func_array[*]}
    do
        for i in ${candidate_list[*]}
            do
                # party-0
                cd ./MP-SPDZ
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}_${i}-others-${sprotocol} ${logFolder} ${sprotocol} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}_${i}-others-${sprotocol} ${logFolder} ${sprotocol}" &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}_${i}-others-${sprotocol} ${logFolder} ${sprotocol}" &
                cd ..
                wait;
            done

        # execution benchmark
        cd ./MP-SPDZ/
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${benchmarkFile}-${func}-others ${blogFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${benchmarkFile}-${func}-others ${blogFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${benchmarkFile}-${func}-others ${blogFolder} ${sprotocol}" &
        cd ..
        wait;
    done
wait;


# Exp-5
# shamir protocol
sprotocol=shamir
protocol=./shamir-party.x
logFolder=~/MP-SPDZ/Record/CandidateBenchmark/${sprotocol}/

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

rm -r ${logFolder}*;


cd ./MP-SPDZ/
for func in ${func_array[*]}
    do
        for i in ${candidate_list[*]}
            do  
                echo ${i}
                logFile=${logFolder}compile_${func}_${i};
                # compile
                ./compile.py ${sourceFile} ${func}_${i} field ${sprotocol} > ${logFile} &
            done
        blogFile=${logFolder}compile_${func}_seq;
        ./compile.py ${benchmarkFile} ${func} field > ${blogFile} &
        wait;
    done
    wait;
cd ..
wait;

# synchronize
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;

for func in ${func_array[*]}
    do
        for i in ${candidate_list[*]}
            do
                # party-0
                cd ./MP-SPDZ
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}_${i}-field-${sprotocol} ${logFolder} ${sprotocol} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}_${i}-field-${sprotocol} ${logFolder} ${sprotocol}" &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}_${i}-field-${sprotocol} ${logFolder} ${sprotocol}" &
                cd ..
                wait;
            done

        # execution benchmark
        cd ./MP-SPDZ/
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${benchmarkFile}-${func}-field ${blogFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${benchmarkFile}-${func}-field ${blogFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${benchmarkFile}-${func}-field ${blogFolder} ${sprotocol}" &
        cd ..
        wait;
    done
wait;