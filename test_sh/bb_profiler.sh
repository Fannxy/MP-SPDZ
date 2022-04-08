#!/bin/bash
echo "==== Test basic building blocks ===="

logFolder=./MP-SPDZ/Record/basic_profiler/
logFile=${logFolder}profiler
logTmp=${logFolder}tmp
sourceFile=bb_profiler

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder}
fi

protocol=./MP-SPDZ/ps-rep-field-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};

# compile and synchronize
# ./MP-SPDZ/compile.py -R 256 ${sourceFile} ring;
./MP-SPDZ/compile.py ${sourceFile} others;
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;



# if log folder not exist, mkdir one.
# echo -e "protocol rep3" >> ${logFile};
# protocol=./replicated-ring-party.x
# # three party compile
# compile_command=./MP-SPDZ/compile.py -R 256 ${sourceFile} ring;
# ${compile_command};
# ssh mp-spdz131 ${compile_command};
# ssh mp-spdz132 ${compile_command};

# ${protocol} -p ${party} ${sourceFile}-ring >> ${logFile};
# ${protocol} -p 1 ${sourceFile}-ring >> ${logTmp};
# ${protocol} -p 2 ${sourceFile}-ring >> ${logTmp};
# wait; 


# echo -e "protocol shamir3" >> ${logFile};
# protocol=./shamir-party.x
# ./compile.py ${sourceFile} field;
# ${protocol} -p 0 ${sourceFile}-field >> ${logFile} & ${protocol} -p 1 ${sourceFile}-field >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-field >> ${logTmp}
# wait;

# echo -e "\n\nprotocol rep prime" >> ${logFile};
# protocol=./replicated-field-party.x
# ./compile.py ${sourceFile} field;
# ${protocol} -p 0 ${sourceFile}-field >> ${logFile} & ${protocol} -p 1 ${sourceFile}-field >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-field >> ${logTmp}
# wait;

# echo -e "\n\nprotocol ps rep prime" >> ${logFile};
# protocol=./ps-rep-field-party.x
# ./compile.py ${sourceFile} field;
# ${protocol} -p 0 ${sourceFile}-field >> ${logFile} & ${protocol} -p 1 ${sourceFile}-field >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-field >> ${logTmp}
# wait;

# echo -e "\n\nprotocol ps rep ring" >> ${logFile};
# protocol=./ps-rep-ring-party.x
# ./compile.py -R 256 ${sourceFile} wo;
# ${protocol} -p 0 ${sourceFile}-wo >> ${logFile} & ${protocol} -p 1 ${sourceFile}-wo >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-wo >> ${logTmp}
# wait;