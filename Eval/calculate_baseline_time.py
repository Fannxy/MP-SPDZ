#!/usr/bin/env python3
"""
根据函数的操作次数和操作时间，计算baseline的估计时间
"""
import json
import sys
import os

def calculate_baseline_time(func_name, operation_timings_file, operation_counts_file, N):
    """
    计算baseline的估计时间
    
    Args:
        func_name: 函数名称
        operation_timings_file: 操作时间文件路径
        operation_counts_file: 操作计数文件路径
        N: 输入数据数量
    
    Returns:
        估计的总时间（秒）
    """
    # 加载操作时间
    with open(operation_timings_file, 'r') as f:
        operation_timings = json.load(f)
    
    # 加载操作计数
    with open(operation_counts_file, 'r') as f:
        operation_counts = json.load(f)
    
    if func_name not in operation_counts:
        raise ValueError(f"函数 {func_name} 不在操作计数文件中")
    
    counts = operation_counts[func_name]
    
    # 计算总时间
    total_time = 0.0
    
    for op, count in counts.items():
        if op in operation_timings and operation_timings[op] is not None:
            # 每个操作的时间 * 操作次数 * 输入数据数量
            total_time += operation_timings[op] * count * N
        else:
            print(f"Warning: 操作 {op} 的时间未找到，跳过", file=sys.stderr)
    
    return total_time

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python calculate_baseline_time.py <func_name> <operation_timings_file> <operation_counts_file> <N>")
        sys.exit(1)
    
    func_name = sys.argv[1]
    operation_timings_file = sys.argv[2]
    operation_counts_file = sys.argv[3]
    N = int(sys.argv[4])
    
    try:
        baseline_time = calculate_baseline_time(func_name, operation_timings_file, operation_counts_file, N)
        print(f"{baseline_time:.6f}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

