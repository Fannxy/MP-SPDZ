if [ ! -n "$1" ]; then
    echo "offer keyword: "
    read keyword
    keyword=${keyword}
else
    keyword=$1
fi

# 查找包含关键词的进程的PID  
pids=$(ps aux | grep "$keyword" | awk '{print $2}')  
  
# 杀死所有找到的进程  
for pid in $pids; do  
    kill -9 $pid
done 

if [ -n "$2" ]; then
    echo "kill for spdz1 and spdz2";
    ssh spdz1 "sh ./MP-SPDZ/Eval/control/kill.sh "${keyword};
    ssh spdz2 "sh ./MP-SPDZ/Eval/control/kill.sh "${keyword};
fi