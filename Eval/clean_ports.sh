#!/bin/bash

for i in {0..3}; do
    pid=$(netstat -tunpl | grep 500$i | awk '{print $7}' | sed "s/\// /g" | awk '{print $1}')
    
    if [ -n "$pid" ]; then
        echo "Killing process $pid on port 500$i"
        kill -9 $pid
    else
        echo "No process found on port 500$i"
    fi
done