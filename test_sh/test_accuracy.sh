logFolder=./Record/accuracy/

plogFile=${logFolder}compile_log
sourceFile=accuracy_test
testProtocol=replicated-ring-party.x

func_array=(sigmoid tanh soft_plus snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);

rm -r ${logFolder}*;

for func in ${func_array[*]}
    do
        logFile=${logFolder}compile_${func};
        blogFile=${blogFolder}compile_${func};

        ./compile.py -R 256 ${sourceFile} ${func} > ${logFile};
        echo "Function "${func} >> ${plogFile};
        echo "Finish compile" >> ${plogFile};
        sh ./test_sh/basic/basic_accuracy.sh ${sourceFile}-${func} ${testProtocol} ${func};
        echo "Finish execution" >> ${plogFile};
    done