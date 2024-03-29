report=$1; process_keyword=$2

nethogs -d 0.5 -t | grep ${process_keyword} >> ${report}