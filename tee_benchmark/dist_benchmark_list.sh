func_list=(comp oppe oram lr nn)
passive_list=(semi2k semi repring repfield)

cd $HOME/MP-SPDZ
for func in ${func_list[*]}; do
    for prot in ${passive_list[*]}; do
        echo "run semi-honest protocol without TEE: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 1   # semi without TEE
    done;
done;

for func in ${func_list[*]}; do
    for prot in ${passive_list[*]}; do
        echo "run semi-honest protocol with TEE: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 2   # semi with TEE
    done;
done;

active_list=(spdz2k mascot psrepring psrepfield)
for func in ${func_list[*]}; do
    for prot in ${active_list[*]}; do
        echo "run malicious protocol without TEE: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 3   # malicious without TEE
    done;
done;

offline_list=(semi-offline semi2k-offline hemi-offline)
for func in ${func_list[*]}; do
    for prot in ${offline_list[*]}; do
        echo "run offline protocol without optimization: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 4  # offline TEE, without optimization
    done;
done;

#for func in ${func_list[*]}; do
#    for prot in ${offline_list[*]}; do
#        echo $prot $func
#        ./tee_benchmark/benchmark_unit.sh ${prot} ${func} 5  # offline TEE, with optimization
#    done;
#done;
