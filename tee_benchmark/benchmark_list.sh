
./tee_benchmark/compile_list.sh

# prot_list=(repring repfield psrepring psrepfield semi2k semi spdz mascot)
# prot_list=(semi2k semi spdz mascot)
prot_list=(spdz)
# prot_list=(spdz mascot)
# prot_list=(mascot)
# func_list=(comp oppe oram lr)
func_list=(comp)
rm -r ./tee_benchmark/Record/*

for func in ${func_list[*]}; do
    for prot in ${prot_list[*]}; do
        ./tee_benchmark/benchmark_unit.sh ${prot} ${func}
    done;
done;
