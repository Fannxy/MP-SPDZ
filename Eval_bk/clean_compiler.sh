
bc_folder=/Programs/Bytecode/
schedule_folder=/Programs/Schedules/

rm -r .$bc_folder*
rm -r .$schedule_folder*

ssh spdz1 "rm -r ./MP-SPDZ$bc_folder*"
ssh spdz2 "rm -r ./MP-SPDZ$bc_folder*"
ssh spdz1 "rm -r ./MP-SPDZ$schedule_folder*"
ssh spdz2 "rm -r ./MP-SPDZ$schedule_folder*"