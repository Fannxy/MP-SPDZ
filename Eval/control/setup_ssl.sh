
./Scripts/setup-ssl.sh;
cd ..
scp -r ./MP-SPDZ/Player-Data spdz1:~/MP-SPDZ/ &
scp -r ./MP-SPDZ/Player-Data spdz2:~/MP-SPDZ/;
wait;

cd ./MP-SPDZ/
c_rehash ./Player-Data
ssh spdz1 "cd ./MP-SPDZ/; c_rehash ./Player-Data" &
ssh spdz2 "cd ./MP-SPDZ/; c_rehash ./Player-Data";
wait;
