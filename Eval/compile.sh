#!/bin/bash

prot=$1; func=$2; modular=$3;
MAIN_FOLDER=$HOME/RoundRole/MP-SPDZ/
logFolder=$MAIN_FOLDER/Record
compileLog=${logFolder}/comp_log-${func}-${modular}

# mkdir $logFolder if it dose not exist
if [ ! -d $logFolder ]; then
    mkdir $logFolder
fi

echo "prot = $prot, func = $func, modular = $modular"

# compile the program.
if [ ${modular} == "r" ]; then
    echo "compile -R 64 -A for $prot $func"
    python3.9 ./compile.py -R 64 ${func} r > ${compileLog}
elif [ ${modular} == "f" ]; then
    echo ">>>>>>>>>>>>>>>>>>>> compile -A for $prot $func"
    python3.9 ./compile.py ${func} f > ${compileLog}
fi