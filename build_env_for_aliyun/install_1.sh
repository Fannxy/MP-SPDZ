#!/bin/bash

apt update
DEBIAN_FRONTEND=noninteractive apt install -y build-essential ocaml ocamlbuild automake autoconf libtool wget python-is-python3 libssl-dev git cmake perl docker.io
DEBIAN_FRONTEND=noninteractive apt install -y libssl-dev libcurl4-openssl-dev protobuf-compiler libprotobuf-dev debhelper cmake reprepro unzip pkgconf libboost-dev libboost-system-dev libboost-thread-dev lsb-release libsystemd0
DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends ca-certificates gnupg2 jq make gdb wget libfuse-dev libtool tzdata rsync dkms
apt install -y --install-recommends linux-generic-hwe-20.04
