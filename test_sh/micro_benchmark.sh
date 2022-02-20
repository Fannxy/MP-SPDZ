logFolder=./Record/Shamir3/efficiency/
blogFolder=./Record/Shamir3/benchmark/

plogFile=${logFolder}compile_log;
bplogFile=${blogFolder}compile_log;
sourceFile=non_linear_funcs
bsourceFile=benchmark_nonlinear


rm -r ${logFolder}*
rm -r ${blogFolder}*

func_array=(sigmoid tanh soft_plus elu selu gelu soft_sign isru snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);

func_array=(elu);

# # replicated-ring3
# for func in ${func_array[*]}
#     do
#         logFile=${logFolder}compile_${func};
#         blogFile=${blogFolder}compile_${func};

#         ./compile.py -R 256 ${sourceFile} ${func} ring > ${logFile};
#         echo "Function "${func} >> ${plogFile};
#         echo "Finish compile" >> ${plogFile};
#         sh ./test_sh/basic/basic_efficiency.sh ${sourceFile}-${func}-ring replicated-ring-party.x ${func} ${logFolder};
#         echo "Finish execution" >> ${plogFile};

#         ./compile.py -R 256 ${bsourceFile} ${func} ring > ${blogFile};
#         echo "Function "${func} >> ${bplogFile};
#         echo "Finish compile" >> ${bplogFile};
#         # sh ./test_sh/basic/basic_benchmark.sh ${bsourceFile}-${func} replicated-ring-party.x ${func} ${logFolder};
#         sh ./test_sh/basic/basic_efficiency.sh ${bsourceFile}-${func}-ring replicated-ring-party.x ${func} ${blogFolder};
#         echo "Finish execution" >> ${bplogFile};
#     done


# shamir3
for func in ${func_array[*]}
    do
        logFile=${logFolder}compile_${func};
        blogFile=${blogFolder}compile_${func};

        ./compile.py ${sourceFile} ${func} field > ${logFile};
        echo "Function "${func} >> ${plogFile};
        echo "Finish compile" >> ${plogFile};
        sh ./test_sh/basic/basic_efficiency.sh ${sourceFile}-${func}-field shamir-party.x ${func} ${logFolder};
        echo "Finish execution" >> ${plogFile};

        ./compile.py ${bsourceFile} ${func} field > ${blogFile};
        echo "Function "${func} >> ${bplogFile};
        echo "Finish compile" >> ${bplogFile};
        # sh ./test_sh/basic/basic_benchmark.sh ${bsourceFile}-${func} replicated-ring-party.x ${func} ${logFolder};
        sh ./test_sh/basic/basic_efficiency.sh ${bsourceFile}-${func}-field shamir-party.x ${func} ${blogFolder};
        echo "Finish execution" >> ${bplogFile};
    done
