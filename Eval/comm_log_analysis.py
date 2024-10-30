import os
import re
import pandas as pd
import argparse

MAIN_FOLDER = "/root/RoundRole/MP-SPDZ/"
log_prefix = "log-"
record_folder = MAIN_FOLDER + "Record/"
result_folder = MAIN_FOLDER + "Results/"


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=str, default="replicated-ring-party.x", help="target graph format")
    
    args = parser.parse_args()
    protocol = args.protocol
    print("analyzing protocol = " + protocol)

    # mkdir result_folder if not exists
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # raise error if record_folder does not exist
    if not os.path.exists(record_folder):
        raise FileNotFoundError("Record folder does not exist")

    log_separator_pattern = re.compile(r'==================== (.+) ====================')
    data_sent_pattern = re.compile(r'Data sent = ([\d.]+) MB in ~\d+ rounds \(party (\d+).*\)')
    log_file_pattern = re.compile(rf'log-{protocol}-(.+)$')

    results = []

    for log_file in os.listdir(record_folder):
        
        log_file_pattern_match = log_file_pattern.match(log_file)
        if log_file_pattern_match and len(log_file_pattern_match.groups()) == 1:
            function = log_file_pattern_match.group(1)
        else:
            print("Skipping file: " + log_file)
            continue
        
        res_tmp = {
            "function": function,
        }
        
        if log_file.startswith(log_prefix):
            log_path = os.path.join(record_folder, log_file)
            with open(log_path, 'r') as log:
                for line in log:
                    log_separator_match = log_separator_pattern.match(line)
                    if log_separator_match:
                        party = log_separator_match.group(1)
                    data_sent_match = data_sent_pattern.match(line)
                    if data_sent_match:
                        data_sent = float(data_sent_match.group(1))
                        party = int(data_sent_match.group(2))
                        res_tmp[f"party{party}-send"] = data_sent
        
        results.append(res_tmp)

    df = pd.DataFrame(results)
    df = df.sort_values(by="function")
    df.to_excel(f"./Results/{protocol}_comm_log_analysis.xlsx", index=False)