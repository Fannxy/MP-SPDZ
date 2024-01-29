#!/bin/bash

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
apt-get install -y automake build-essential clang cmake git libboost-dev libboost-thread-dev libgmp-dev libntl-dev libsodium-dev libssl-dev libtool python3
apt-get install -y libboost-iostreams-dev libboost-filesystem-dev
pip install scikit-learn
git clone git@github.com:Fannxy/MP-SPDZ.git
cd MP-SPDZ
for i in `git branch -r`; do git checkout `basename $i` && git reset --hard && git pull --all; done
git checkout --recurse-submodules mpc-tee
make setup
make -j8
make hemi-offline.x
make semi-offline.x
make semi2k-offline.x
cd ..        
