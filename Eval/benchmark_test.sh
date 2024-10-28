prot=replicated-ring-party.x
func=aes_circuit
comptype=r
IFS=',' read -r -a keywords < target_keyword.txt

compile_pass_file=./compile_pass.txt

for func in "${keywords[@]}" 
do
    ./Eval/compile.sh $prot $func $comptype
    if [ $? -eq 0 ]; then
        echo $func >> $compile_pass_file
    fi
done

# sync with other machines.
