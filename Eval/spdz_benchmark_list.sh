#!/bin/bash
BuildFlag=$1
CompileOnly=$2

task_list=("max" "average" "metric" "cipher_index" "sort")

for task in ${task_list[@]}; do
    ./Eval/spdz_benchmark_unit.sh ${task} ${BuildFlag} ${CompileOnly}
done