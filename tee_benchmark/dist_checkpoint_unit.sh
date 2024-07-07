prot=$1; func=$2; comptype=$3;
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
parties["semi2k"]=2; parties["semi"]=2;
parties["hemi"]=2;   parties["soho"]=2;
parties["shamir"]=3;

declare -A modular
modular["repring"]=r; modular["repfield"]=f;
modular["semi2k"]=r; modular["semi"]=f;
modular["shamir"]=f; modular["hemi"]=f; modular["soho"]=f;


declare -A benchmark
benchmark["lr"]=breast_logistic
benchmark["oppe"]=sigmoid
benchmark["oram"]=oram_tutorial
benchmark["comp"]=comp
benchmark["nn"]=benchmark_net

# local host: 172.31.244.198
remoteHosts=(172.31.244.206 172.31.244.213 172.31.244.211)

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
    {
        echo "handle Player-Data and Programs"
	ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "PATH=$PATH ; rm -r $HOME/MP-SPDZ/occlum_workspace/image/Programs ; rm -r $HOME/MP-SPDZ/occlum_workspace/image/Player-Data ; cp -r $HOME/MP-SPDZ/Programs $HOME/MP-SPDZ/occlum_workspace/image/ ; cp -r $HOME/MP-SPDZ/Player-Data $HOME/MP-SPDZ/occlum_workspace/image/ ; cd $HOME/MP-SPDZ/occlum_workspace && occlum build"
    }&
    done

    for period in 50 100 200 500 1000
    do
        logFile=${logFolder}/${func}_${prot}_${comptype}_p${period}_log.txt
        echo "logFile = $logFile"
        i=0
        for host in ${remoteHosts[*]}
        do
	    if [ $i == ${parties[$prot]} ]; then
                break
            fi
            {
            if [[ ${protocol[$prot]} == *"rep"* ]]; then
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -A $period  --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
            elif [[ ${protocol[$prot]} == *"shamir"* ]]; then
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -A $period -N ${parties[$prot]} --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
            elif [[ ${protocol[$prot]} == *"hemi"* ]]; then
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -A $period -N ${parties[$prot]} --ip-file-name /HOST -p $i -M -v ${benchmark[$func]} >${logFile} 2>&1"
            else
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "PATH=$PATH ; cd $HOME/MP-SPDZ/occlum_workspace && occlum run /bin/${protocol[$prot]} -A $period -N ${parties[$prot]} -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"

            fi
            }&
            i=$(( i + 1 ))
        done
        wait;
    done
else
    for host in ${remoteHosts[*]}
    do
        echo "handle Player-Data and Programs"
        ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "rm -r /Programs ; cp -r $HOME/MP-SPDZ/Programs / ; rm -r /Player-Data ; cp -r $HOME/MP-SPDZ/Player-Data /"
    done

    for period in 50 100 200 500 1000
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
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} -N 2 -e --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
            fi
            if [ ${parties[$prot]} == 3 ]; then
                ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@${remoteHosts[$i]} "cd $HOME/MP-SPDZ && ./${protocol[$prot]} --ip-file-name /HOST -p $i -v ${benchmark[$func]} >${logFile} 2>&1"
            fi
            }&
            i=$(( i + 1 ))
        done
        wait;
    done
fi
