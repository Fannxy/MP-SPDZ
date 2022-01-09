logFolder=./Record/efficiency/
blogFolder=./Record/benchmark/

plogFile=${logFolder}compile_log;
bplogFile=${blogFolder}compile_log;
sourceFile=non_linear_funcs
bsourceFile=benchmark_nonlinear

func_array=(sigmoid tanh soft_plus snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);

for func in ${func_array[*]}
    do
        logFile=${logFolder}compile_${func};
        blogFile=${blogFolder}compile_${func};

        ./compile.py -R 256 ${sourceFile} ${func} > ${logFile};
        echo "Function "${func} >> ${plogFile};
        echo "Finish compile" >> ${plogFile};
        sh ./test_sh/basic_benchmark.sh ${sourceFile}-${func} replicated-ring-party.x ${func};
        echo "Finish execution" >> ${plogFile};

        ./compile.py -R 256 ${bsourceFile} ${func} > ${blogFile};
        echo "Function "${func} >> ${bplogFile};
        echo "Finish compile" >> ${bplogFile};
        sh ./test_sh/benchmark.sh ${bsourceFile}-${func} replicated-ring-party.x ${func};
        echo "Finish execution" >> ${bplogFile};
    done
