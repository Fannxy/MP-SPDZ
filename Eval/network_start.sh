# set up the ssh configurations - pre-config 4 hosts.
ssh_config_content=$(cat <<EOF

Host h1
        HostName 10.0.0.11
        User root
        Port 22

Host h2
        HostName 10.0.0.12
        User root
        Port 22

Host h3
        HostName 10.0.0.13
        User root
        Port 22

Host h4
        HostName 10.0.0.14
        User root
        Port 22

EOF
)

# echo "$ssh_config_content" >> ~/.ssh/config

# echo ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# 检查 ~/.ssh/config 是否包含这些配置
if ! grep -q "Host h1" ~/.ssh/config; then
    echo "$ssh_config_content" >> ~/.ssh/config
    echo "SSH configurations have been added to ~/.ssh/config"
else
    echo "SSH configurations already exist in ~/.ssh/config"
fi

# 检查并追加公钥到 authorized_keys
if ! grep -q "$(cat ~/.ssh/id_rsa.pub)" ~/.ssh/authorized_keys; then
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    echo "Public key has been added to ~/.ssh/authorized_keys"
else
    echo "Public key already exists in ~/.ssh/authorized_keys"
fi

# obtain the ip address of the current machine
ip_address=$(ifconfig ens121f0 | grep 'inet ' | awk '{print $2}')

# setup the bandwidth and latency.
bandwidth=100 # in Mbps
latency=1ms # in ms

# Start the network with specified bandwidth and latency
./Eval/network_setup.sh ${bandwidth} ${bandwidth} ${bandwidth} ${latency} ${latency} ${latency} ${ip_address}

echo "Network started with bandwidth: ${bandwidth}Mbps and latency: ${latency}ms, you can login the hosts through ssh h1, ssh h2, ssh h3"


