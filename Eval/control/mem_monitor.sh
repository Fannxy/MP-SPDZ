report=$1

while true    
do    
    free -h | grep Mem | awk '{print $3}' | tr -d 'i'  >> ${report}  
    sleep 1  
done    