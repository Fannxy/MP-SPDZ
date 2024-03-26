# # synchronized with other machines once.
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
# wait;
# cd ./MP-SPDZ/;

# ./Eval/control/setup_ssl.sh;
# wait;

# execute the commands.
task_list=("average" "cipher_index" "metric" "max")

for task in ${task_list[@]}; do
    ./Eval/spdz_benchmark_unit.sh ${task}
done