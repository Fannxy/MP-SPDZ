tc qdisc add dev eth0 root handle 1: tbf rate 40mbit burst 40mbit latency 40ms; tc qdisc add dev eth0 parent 1:1 handle 10: netem delay 40ms
