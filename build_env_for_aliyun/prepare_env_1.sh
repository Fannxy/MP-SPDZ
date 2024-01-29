#!/bin/bash

apt update
apt install -y ssh net-tools iputils-ping
sed -i "s/#PubkeyAuthentication/PubkeyAuthentication/g" /etc/ssh/sshd_config
sed -i "s/#PermitRootLogin/PermitRootLogin/g" /etc/ssh/sshd_config
sed -i "s/#AuthorizedKeysFile/AuthorizedKeysFile/g" /etc/ssh/sshd_config
service ssh restart
mkdir .ssh
chmod 700 .ssh
ssh-keygen -t ed25519
echo "Add the public key to github"
