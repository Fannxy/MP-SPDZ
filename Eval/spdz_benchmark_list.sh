# task_list=("max" "average" "metric" "cipher_index")
task_list=("average" "cipher_index" "metric" "max")

for task in ${task_list[@]}; do
    ./Eval/spdz_benchmark_unit.sh ${task}
done