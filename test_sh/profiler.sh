logFolder=./Record/profiler/
compileLog=${logFolder}compile_log
logFile=${logFolder}profiler
logTmp=${logFolder}tmp
logEx=${logFolder}exe_log
sourceFile=non_linear_profiler

# # generate profiler rep3.
# protocol=./replicated-ring-party.x
protocol=./ps-rep-ring-party.x
echo -e "Test protocol - ${protocol}\n" >> ${logFile};
kArray=($(seq 3 2 20));
mArray=($(seq 2 15 100));

for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                ./compile.py -R 256 ${sourceFile} 0 $k $m 0 >> ${compileLog} &
            done
        wait;
    done

for k in ${kArray[@]}
    do 
        for m in ${mArray[@]}
            do 
                echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFile}; 
                # ./compile.py -R 256 ${sourceFile} 1 $k $m >> ${compileLog} &
                ${protocol} -p 0 ${sourceFile}-0-${k}-${m}-0 >> ${logFile} & ${protocol} -p 1 ${sourceFile}-0-${k}-${m}-0 >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-0-${k}-${m}-0 >> ${logTmp}
                wait;
                echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logFile};
            done
    done

# generate profile shamir-party
# protocol=./shamir-party.x
# protocol=./replicated-field-party.x
# protocol=./ps-rep-field-party.x
# echo -e "Test protocol - ${protocol}\n" >> ${logFile};
# kArray=($(seq 3 2 20));
# mArray=($(seq 2 15 100));

# for k in ${kArray[@]}
#     do 
#         for m in ${mArray[@]}
#             do 
#                 ./compile.py ${sourceFile} 0 $k $m 0 >> ${compileLog} & 
#             done
#             wait;
#     done

# for k in ${kArray[@]}
#     do 
#         for m in ${mArray[@]}
#             do 
#                 echo "Protocol ${protocol} test for k, m = ${k}, ${m} " >> ${logFile}; 
#                 ${protocol} -p 0 ${sourceFile}-0-${k}-${m}-0 >> ${logFile} & ${protocol} -p 1 ${sourceFile}-0-${k}-${m}-0 >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-0-${k}-${m}-0 >> ${logTmp}
#                 wait;
#                 echo -e "Success ${protocol} for (k, m)=(${k}, ${m}) \n\n\n" >> ${logFile};
#             done
#     done

