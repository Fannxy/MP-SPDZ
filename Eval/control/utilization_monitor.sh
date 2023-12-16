report=$1

while true    
do    
    cpu_usage=$(top -b -n 1 | grep "Cpu(s)" | awk '{print $2+$4}')  
    mem_usage=$(free -h | grep Mem | awk '{print $3}' | tr -d 'i')  
    bandwidth_usage=$(ifstat -t 1 1 | grep eth0 | awk '{print $8}')  
    echo "$cpu_usage $mem_usage $bandwidth_usage" >> ${report}  
    sleep 1 
done