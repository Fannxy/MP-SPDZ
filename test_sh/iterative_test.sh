plogFile=./record/execute_log;

./compile.py -R 256 non_linear_funcs -a ./record/tmp >> ${plogFile};
echo "Finish compile" >> ${plogFile};

sh ./test_sh/basic_test.sh non_linear_funcs replicated-ring-party.x test_general_non_linear;
echo "Finish execution" >> ${plogFile};

# ./compile.py -R 256 test_general_iterative -m 20;
# echo "Finish compile" >> ${plogFile};

# sh ./test_sh/basic_test.sh test_general_iterative replicated-ring-party.x general_iterative_time;
# echo "Finish execution" >> ${plogFile};
