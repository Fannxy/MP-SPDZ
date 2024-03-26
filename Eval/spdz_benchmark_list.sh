task_list=("max" "average" "metric" "cipher_index")

for task in ${task_list[@]}; do
    ./Eval/spdz_benchmark_unit.sh ${task}
done