#!/bin/bash
# 运行明文准确率测试脚本

set -e

MP_SPDZ_DIR=/root/llm-project/NFGen+KAN/MP-SPDZ/
cd ${MP_SPDZ_DIR}

echo "Running plaintext accuracy test..."
python3 Eval/plaintext_accuracy_test.py

echo "Plaintext accuracy test completed."
echo "Results are saved in /root/llm-project/NFGen+KAN/Results/plaintext/accuracy/"

