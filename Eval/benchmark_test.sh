MAIN_FOLDER=/root/RoundRole/MP-SPDZ/

prot_list_ring=(replicated-ring-party.x ps-rep-ring-party.x semi2k-party.x spdz2k-party.x) 
prot_list_field=(replicated-field-party.x ps-rep-field-party.x semi-party.x mascot-party.x shamir-party.x atlas-party.x)

declare -A modular
modular["replicated-ring-party.x"]=r;
modular["ps-rep-ring-party.x"]=r; modular["semi2k-party.x"]=r; modular["spdz2k-party.x"]=r;

modular["replicated-field-party.x"]=f; 
modular["ps-rep-field-party.x"]=f; modular["semi-party.x"]=f; 
modular["mascot-party.x"]=f; modular["shamir-party.x"]=f; modular["atlas-party.x"]=f;

declare -A parties
parties["replicated-ring-party.x"]=3; parties["ps-rep-ring-party.x"]=3;
parties["semi2k-party.x"]=2; parties["spdz2k-party.x"]=2;
parties["replicated-field-party.x"]=3; parties["ps-rep-field-party.x"]=3;
parties["semi-party.x"]=2; parties["mascot-party.x"]=2;
parties["shamir-party.x"]=3; parties["atlas-party.x"]=3;

mapfile -t target_list < ./basic_functions.txt

echo "target_list: ${target_list[@]}"

# function compile
compile_func() {
    local func=$1
    local prot=$2
    local comptype=$3
    local temp_dir=$4

    if [ -f ${MAIN_FOLDER}Programs/Schedules/${func}-${comptype}.sch ]; then
        return
    fi

    ./Eval/compile.sh "$prot" "$func" "$comptype"
    if [ $? -eq 0 ]; then
        echo "$func" >> "$temp_dir/compile_pass-${comptype}_$$.txt"
    else
        echo "$func" >> "$temp_dir/compile_fail-${comptype}_$$.txt"
        echo "Error details:" >> "$temp_dir/compile_fail_$$.txt"
        ./Eval/compile.sh "$prot" "$func" "$comptype" 2>> "$temp_dir/compile_fail-${comptype}_$$.txt"
    fi
}

temp_dir=$(mktemp -d)

export -f compile_func
parallel -j 8 compile_func ::: "${target_list[@]}" ::: "hold" ::: "r" ::: "$temp_dir"

cat "$temp_dir"/compile_pass-r_*.txt > $MAIN_FOLDER/compile_pass-r.txt
cat "$temp_dir"/compile_fail-r_*.txt > $MAIN_FOLDER/compile_fail-r.txt


# export -f compile_func
parallel -j 8 compile_func ::: "${target_list[@]}" ::: "$prot" ::: "f" ::: "$temp_dir"

cat "$temp_dir"/compile_pass-f_*.txt > $MAIN_FOLDER/compile_pass-f.txt
cat "$temp_dir"/compile_fail-f_*.txt > $MAIN_FOLDER/compile_fail-f.txt


# # let other machines compile the project.
# ssh aby31 "cd ${MAIN_FOLDER}; make rep-ring;" &
# ssh aby32 "cd ${MAIN_FOLDER}; make rep-ring;" &

# # sync with other machines.
# scp -r ${MAIN_FOLDER}Programs aby31:${MAIN_FOLDER} &
# scp -r ${MAIN_FOLDER}Programs aby32:${MAIN_FOLDER} &
# wait;

# evaluate the project.
for prot in "${prot_list_ring[@]}"
do
    parties=${parties[$prot]}
    for func in "${target_list[@]}"
    do
        echo "executing $func-r"
        ./Eval/dis_exec.sh $prot $func-r $parties
    done
    wait;
    python3 ./Eval/comm_log_analysis.py --protocol ${prot}
done

for prot in "${prot_list_field[@]}"
do
    parties=${parties[$prot]}
    for func in "${target_list[@]}"
    do
        echo "executing $func-f"
        ./Eval/dis_exec.sh $prot $func-f $parties
    done
    wait;
    python3 ./Eval/comm_log_analysis.py --protocol ${prot}
done