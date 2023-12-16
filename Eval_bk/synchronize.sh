makekey=replicated

ssh spdz1 "cd ./MP-SPDZ/; git pull; make $makekey"
ssh spdz2 "cd ./MP-SPDZ/; git pull; make $makekey"