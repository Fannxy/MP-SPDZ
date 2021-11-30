plogFile=./record/execute_log;

./compile.py -R 256 non_linear_funcs -m 20;
echo "Finish compile" >> ${plogFile};

sh ./test_sh/basic_test.sh non_linear_funcs replicated-ring-party.x test;
echo "Finish execution" >> ${plogFile};