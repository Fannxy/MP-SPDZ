prot=$1; func=$2; comptype=$3;
logFolder=$HOME/MP-SPDZ/tee_benchmark/Record/

declare -A protocol
protocol["repring"]=replicated-ring-party.x
protocol["repfield"]=replicated-field-party.x
protocol["psrepring"]=ps-rep-ring-party.x
protocol["psrepfield"]=ps-rep-field-party.x
protocol["semi2k"]=semi2k-party.x
protocol["semi"]=semi-party.x
protocol["spdz2k"]=spdz2k-party.x
protocol["mascot"]=mascot-party.x
protocol["semi-offline"]=semi-offline.x
protocol["semi2k-offline"]=semi2k-offline.x
protocol["hemi-offline"]=hemi-offline.x

declare -A parties
parties["repring"]=3; parties["repfield"]=3;
parties["psrepring"]=3; parties["psrepfield"]=3;
parties["semi2k"]=2; parties["semi"]=2;
parties["spdz2k"]=2; parties["mascot"]=2;
parties["semi2k-offline"]=2; parties["semi-offline"]=2;
parties["hemi-offline"]=2;

declare -A modular
modular["repring"]=r; modular["repfield"]=f;
modular["psrepring"]=r; modular["psrepfield"]=f;
modular["semi2k"]=r; modular["semi"]=f;
modular["spdz2k"]=r; modular["mascot"]=f;
modular["semi2k-offline"]=r; modular["semi-offline"]=f;
modular["hemi-offline"]=f;

declare -A benchmark
benchmark["lr"]=breast_logistic
benchmark["oppe"]=sigmoid
benchmark["oram"]=oram_tutorial
benchmark["comp"]=comp
benchmark["nn"]=benchmark_net

# local host: 172.31.244.198
remoteHosts=(172.31.244.198 172.31.244.197 172.31.244.196)

compileLog=${logFolder}comp_log
for host in ${remoteHosts[*]}
do
    ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "mkdir -p $logFolder"
    if [ ${modular[$prot]} == "r" ]; then
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "cd $HOME/MP-SPDZ && ./compile.py -R 64 ${benchmark[$func]} > ${compileLog}"
    fi
    if [ ${modular[$prot]} == "f" ]; then
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "cd $HOME/MP-SPDZ && ./compile.py ${benchmark[$func]} > ${compileLog}"
    fi
done

logFile=${logFolder}${func}_${prot}_${comptype}_log.txt

if [ ${comptype} == 1 -o ${comptype} == 3 ]; then
    for host in ${remoteHosts[*]}
    do
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "rm -r /Programs ; cp -r $HOME/MP-SPDZ/Programs / ; rm -r /Player-Data ; cp -r $HOME/MP-SPDZ/Player-Data /"
    done
    i=0
    if [ ${parties[$prot]} == 2 ]; then
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} -N 2 -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
        i=$(( i + 1 ))
    fi
    wait;
    if [ ${parties[$prot]} == 3 ]; then
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} -N 3 -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
        i=$(( i + 1 ))
    fi
    wait;

else
    for host in ${remoteHosts[*]}
    do
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "rm -r $HOME/MP-SPDZ/occlum_workspace/image/Programs ; rm -r $HOME/MP-SPDZ/occlum_workspace/image/Player-Data ; cp -r $HOME/MP-SPDZ/Programs $HOME/MP-SPDZ/occlum_workspace/image/ ; cp -r $HOME/Player-Data $HOME/MP-SPDZ/occlum_workspace/image/ ; cd $HOME/MP-SPDZ/occlum_workspace && occlum build"
    done

    i=0
    if [ ${parties[$prot]} == 2 ]; then
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -N 2 -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
        i=$(( i + 1 ))
    fi
    wait;
    if [ ${parties[$prot]} == 3 ]; then
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -N 3 -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
         i=$(( i + 1 ))
    fi
    wait;
fi
