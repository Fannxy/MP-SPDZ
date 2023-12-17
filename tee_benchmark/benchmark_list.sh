prot_list=(repring repfield psrepring psrepfield semi2k semi spdz mascot)
# prot_list=(mascot)
func_list=(lr)

for func in ${func_list[*]}; do
    for prot in ${prot_list[*]}; do
        ./tee_benchmark/benchmark_unit.sh ${prot} ${func};
    done;
done;