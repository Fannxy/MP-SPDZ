# synchronized with other machines once.
# cd ..
# scp -r ./MP-SPDZ/Programs spdz1:~/MP-SPDZ/ &
# scp -r ./MP-SPDZ/Programs spdz2:~/MP-SPDZ
# wait;
# cd ./MP-SPDZ/;

# ./Eval/control/setup_ssl.sh;
# wait;

# execute the commands.
task_list=("max" "average" "metric" "cipher_index" "sort")

for task in ${task_list[@]}; do
    ./Eval/spdz_benchmark_unit.sh ${task}
done