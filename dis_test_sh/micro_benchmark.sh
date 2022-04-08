sourceFile=non_linear_funcs
benchmarkFile=benchmark_nonlinear


# func_array=(sigmoid tanh soft_plus elu selu gelu soft_sign isru snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis);

# func_array1=(sigmoid tanh soft_plus elu selu gelu soft_sign)
# func_array2=(isru snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis)

func_array=(chi_square);


## Exp - 1
# sprotocol=repring
# protocol=./replicated-ring-party.x
# logFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/efficiency/
# blogFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/benchmark/

# if [ ! -d ${logFolder} ]; then
#     mkdir ${logFolder};
# fi

# if [ ! -d ${blogFolder} ]; then
#     mkdir ${blogFolder};
# fi

# rm -r ${logFolder}*;
# rm -r ${blogFolder}*;

# cd ./MP-SPDZ/
# for func in ${func_array1[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py -R 256 ${sourceFile} ${func} ring ${sprotocol} > ${logFile} &
#         ./compile.py -R 256 ${benchmarkFile} ${func} ring > ${blogFile} &
#     done
#     wait;

# for func in ${func_array2[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py -R 256 ${sourceFile} ${func} ring ${sprotocol} > ${logFile} &
#         ./compile.py -R 256 ${benchmarkFile} ${func} ring > ${blogFile} &
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
#         # execution our methods.
#         # party-0
#         cd ./MP-SPDZ
#         ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}-ring-${sprotocol} ${logFolder} ${sprotocol} & 
#         # party-1
#         ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
#         # party-2
#         ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
#         cd ..
#         wait;

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


## Exp-2
# # replicated prime protocol
# sprotocol=repprime
# protocol=./replicated-field-party.x
# logFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/efficiency/
# blogFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/benchmark/

# if [ ! -d ${logFolder} ]; then
#     mkdir ${logFolder};
# fi

# if [ ! -d ${blogFolder} ]; then
#     mkdir ${blogFolder};
# fi

# rm -r ${logFolder}*;
# rm -r ${blogFolder}*;


# cd ./MP-SPDZ/
# for func in ${func_array1[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py ${sourceFile} ${func} field ${sprotocol} > ${logFile} &
#         ./compile.py ${benchmarkFile} ${func} field > ${blogFile} &
#     done
#     wait;

# for func in ${func_array2[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py ${sourceFile} ${func} field ${sprotocol} > ${logFile} &
#         ./compile.py ${benchmarkFile} ${func} field > ${blogFile} &
#     done
#     wait;
# cd ..

# # synchronize
# scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
# scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
# wait;

# for func in ${func_array[*]}
#     do
#         # execution our methods.
#         # party-0
#         cd ./MP-SPDZ
#         ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}-field-${sprotocol} ${logFolder} ${sprotocol} & 
#         # party-1
#         ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}-field-${sprotocol} ${logFolder} ${sprotocol}" &
#         # party-2
#         ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}-field-${sprotocol} ${logFolder} ${sprotocol}" &
#         cd ..
#         wait;

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
#     wait;


# ps rep prime protocol
sprotocol=psrepprime
protocol=./ps-rep-field-party.x
logFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/efficiency/
blogFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/benchmark/

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

if [ ! -d ${blogFolder} ]; then
    mkdir ${blogFolder};
fi

rm -r ${logFolder}*;
rm -r ${blogFolder}*;

cd ./MP-SPDZ/
for func in ${func_array[*]}
    do
        logFile=${logFolder}compile_${func};
        blogFile=${blogFolder}compile_${func};
        # compile
        ./compile.py ${sourceFile} ${func} others ${sprotocol} > ${logFile} &
        ./compile.py ${benchmarkFile} ${func} others > ${blogFile} &
    done
    wait;

# for func in ${func_array2[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py ${sourceFile} ${func} others ${sprotocol} > ${logFile} &
#         ./compile.py ${benchmarkFile} ${func} others > ${blogFile} &
#     done
#     wait;
# cd ..

# synchronize
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;

for func in ${func_array[*]}
    do
        # execution our methods.
        # party-0
        cd ./MP-SPDZ
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}-others-${sprotocol} ${logFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}-others-${sprotocol} ${logFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}-others-${sprotocol} ${logFolder} ${sprotocol}" &
        cd ..
        wait;

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


# # ps rep ring protocol
# sprotocol=psrepring
# protocol=./ps-rep-ring-party.x
# logFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/efficiency/
# blogFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/benchmark/

# if [ ! -d ${logFolder} ]; then
#     mkdir ${logFolder};
# fi

# if [ ! -d ${blogFolder} ]; then
#     mkdir ${blogFolder};
# fi

# rm -r ${logFolder}*;
# rm -r ${blogFolder}*;

# cd ./MP-SPDZ/
# for func in ${func_array1[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py -R 256 ${sourceFile} ${func} others ${sprotocol} > ${logFile} &
#         ./compile.py -R 256 ${benchmarkFile} ${func} others > ${blogFile} &
#     done
#     wait;

# for func in ${func_array2[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py -R 256 ${sourceFile} ${func} others ${sprotocol} > ${logFile} &
#         ./compile.py -R 256 ${benchmarkFile} ${func} others > ${blogFile} &
#     done
#     wait;
# cd ..

# # synchronize
# scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
# scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
# wait;

# for func in ${func_array[*]}
#     do
#         # execution our methods.
#         # party-0
#         cd ./MP-SPDZ
#         ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}-others-${sprotocol} ${logFolder} ${sprotocol} & 
#         # party-1
#         ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}-others-${sprotocol} ${logFolder} ${sprotocol}" &
#         # party-2
#         ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}-others-${sprotocol} ${logFolder} ${sprotocol}" &
#         cd ..
#         wait;

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
#     wait;


# # shamir protocol
# sprotocol=shamir
# protocol=./shamir-party.x
# logFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/efficiency/
# blogFolder=~/MP-SPDZ/Record/MicroBenchmark/${sprotocol}/benchmark/

# if [ ! -d ${logFolder} ]; then
#     mkdir ${logFolder};
# fi

# if [ ! -d ${blogFolder} ]; then
#     mkdir ${blogFolder};
# fi

# rm -r ${logFolder}*;
# rm -r ${blogFolder}*;

# cd ./MP-SPDZ/
# for func in ${func_array1[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py ${sourceFile} ${func} field ${sprotocol} > ${logFile} &
#         ./compile.py ${benchmarkFile} ${func} field > ${blogFile} &
#     done
#     wait;

# for func in ${func_array2[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};
#         # compile
#         ./compile.py ${sourceFile} ${func} field ${sprotocol} > ${logFile} &
#         ./compile.py ${benchmarkFile} ${func} field > ${blogFile} &
#     done
#     wait;
# cd ..

# # synchronize
# scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
# scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
# wait;

# for func in ${func_array[*]}
#     do
#         # execution our methods.
#         # party-0
#         cd ./MP-SPDZ
#         ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}-field-${sprotocol} ${logFolder} ${sprotocol} & 
#         # party-1
#         ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}-field-${sprotocol} ${logFolder} ${sprotocol}" &
#         # party-2
#         ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-${func}-field-${sprotocol} ${logFolder} ${sprotocol}" &
#         cd ..
#         wait;

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
#     wait;