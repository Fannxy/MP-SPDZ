sourceFile=candidate_test
benchmarkFile=benchmark_nonlinear
# func_array=(sigmoid tanh elu soft_sign isru)
func_array=(sigmoid tanh elu)
candidate_list=($(seq 0 1 4))

# Exp - 1
sprotocol=repring
protocol=./replicated-ring-party.x
logFolder=~/MP-SPDZ/Record/CandidateBenchmark/${sprotocol}/

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi
rm -r ${logFolder}*;

# cd ./MP-SPDZ/
# for func in ${func_array[*]}
#     do
#         for i in ${candidate_list[*]}
#             do  
#                 echo ${i}
#                 logFile=${logFolder}compile_${func}${i};
#                 # compile
#                 ./compile.py -R 256 ${sourceFile} ${func}${i} ring ${sprotocol} > ${logFile} &
#             done
#         blogFile=${logFolder}compile_${func}_seq;
#         ./compile.py -R 256 ${benchmarkFile} ${func} ring > ${blogFile} &
#         wait;
#     done
#     wait;
# cd ..
# wait;

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
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}${i}-ring-${sprotocol} ${logFolder} ${sprotocol} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}${i}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}${i}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
                cd ..
                wait;
            done

        # execution benchmark
        cd ./MP-SPDZ/
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${benchmarkFile}-${func}-ring ${blogFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${benchmarkFile}-${func}-ring ${blogFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${benchmarkFile}-${func}-ring ${blogFolder} ${sprotocol}" &
        cd ..
        wait;
    done
wait;