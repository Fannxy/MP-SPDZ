echo "==== Test basic building blocks ===="

logFolder=./Record/basic_profiler/
logFile=${logFolder}profiler
logTmp=${logFolder}tmp
sourceFile=bb_profiler

echo -e "protocol rep3" >> ${logFile};
protocol=./replicated-ring-party.x
./compile.py -R 256 ${sourceFile} ring;
${protocol} -p 0 ${sourceFile}-ring >> ${logFile} & ${protocol} -p 1 ${sourceFile}-ring >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-ring >> ${logTmp}
wait; 


echo -e "protocol shamir3" >> ${logFile};
protocol=./shamir-party.x
./compile.py ${sourceFile} field;
${protocol} -p 0 ${sourceFile}-field >> ${logFile} & ${protocol} -p 1 ${sourceFile}-field >> ${logTmp} & ${protocol} -p 2 ${sourceFile}-field >> ${logTmp}
wait;