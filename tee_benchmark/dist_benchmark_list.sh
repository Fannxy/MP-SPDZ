func_list=(comp oppe oram lr nn)
passive_list=(semi2k semi repring repfield)

cd $HOME/MP-SPDZ
for func in ${func_list[*]}; do
    for prot in ${passive_list[*]}; do
        echo "run semi-honest protocol without TEE: $prot $func"
	./tee_benchmark/clean_port.sh
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 1   # semi without TEE
	./tee_benchmark/clean_port.sh
    done;
done;

active_list=(spdz2k mascot psrepring psrepfield)
for func in ${func_list[*]}; do
    for prot in ${active_list[*]}; do
        echo "run malicious protocol without TEE: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 3   # malicious without TEE
	./tee_benchmark/clean_port.sh
    done;
done;

for func in ${func_list[*]}; do
    for prot in ${passive_list[*]}; do
        ./tee_benchmark/clean_port.sh
	echo "run semi-honest protocol with TEE: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 2   # semi with TEE
        ./tee_benchmark/clean_port.sh    
    done;
done;

offline_list=(semi2k-offline semi-offline hemi-offline)
for func in ${func_list[*]}; do
    for prot in ${offline_list[*]}; do
	./tee_benchmark/clean_port.sh
        echo "run offline protocol without optimization: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 4  # offline TEE, without optimization
        ./tee_benchmark/clean_port.sh
    done;
done;

for func in ${func_list[*]}; do
    for prot in ${offline_list[*]}; do
        echo $prot $func
	./tee_benchmark/clean_port.sh
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 5  # offline TEE, with optimization
	./tee_benchmark/clean_port.sh
    done;
done;

for func in ${func_list[*]}; do
    for prot in ${offline_list[*]}; do
	./tee_benchmark/clean_port.sh
        echo "run offline protocol without optimization: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 7  # offline, without optimization and TEE
	./tee_benchmark/clean_port.sh
    done;
done;
