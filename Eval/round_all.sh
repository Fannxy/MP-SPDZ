nth_list=(0 1 2 3 4 5)
# for nth in "${nth_list[@]}"; do
#     ./Eval/round_test.sh $nth;
#     wait;
# done

# for nth in "${nth_list[@]}"; do
#     ./Eval/round_baseline.sh $nth;
#     wait;
# done

# secure
for nth in "${nth_list[@]}"; do
    ./Eval/round_secure_test.sh $nth;
    wait;
done

# # nfgen
# for nth in "${nth_list[@]}"; do
#     ./Eval/round_nfgen.sh $nth;
#     wait;
# done