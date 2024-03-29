task_list=("sort")

for task in ${task_list[@]}; do
    ./Eval/tgl_benchmark_unit.sh ${task}
done