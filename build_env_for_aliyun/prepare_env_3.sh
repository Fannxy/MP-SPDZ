#!/bin/bash

mkdir -p /Programs
mkdir -p /Player-Data

# need to change the HOST if necessary
cp MP-SPDZ/HOST /HOST
# need to compile all programs before the copy
rm -r /Programs
cp -r MP-SPDZ/Programs /
# need to generate all input and ssl keys/certs before the copy
rm -r /Player-Data
cp -r MP-SPDZ/Player-Data /
cd MP-SPDZ
mkdir occlum_workspace && cd occlum_workspace
occlum init && rm -rf image
copy_bom -f ../hello.yaml --root image --include-dir /opt/occlum/etc/template
cp ../HOST image/
cp -r ../Programs image/
cp -r ../Player-Data image/
sed -i "s/\"kernel_space_heap_size\": \"32MB\",/\"kernel_space_heap_size\": \"128MB\",/g" Occlum.json
sed -i "s/\"kernel_space_stack_size\": \"1MB\",/\"kernel_space_stack_size\": \"32MB\",/g" Occlum.json
sed -i "s/\"user_space_size\": \"300MB\",/\"user_space_size\": \"16GB\",/g" Occlum.json
sed -i "s/\"max_num_of_threads\": 32/\"max_num_of_threads\": 1024/g" Occlum.json
sed -i "s/\"default_stack_size\": \"4MB\",/\"default_stack_size\": \"8MB\",/g" Occlum.json
sed -i "s/\"default_heap_size\": \"32MB\",/\"default_heap_size\": \"64MB\",/g" Occlum.json
sed -i "s/\"default_mmap_size\": \"100MB\"/\"default_mmap_size\": \"256MB\"/g" Occlum.json
sed -i "s/\"debuggable\": true,/\"debuggable\": false,/g" Occlum.json
echo -e "nameserver 8.8.8.8\nnameserver 8.8.4.4" > image/etc/resolv.conf
echo -e "hosts: files dns" > image/etc/nsswitch.conf
#mkdir -p image/root/MP-SPDZ/local/lib
#cp ../libFHE.so image/root/MP-SPDZ/ 
#cp ../libSPDZ.so image/root/MP-SPDZ/
#cp ../local/lib/libboost_filesystem.so.1.83.0 image/root/MP-SPDZ/local/lib/
#cp ../local/lib/libboost_iostreams.so.1.83.0 image/root/MP-SPDZ/local/lib/
cp /lib/x86_64-linux-gnu/{libnss_dns.so.2,libnss_files.so.2,libresolv.so.2} image/opt/occlum/glibc/lib

occlum build
echo "next step: run!"
