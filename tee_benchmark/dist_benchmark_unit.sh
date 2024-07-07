prot=$1; func=$2; comptype=$3; n=$4;
logFolder=$HOME/MP-SPDZ/tee_benchmark/Record
echo "compute type = $comptype"

declare -A protocol
protocol["repring"]=replicated-ring-party.x
protocol["repfield"]=replicated-field-party.x
protocol["psrepring"]=ps-rep-ring-party.x
protocol["psrepfield"]=ps-rep-field-party.x
protocol["shamir"]=shamir-party.x
protocol["malicious-shamir"]=malicious-shamir-party.x
protocol["semi2k"]=semi2k-party.x
protocol["semi"]=semi-party.x
protocol["spdz2k"]=spdz2k-party.x
protocol["mascot"]=mascot-party.x
protocol["hemi"]=hemi-party.x
protocol["lowgear"]=lowgear-party.x
protocol["soho"]=soho-party.x
protocol["highgear"]=highgear-party.x
protocol["semi-offline"]=semi-offline.x
protocol["semi2k-offline"]=semi2k-offline.x
protocol["hemi-offline"]=hemi-offline.x

declare -A parties
parties["repring"]=3; parties["repfield"]=3;
parties["psrepring"]=3; parties["psrepfield"]=3;
parties["shamir"]=$n; parties["malicious-shamir"]=$n;
parties["semi2k"]=$n; parties["semi"]=$n;
parties["spdz2k"]=$n; parties["mascot"]=$n;
parties["hemi"]=$n;   parties["lowgear"]=$n;
parties["soho"]=$n;   parties["highgear"]=$n;
parties["semi2k-offline"]=$n; parties["semi-offline"]=$n;
parties["hemi-offline"]=$n;

declare -A modular
modular["repring"]=r; modular["repfield"]=f;
modular["psrepring"]=r; modular["psrepfield"]=f;
modular["shamir"]=f; modular["malicious-shamir"]=f;
modular["semi2k"]=r; modular["semi"]=f;
modular["spdz2k"]=r; modular["mascot"]=f;
modular["hemi"]=f;  modular["lowgear"]=f;
modular["soho"]=f;  modular["highgear"]=f;
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

compileLog=${logFolder}/comp_log
i=0
for host in ${remoteHosts[*]}
do
    if [ $i == ${parties[$prot]} ]; then
        break
    fi
    ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "mkdir -p $logFolder"
    if [ ${modular[$prot]} == "r" ]; then
	echo "compile -R 64 for $prot $func on host $host"
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "cd $HOME/MP-SPDZ && ./compile.py -R 64 ${benchmark[$func]} > ${compileLog}"
    fi
    if [ ${modular[$prot]} == "f" ]; then
	echo "compile for $prot $func on host $host"
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "cd $HOME/MP-SPDZ && ./compile.py ${benchmark[$func]} > ${compileLog}"
    fi
    i=$(( i + 1 ))
done

logFile=${logFolder}/${func}_${prot}_${comptype}_${n}_log.txt
echo "logFile = $logFile"

if [ ${comptype} == 1 -o ${comptype} == 3 -o ${comptype} == 7 ]; then
    echo "without TEE"
    i=0
    for host in ${remoteHosts[*]}
    do
	if [ $i == ${parties[$prot]} ]; then
            break
        fi
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "rm -r /Programs ; cp -r $HOME/MP-SPDZ/Programs / ; rm -r /Player-Data ; cp -r $HOME/MP-SPDZ/Player-Data /"
	i=$(( i + 1 ))
    done

    echo "begin to run"
    i=0
    for host in ${remoteHosts[*]}
    do
        if [ $i == ${parties[$prot]} ]; then
	    break
	fi
	{
        if [[ ${protocol[$prot]} == *"rep"* ]]; then
	    echo "run command: ./${protocol[$prot]} --ip-file-name /HOST -p $i -v ${benchmark[$func]} on host $host"
            ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
    	elif [[ ${protocol[$prot]} == *"shamir"* ]]; then
	    echo "run command: ./${protocol[$prot]} -N ${parties[$prot]} -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} on host $host"
            ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} -N ${parties[$prot]} --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
	elif [[ ${protocol[$prot]} == *"hemi"* ]]; then
	    echo "run command: ./${protocol[$prot]} -N ${parties[$prot]} -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} on host $host"
	    ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} -N ${parties[$prot]} --ip-file-name /HOST -p $i -M -v ${benchmark[$func]} >${logFile} 2>&1"
    	else
	    echo "run command: ./${protocol[$prot]} -N ${parties[$prot]} -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} on host $host"
            ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} -N ${parties[$prot]} -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
        fi
        }&
        i=$(( i + 1 ))
    done
    wait;

else
    i=0
    for host in ${remoteHosts[*]}
    do
	if [ $i == ${parties[$prot]} ]; then
            break
        fi
	{
	ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "PATH=$PATH ; rm -r $HOME/MP-SPDZ/occlum_workspace/image/Programs ; rm -r $HOME/MP-SPDZ/occlum_workspace/image/Player-Data ; cp -r $HOME/MP-SPDZ/Programs $HOME/MP-SPDZ/occlum_workspace/image/ ; cp -r $HOME/MP-SPDZ/Player-Data $HOME/MP-SPDZ/occlum_workspace/image/ ; cd $HOME/MP-SPDZ/occlum_workspace && occlum build"
	}&
        i=$(( i + 1 ))
    done
    wait;

    i=0
    for host in ${remoteHosts[*]}
    do
        if [ $i == ${parties[$prot]} ]; then
            break
        fi
        {
        if [[ ${protocol[$prot]} == *"rep"* ]]; then
            ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
    	elif [[ ${protocol[$prot]} == *"shamir"* ]]; then
	    ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -N ${parties[$prot]} --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
	elif [[ ${protocol[$prot]} == *"hemi"* ]]; then
	    ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -N ${parties[$prot]} --ip-file-name /HOST -p $i -M -v ${benchmark[$func]} >${logFile} 2>&1"
    	else
            ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -N ${parties[$prot]} -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"

	fi
        }&
        i=$(( i + 1 ))
    done
    wait;
fi
