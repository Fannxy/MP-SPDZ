task=$1

logFolder=./Record/benchmark_spdz_tgl/
clogFolder=./Record/tgl_compile/
clogFile=${clogFolder}compile_log
instructFolder=./Record/tgl_instruct/
sourceFile=pta_baseline
protocol=replicated-ring-party.x

BuildFlag=False
CompileOnly=True

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

if [ ! -d ${clogFolder} ]; then
    mkdir ${clogFolder};
fi

if [ ! -d ${instructFolder} ]; then
    mkdir ${instructFolder};
fi

parallel_list=(64 128 256)
N_list=(1 1 1 1)
REPEAT=1

declare -A MLists
MLists["cipher_index"]="1048576 16777216 268435456 1073741824"
MLists["max"]="1048576 16777216 268435456 1073741824"
MLists["average"]="1048576 16777216 268435456 1073741824"
MLists["metric"]="1048576 16777216 268435456 1073741824"
MLists["sort"]="1024 4096 16384 32768"

read -a M_list <<< ${MLists[$task]}
param_len=${#M_list[@]}

if [ $BuildFlag = True ]; then
    
    # cd ..
    # scp -r ./MP-SPDZ/CONFIG.mine spdz1:~/MP-SPDZ/ &
    # scp -r ./MP-SPDZ/CONFIG.mine spdz2:~/MP-SPDZ
    # wait;
    # cd ./MP-SPDZ/;

    make -j 8 replicated-ring-party.x &
    # ssh spdz1 "cd ./MP-SPDZ/; make -j 8 replicated-ring-party.x" &
    # ssh spdz2 "cd ./MP-SPDZ/; make -j 8 replicated-ring-party.x" &
    # wait;

fi

# compile the baseline functions.
for ((i=0; i<param_len; i++)); do
    for ((j=0; j<${#parallel_list[@]}; j++)); do
        M=${M_list[i]}; N=${N_list[i]};
        clog=${clogFile}-${task}-${N}-${M}-${REPEAT}-${parallel_list[j]};
        bc_file=./Programs/Schedules/${sourceFile}-${task}-${N}-${M}-${REPEAT}-${parallel_list[j]}.sch 
        # if [ -f ${bc_file} ]; then
        #     continue
        # fi
        python compile.py -R 64 -l -v -a ${instructFolder}instruct ${sourceFile} ${task} $N $M $REPEAT ${parallel_list[j]} > ${clog} 2>&1 &
        wait;
    done;
done;


if [ $CompileOnly = True ]; then
    exit 0
fi