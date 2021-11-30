echo "==== dot product ===="

plogFile=./record/profiler_log

./compile.py -R 256 bb_profiler;
echo "Finish compile step2" >> ${plogFile};

sh ./test_sh/basic_test.sh bb_profiler replicated-ring-party.x dot-product;
echo "Finish execution" >> ${plogFile};
