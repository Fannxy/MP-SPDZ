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