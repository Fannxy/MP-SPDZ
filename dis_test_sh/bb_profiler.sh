echo "==== Test basic building blocks ===="

logFolder=~/MP-SPDZ/Record/dis_bb_profiler/
logTmp=${logFolder}tmp
sourceFile=building_blocks_profiler
compileLog=${logFolder}compile

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

rm -r ${logFolder}*

building_list=(mpc_reciprocal mpc_sqrt mpc_log mpc_exp mpc_comp mpc_mul)

# Exp 1:  repring
sprotocol=repring
logFile=${logFolder}${sprotocol}.txt
protocol=./replicated-ring-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};

cd ./MP-SPDZ/
for bb in ${building_list[*]}
    do  
        echo "continue "${bb}
        compileLog=${logFolder}compile_${bb};
        ./compile.py -R 256 ${sourceFile} 1 ${bb} > ${compileLog} &
    done

wait;
cd ..

# synchronize
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;

for bb in ${building_list[*]}
    do
        cd ./MP-SPDZ
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-1-${bb} ${logFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-1-${bb} ${logFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-1-${bb} ${logFolder} ${sprotocol}" &
        cd ..
        wait;
    done
    wait;



# Exp 2:  ps-repring
sprotocol=psrepring
logFile=${logFolder}${sprotocol}.txt
protocol=./ps-rep-ring-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};

cd ./MP-SPDZ/
for bb in ${building_list[*]}
    do
        compileLog=${logFolder}compile_${bb}
        ./compile.py -R 256 ${sourceFile} 0 ${bb} > ${compileLog} &
    done
    wait;
cd ..

# synchronize
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;

for bb in ${building_list[*]}
    do
        cd ./MP-SPDZ
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-0-${bb} ${logFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-0-${bb} ${logFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-0-${bb} ${logFolder} ${sprotocol}" &
        cd ..
        wait;
    done
wait;



# Exp 3:  rep-prime
sprotocol=repprime
logFile=${logFolder}${sprotocol}.txt
protocol=./replicated-field-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};

cd ./MP-SPDZ/
for bb in ${building_list[*]}
    do
        compileLog=${logFolder}compile_${bb}
        ./compile.py ${sourceFile} 2 ${bb} > ${compileLog} &
    done
    wait;
cd ..

# synchronize
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;

for bb in ${building_list[*]}
    do
        cd ./MP-SPDZ
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-2-${bb} ${logFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-2-${bb} ${logFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-2-${bb} ${logFolder} ${sprotocol}" &
        cd ..
        wait;
    done
wait;


# Exp 4:  shamir
sprotocol=shamir
logFile=${logFolder}${sprotocol}.txt
protocol=./shamir-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};


for bb in ${building_list[*]}
    do
        cd ./MP-SPDZ
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-2-${bb} ${logFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-2-${bb} ${logFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-2-${bb} ${logFolder} ${sprotocol}" &
        cd ..
        wait;
    done
wait;



# Exp 5:  ps-repprime
sprotocol=psrepprime
logFile=${logFolder}${sprotocol}.txt
protocol=./ps-rep-field-party.x
echo -e "Protocol - ${protocol}" >> ${logFile};

cd ./MP-SPDZ/
for bb in ${building_list[*]}
    do
        compileLog=${logFolder}compile_${bb}
        ./compile.py ${sourceFile} 0 ${bb} > ${compileLog} &
    done
    wait;
cd ..

# synchronize
scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
wait;

for bb in ${building_list[*]}
    do
        cd ./MP-SPDZ
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-0-${bb} ${logFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-0-${bb} ${logFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-0-${bb} ${logFolder} ${sprotocol}" &
        cd ..
        wait;
    done
wait;


