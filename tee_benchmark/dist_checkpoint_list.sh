func_list=(nn)
passive_list=(semi2k semi repring repfield)

cd $HOME/MP-SPDZ

for func in ${func_list[*]}; do
    for prot in ${passive_list[*]}; do
        echo "run semi-honest protocol with TEE: $prot $func, adjust the checkpoint period"
        ./tee_benchmark/dist_checkpoint_unit.sh ${prot} ${func} 6   # semi with TEE
    done;
done;
