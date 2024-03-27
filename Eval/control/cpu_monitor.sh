report=$1; process_keyword=$2

# while true    
# do    
#     cpu_usage=$(top -b -n 1 | grep ${process_keyword} | awk '{print $2+$4}')   
#     echo "$cpu_usage" >> ${report}  
#     sleep 1 
# done
PIDS=$(pgrep -f ${process_keyword} | tr '\n' ',' | sed 's/,$//')

watch -n 0.5 -t "ps -p ${PIDS} -o pid,ppid,cmd,%cpu,%mem >> ${report}" >> /dev/null