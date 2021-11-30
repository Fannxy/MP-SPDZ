plogFile=./record/compile_log;

# func_array=(sigmoid tanh soft_plus snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);
func_array=(reciprocal func_sqrt func_log func_exp);

for func in ${func_array[*]}
    do
        logFile=./record/compile_${func}
        ./compile.py -R 256 non_linear_funcs ${func} > ${logFile};
        echo "Finish compile" >> ${plogFile};
        sh ./test_sh/basic_test.sh non_linear_funcs replicated-ring-party.x ${func};
        echo "Finish execution" >> ${plogFile};
    done

# ./compile.py -R 256 -a ./record/tmp non_linear_funcs ${func} >> ${logFile};
# echo "Finish compile" >> ${plogFile};

# sh ./test_sh/basic_test.sh non_linear_funcs replicated-ring-party.x ${func};
# echo "Finish execution" >> ${plogFile};
