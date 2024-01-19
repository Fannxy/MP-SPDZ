
./tee_benchmark/compile_list.sh

prot_list=(repring repfield psrepring psrepfield semi2k semi spdz mascot)
# prot_list=(repring)
func_list=(oppe)
# func_list=(lr oppe oram)

rm -r ./tee_benchmark/Record/*

for func in ${func_list[*]}; do
    for prot in ${prot_list[*]}; do
        ./tee_benchmark/benchmark_unit.sh ${prot} ${func} &> ./tee_benchmark/Record/${prot}-${func}.txt
    done;
done;
