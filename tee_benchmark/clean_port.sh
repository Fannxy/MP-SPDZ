#!/bin/bash

remoteHosts=(172.31.244.198 172.31.244.197 172.31.244.196)
i=0
for host in ${remoteHosts[*]}
do
    ssh -i $HOME/.ssh/id_ed25519 -p 1234 root@$host "netstat -tunpl | grep 500$i | awk '{print \$7}' | sed \"s/\\// /g\" | awk '{print \$1}' | xargs kill -9 "
    i=$(( i + 1 ))
done
