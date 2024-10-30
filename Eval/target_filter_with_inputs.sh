grep -oP '(?<=./Programs/Source/)[^/]+(?=\.mpc)' ./contains_input_from.txt | paste -sd, - > ./target_keyword2.txt

prot=replicated-ring-party.x
comptype=r
IFS=',' read -r -a keywords < target_keyword2.txt

compile_pass_file=./compile_pass3.txt
compile_fail_file=./compile_fail3.txt

# rm compile_passfile if it exists
if [ -f "$compile_pass_file" ]; then
    rm "$compile_pass_file"
fi

# rm compile_fail_file if it exists
if [ -f "$compile_fail_file" ]; then
    rm "$compile_fail_file"
fi

temp_dir=$(mktemp -d)

# 定义编译函数
compile_func() {
    local func=$1
    local prot=$2
    local comptype=$3
    local temp_dir=$4

    ./Eval/compile.sh "$prot" "$func" "$comptype"
    if [ $? -eq 0 ]; then
        echo "$func" >> "$temp_dir/compile_pass3_$$.txt"
    else
        echo "$func" >> "$temp_dir/compile_fail3_$$.txt"
        echo "Error details:" >> "$temp_dir/compile_fail3_$$.txt"
        ./Eval/compile.sh "$prot" "$func" "$comptype" 2>> "$temp_dir/compile_fail3_$$.txt"
    fi
}

export -f compile_func

# 使用 GNU Parallel 并行执行编译任务
parallel -j 8 compile_func ::: "${keywords[@]}" ::: "$prot" ::: "$comptype" ::: "$temp_dir"

# 合并所有临时文件到最终的 compile_pass_file
cat "$temp_dir"/compile_pass3_*.txt > "$compile_pass_file"
cat "$temp_dir"/compile_fail3_*.txt > "$compile_fail_file"

# 删除临时目录
rm -rf "$temp_dir"

