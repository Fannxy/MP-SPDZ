plogFile=./record_benchmark/compile_log;

func_array=(sigmoid tanh soft_plus snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);
# func_array=(reciprocal func_sqrt func_log func_exp);

for func in ${func_array[*]}
    do
        logFile=./record_benchmark/compile_${func};

        ./compile.py -R 256 benchmark_nonlinear ${func} > ${logFile};
        echo "Function "${func} >> ${plogFile};
        echo "Finish compile" >> ${plogFile};
        sh ./test_sh/basic_benchmark.sh benchmark_nonlinear-${func} replicated-ring-party.x ${func};
        echo "Finish execution" >> ${plogFile};
    done
