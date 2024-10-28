#!/bin/bash

prot=$1; func=$2; modular=$3;
MAIN_FOLDER=$HOME/RoundRole/MP-SPDZ/
logFolder=$MAIN_FOLDER/Record
compileLog=${logFolder}/comp_log-${func}-${comptype}

# mkdir $logFolder if it dose not exist
if [ ! -d $logFolder ]; then
    mkdir $logFolder
fi

# compile the program.
if [ ${modular} == "r" ]; then
    echo "compile -R 64 -A for $prot $func"
    ./compile.py -R 64 ${func} > ${compileLog}
fi