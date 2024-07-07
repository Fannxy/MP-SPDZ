func_list=(comp oppe oram lr nn)
passive_list=(semi2k semi repring repfield shamir hemi soho)

cd $HOME/MP-SPDZ
for n in 3; do
for func in ${func_list[*]}; do
    for prot in ${passive_list[*]}; do
        echo "run semi-honest protocol without TEE: $prot $func"
	./tee_benchmark/clean_port.sh
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 1 ${n} # semi without TEE
	./tee_benchmark/clean_port.sh
    done;
done;
done

active_list=(spdz2k mascot psrepring psrepfield malicious-shamir lowgear highgear)

for n in 3; do
for func in ${func_list[*]}; do
    for prot in ${active_list[*]}; do
        ./tee_benchmark/clean_port.sh
	echo "run malicious protocol without TEE: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 3 ${n} # malicious without TEE
	./tee_benchmark/clean_port.sh
    done;
done;
done;

for n in 3; do
for func in ${func_list[*]}; do
    for prot in ${passive_list[*]}; do
        ./tee_benchmark/clean_port.sh
	echo "run semi-honest protocol with TEE: $prot $func"
        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 2 ${n} # semi with TEE, without optmization
        ./tee_benchmark/clean_port.sh    
    done;
done;
done

#for n in 2; do
#for func in ${func_list[*]}; do
#    for prot in ${passive_list[*]}; do
#        ./tee_benchmark/clean_port.sh
#        echo "run semi-honest protocol with TEE: $prot $func"
#        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 0 ${n}   # semi with TEE, with optimization
#        ./tee_benchmark/clean_port.sh
#    done;
#done;
#done

offline_list=(semi2k-offline semi-offline hemi-offline)
#for n in 2; do
#for func in ${func_list[*]}; do
#    for prot in ${offline_list[*]}; do
#	./tee_benchmark/clean_port.sh
#        echo "run offline protocol without optimization: $prot $func"
#        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 4 ${n} # offline TEE, without optimization
#        ./tee_benchmark/clean_port.sh
#    done;
#done;
#done

#for n in 2; do
#for func in ${func_list[*]}; do
#    for prot in ${offline_list[*]}; do
#        echo $prot $func
#	./tee_benchmark/clean_port.sh
#        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 5 ${n} # offline TEE, with optimization
#	./tee_benchmark/clean_port.sh
#    done;
#done;
#done

#for n in 2; do
#for func in ${func_list[*]}; do
#    for prot in ${offline_list[*]}; do
#	./tee_benchmark/clean_port.sh
#        echo "run offline protocol without optimization: $prot $func"
#        ./tee_benchmark/dist_benchmark_unit.sh ${prot} ${func} 7 ${n} # offline, without optimization and TEE
#	./tee_benchmark/clean_port.sh
#    done;
#done;
#done
