sprotocol=repring
protocol=./replicated-ring-party.x

logFolder=./Record/${sprotocol}/efficiency/
blogFolder=./Record/${sprotocol}/benchmark/

if [ ! -d ${logFolder} ]; then
    mkdir ${logFolder};
fi

if [ ! -d ${blogFolder} ]; then
    mkdir ${blogFolder};
fi

rm -r ${logFolder}*;
rm -r ${blogFolder}*;

func_array=(sigmoid tanh soft_plus elu selu gelu soft_sign isru snormal_dis scauchy_dis gamma_dis sexp_dis chi_square slog_dis reciprocal func_sqrt func_log func_exp);

for func in ${func_array[*]}
    do
        logFile=${logFolder}compile_${func};
        blogFile=${blogFolder}compile_${func};

        # compile and synchronize.
        cd ./MP-SPDZ/
        ./compile.py -R 256 ${sourceFile} ${func} ring ${sprotocol} > ${logFile};
        cd ..
        wait;

        scp -r ./MP-SPDZ/Programs mp-spdz131:~/MP-SPDZ/ & 
        scp -r ./MP-SPDZ/Programs mp-spdz132:~/MP-SPDZ/
        wait;

        # party-0
        cd ./MP-SPDZ
        ./dis_test_sh/basic_dis/exec.sh 0 ${protocol} ${sourceFile}-${func}-ring-${sprotocol} ${logFolder} ${sprotocol} & 
        # party-1
        ssh mp-spdz131 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 1 ${protocol} ${sourceFile}-${func}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
        # party-2
        ssh mp-spdz132 "cd ./MP-SPDZ/; ./dis_test_sh/basic_dis/exec.sh 2 ${protocol} $${sourceFile}-${func}-ring-${sprotocol} ${logFolder} ${sprotocol}" &
        cd ..
        wait;
    done