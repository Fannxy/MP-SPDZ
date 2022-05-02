logFolder=~/MP-SPDZ/Record/dis_profiler/
compileLog=${logFolder}compile_log
logTmp=${logFolder}tmp
logEx=${logFolder}exe_log
sourceFile=non_linear_profiler

# rm -r ${logFolder}*;

echo -e "Test protocol - ${protocol}\n" >> ${logEx};
kArray=($(seq 3 2 10));
mArray=($(seq 2 2 50));
m1Array=($(seq 2 2 20));
m2Array=($(seq 22 2 32));
m3Array=($(seq 34 2 40));
m4Array=($(seq 42 2 48));


# Profiler1 - Rep3
protocol=./replicated-ring-party.x
logFile=repring
echo -e "Test protocol - ${protocol}\n" >> ${logEx};

for k in ${kArray[@]}
    do 
        for m in ${m1Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 1 $k $m >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m2Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 1 $k $m >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m3Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 1 $k $m >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m4Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 1 $k $m >> ${compileLog} &
                cd ..
            done
        wait;
    done

synchronize
scp -r ./MP-SPDZ/Programs/ mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs/ mp-spdz132:~/MP-SPDZ/
wait;

for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFolder}${logFile}; 
                # party-0
                cd ./MP-SPDZ 
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-1-${k}-${m} ${logFolder} ${logFile} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-1-${k}-${m} ${logFolder} " &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-1-${k}-${m} ${logFolder} " &
                cd ..
                wait;
                echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logEx};
            done
    done
wait;


#Profiler2 - RepPrime
protocol=./replicated-field-party.x
logFile=repprime
echo -e "Test protocol - ${protocol}\n" >> ${logEx};

for k in ${kArray[@]}
    do 
        for m in ${m1Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m2Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m3Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m4Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
    done

# synchronize
scp -r ./MP-SPDZ/Programs/ mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs/ mp-spdz132:~/MP-SPDZ/
wait;

for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFile}; 
                # party-0
                cd ./MP-SPDZ 
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} ${logFile} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
                cd ..
                wait;
                echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logEx};
            done
    done
wait;

# Profiler2 - PsRepPrime
protocol=./ps-rep-field-party.x
logFile=psrepprime
echo -e "Test protocol - ${protocol}\n" >> ${logEx};

# compile in single machine.
for k in ${kArray[@]}
    do 
        for m in ${m1Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m2Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m3Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m4Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
    done

# synchronize
scp -r ./MP-SPDZ/Programs/ mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs/ mp-spdz132:~/MP-SPDZ/
wait;


for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logEx}; 
                # party-0
                cd ./MP-SPDZ 
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} ${logFile} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} " &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} " &
                cd ..
                wait;
                echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logEx};
            done
    done
wait;


# Profiler4 - PsRepRing
protocol=./ps-rep-ring-party.x
logFile=psrepring
echo -e "Test protocol - ${protocol}\n" >> ${logEx};

# compile in single machine.
for k in ${kArray[@]}
    do 
        for m in ${m1Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m2Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m3Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m4Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py -R 256 ${sourceFile} 0 $k $m 0 >> ${compileLog} &
                cd ..
            done
        wait;
    done

# synchronize
scp -r ./MP-SPDZ/Programs/ mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs/ mp-spdz132:~/MP-SPDZ/
wait;


for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logEx}; 
                # party-0
                cd ./MP-SPDZ 
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} ${logFile} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} " &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-0-${k}-${m}-0 ${logFolder} " &
                cd ..
                wait;
                echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logEx};
            done
    done
wait;


# Profiler5 - Shamir
protocol=./shamir-party.x
logFile=shamir
echo -e "Test protocol - ${protocol}\n" >> ${logEx};

for k in ${kArray[@]}
    do 
        for m in ${m1Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0>> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m2Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0>> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m3Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0>> ${compileLog} &
                cd ..
            done
        wait;
        for m in ${m4Array[@]}
            do 
                cd ./MP-SPDZ/
                ./compile.py ${sourceFile} 2 $k $m 0>> ${compileLog} &
                cd ..
            done
        wait;
    done

# synchronize
scp -r ./MP-SPDZ/Programs/ mp-spdz131:~/MP-SPDZ/ & 
scp -r ./MP-SPDZ/Programs/ mp-spdz132:~/MP-SPDZ/
wait;

for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFile}; 
                # party-0
                cd ./MP-SPDZ 
                ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} ${logFile} & 
                # party-1
                ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
                # party-2
                ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} ${sourceFile}-2-${k}-${m}-0 ${logFolder} " &
                cd ..
                wait;
                echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logEx};
            done
    done
wait;
