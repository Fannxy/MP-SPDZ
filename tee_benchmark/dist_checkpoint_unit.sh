prot=$1; func=$2; comptype=$3;
logFolder=$HOME/MP-SPDZ/tee_benchmark/Record
echo "compute type = $comptype"

declare -A protocol
protocol["repring"]=replicated-ring-party.x
protocol["repfield"]=replicated-field-party.x
protocol["semi2k"]=semi2k-party.x
protocol["semi"]=semi-party.x

declare -A parties
parties["repring"]=3; parties["repfield"]=3;
parties["semi2k"]=2; parties["semi"]=2;

declare -A modular
modular["repring"]=r; modular["repfield"]=f;
modular["semi2k"]=r; modular["semi"]=f;

declare -A benchmark
benchmark["lr"]=breast_logistic
benchmark["oppe"]=sigmoid
benchmark["oram"]=oram_tutorial
benchmark["comp"]=comp
benchmark["nn"]=benchmark_net

# local host: 172.31.244.198
remoteHosts=(172.31.244.198 172.31.244.197 172.31.244.196)

compileLog=${logFolder}/comp_log
for host in ${remoteHosts[*]}
do
    ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "mkdir -p $logFolder"
    if [ ${modular[$prot]} == "r" ]; then
	echo "compile -R 64 -A for $prot $func on host $host"
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "cd $HOME/MP-SPDZ && ./compile.py -R 64 -A ${benchmark[$func]} > ${compileLog}"
    fi
    if [ ${modular[$prot]} == "f" ]; then
	echo "compile -A for $prot $func on host $host"
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "cd $HOME/MP-SPDZ && ./compile.py -A ${benchmark[$func]} > ${compileLog}"
    fi
done

if [ ${comptype} == 6 ]; then
    for host in ${remoteHosts[*]}
    do
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "PATH=$PATH ; rm -r $HOME/MP-SPDZ/occlum_workspace/image/Programs ; rm -r $HOME/MP-SPDZ/occlum_workspace/image/Player-Data ; cp -r $HOME/MP-SPDZ/Programs $HOME/MP-SPDZ/occlum_workspace/image/ ; cp -r $HOME/Player-Data $HOME/MP-SPDZ/occlum_workspace/image/ ; cd $HOME/MP-SPDZ/occlum_workspace && occlum build"
    done

    for period in 1 5 10 20 50 100
    do
        logFile=${logFolder}/${func}_${prot}_${comptype}_${period}_log.txt
        echo "logFile = $logFile"
        i=0
        for host in ${remoteHosts[*]}
        do

            if [ $i == 2 -a ${parties[$prot]} == 2 ]; then
                break
            fi
            {
            if [ ${parties[$prot]} == 2 ]; then
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -A $period -N 2 -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} > ${logFile} 2>&1"
            fi
            if [ ${parties[$prot]} == 3 ]; then
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -A $period --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
            fi
            }&
            i=$(( i + 1 ))
        done
        wait;
    done
fi
