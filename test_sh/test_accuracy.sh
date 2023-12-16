logFolder=./Record/accuracy/

plogFile=${logFolder}compile_log
sourceFile=benchmark_accuracy

func_array=(sigmoid tanh soft_plus elu selu gelu soft_sign isru snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);
# func_array=(func_sqrt reciprocal func_log func_exp)
# func_array=(reciprocal, slog_dis, soft_plus)

rm -r ${logFolder}*;

testProtocol=replicated-ring-party.x
for func in ${func_array[*]}
    do
        logFile=${logFolder}compile_${func};

        ./compile.py -R 256 ${sourceFile} ${func} ring > ${logFile};
        echo "Function "${func} >> ${plogFile};
        echo "Finish compile" >> ${plogFile};
        sh ./test_sh/basic/basic_accuracy.sh ${sourceFile}-${func}-ring ${testProtocol} ${func} ${logFolder};
        echo "Finish execution" >> ${plogFile};
    done

# # Then test the problemtic exp function in MP-SPDZ.
# ./compile.py -R 256 test_accuracy;
# echo -e "exp test (-50, +50)" >> ${plogFile};
# sh ./test_sh/basic/basic_accuracy.sh test_accuracy ${testProtocol} exp ${logFolder};
# echo "Finish execution" >> ${plogFile};