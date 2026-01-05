# start network and set the bandwidth
parties_num=$1
bandwidth=$2
latency=$3
if [ ${parties_num} -eq 3 ]; then
    bw_list="$bandwidth $bandwidth $bandwidth"
    atency_list="$latency $latency $latency"
else
    bw_list="$bandwidth $bandwidth $bandwidth $bandwidth"
    atency_list="$latency $latency $latency $latency"
fi

ip="$4"
logFolder="$5"
mn -c
root_folder=/root/llm-project/NFGen+KAN/
# root_folder=/root/
log_file=${logFolder}network_setup.log

MININET_SESSION="mininet"
mininet_folder=/root/llm-project/NFGen+KAN/aby3/Net/mininet
# mininet_folder=/root/mininet

# 检查 tmux 会话是否存在
if tmux has-session -t $MININET_SESSION 2>/dev/null; then
    echo "tmux session $MININET_SESSION already exists"
else
    # 创建一个新的 tmux 会话
    tmux new-session -d -s $MININET_SESSION
    echo "tmux session $MININET_SESSION created"
fi

cd ${mininet_folder};
# tmux new-session -d -s $MININET_SESSION "python ./examples/p2p_3pc_net.py --ip 10.1.0.12 --bw $bw_list; bash"
if [ ${parties_num} -eq 3 ]; then
    tmux send-keys -t $MININET_SESSION "cd ${mininet_folder}; python ./examples/p2p_3pc_net.py --ip ${ip} --bw $bw_list; bash" C-m
else
    tmux send-keys -t $MININET_SESSION "cd ${mininet_folder}; python ./examples/p2p_4pc_net.py --ip ${ip} --bw $bw_list; bash" C-m
fi

echo "output the information to ${log_file}."

# wait for the network to be set up
for i in $(seq 1 ${parties_num}); do
    host="h${i}"
    while ! ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no $host "exit" 2>/dev/null; do
        echo "Waiting for $host to be ready..." >> $log_file
        sleep 5
    done
    echo "$host is ready" >> $log_file
done

echo "All hosts are ready" >> $log_file