#!/usr/bin/env python3
"""
解析操作时间日志文件，提取各种操作的平均时间
"""
import re
import json
import sys
import os

def parse_timer_output(log_file):
    """
    从MP-SPDZ的日志文件中解析Timer输出
    返回时间（秒）
    """
    if not os.path.exists(log_file):
        return None
    
    timer_pattern = r'Timer\s+1:\s+([\d.]+)\s+seconds'
    
    with open(log_file, 'r') as f:
        content = f.read()
        matches = re.findall(timer_pattern, content)
        if matches:
            # 取最后一个匹配（通常是最终结果）
            return float(matches[-1])
    
    return None

def extract_operation_timings(protocol, network, N):
    """
    从日志文件中提取各种操作的时间
    """
    base_dir = f"/root/llm-project/NFGen+KAN/Results/{protocol}/{network}/operation_timings/"
    log_dir = base_dir
    
    operations = ["add", "sub", "mult", "div", "pow", "sqrt", "exp", "log", "sin", "cos", "compare", "if_else"]
    timings = {}
    
    for op in operations:
        log_file = f"{log_dir}operation_execution_log_{op}.log"
        time = parse_timer_output(log_file)
        if time is not None:
            # 除以N得到单次操作的平均时间
            timings[op] = time / N
        else:
            print(f"Warning: 无法解析 {op} 的时间", file=sys.stderr)
            timings[op] = None
    
    return timings

def save_timings_json(timings, output_file):
    """
    保存时间数据到JSON文件
    """
    with open(output_file, 'w') as f:
        json.dump(timings, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python parse_operation_timings.py <protocol> <network> <N> [output_file]")
        sys.exit(1)
    
    protocol = sys.argv[1]
    network = sys.argv[2]
    N = int(sys.argv[3])
    output_file = sys.argv[4] if len(sys.argv) > 4 else f"/root/llm-project/NFGen+KAN/Results/{protocol}/{network}/operation_timings.json"
    
    timings = extract_operation_timings(protocol, network, N)
    save_timings_json(timings, output_file)
    
    print(f"操作时间已保存到: {output_file}")
    print(json.dumps(timings, indent=2))

