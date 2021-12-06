plogFile=./record/compile_log;
pbenlogFile=./record_benchmark/compile_log;

# func_array=(sigmoid tanh soft_plus snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);
# func_array=(reciprocal func_sqrt func_log func_exp);
func_array=(snormal_dis);

for func in ${func_array[*]}
    do
        logFile=./record/compile_${func};
        blogFile=./record_benchmark/compile_${func};
        
        # compile and run our function.
        # ./compile.py -R 256 non_linear_funcs ${func} > ${logFile};
        # echo "Finish compile" >> ${plogFile};
        # sh ./test_sh/basic_test.sh non_linear_funcs-${func} replicated-ring-party.x ${func};
        # echo "Finish execution general-"${func} >> ${plogFile};

        # compile and run benchmark.
        ./compile.py -R 256 benchmark_nonlinear ${func} > ${blogFile};
        echo "Function benchmark-"${func} >> ${pbenlogFile};
        sh ./test_sh/basic_benchmark.sh benchmark_nonlinear-${func} replicated-ring-party.x ${func};
        echo "Finish execution benchmark-"${func} >> ${pbenlogFile};
    done