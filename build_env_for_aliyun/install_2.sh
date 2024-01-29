#!/bin/bash

mkdir -p /dev/sgx
ln -sf ../sgx_enclave /dev/sgx/enclave
ln -sf ../sgx_provision /dev/sgx/provision

echo 'deb [arch=amd64] https://download.01.org/intel-sgx/sgx_repo/ubuntu focal main' | sudo tee /etc/apt/sources.list.d/intel-sgx.list
wget -qO - https://download.01.org/intel-sgx/sgx_repo/ubuntu/intel-sgx-deb.key | sudo apt-key add
apt update
DEBIAN_FRONTEND=noninteractive apt install -y libsgx-epid libsgx-quote-ex libsgx-dcap-ql
DEBIAN_FRONTEND=noninteractive apt install -y libsgx-urts-dbgsym libsgx-enclave-common-dbgsym libsgx-dcap-ql-dbgsym libsgx-dcap-default-qpl-dbgsym
DEBIAN_FRONTEND=noninteractive apt install -y libsgx-enclave-common-dev libsgx-dcap-ql-dev libsgx-dcap-default-qpl-dev
DEBIAN_FRONTEND=noninteractive apt install -y libsgx-dcap-ql libsgx-epid libsgx-urts libsgx-quote-ex libsgx-uae-service libsgx-dcap-quote-verify-dev
wget https://download.01.org/intel-sgx/sgx-linux/2.22/distro/ubuntu20.04-server/sgx_linux_x64_sdk_2.22.100.3.bin
chmod +x sgx_linux_x64_sdk_2.22.100.3.bin

docker run -it --net=host --device /dev/sgx/enclave --device /dev/sgx/provision occlum/occlum:0.30.0-ubuntu20.04
