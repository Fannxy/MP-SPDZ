prot_list=(repring repfield psrepring psrepfield semi2k semi spdz mascot)
# prot_list=(semi2k semi spdz mascot)
# prot_list=(repring)
func_list=(comp)
exec_perf='/usr/lib/linux-tools/4.15.0-20-generic/perf'


for func in ${func_list[*]}; do
    for prot in ${prot_list[*]}; do
        ./tee_benchmark/benchmark_unit.sh ${prot} ${func};
        ${exec_perf} script -i ./Perf/${prot}.data > ./Perf/${prot}_out.perf
    done;
done;