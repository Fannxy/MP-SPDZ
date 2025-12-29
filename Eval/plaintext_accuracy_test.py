#!/usr/bin/env python3
"""
明文准确率测试脚本
使用 MP-SPDZ 的算法逻辑（明文版本）计算adult和breast_cancer数据集的准确率
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os
import sys

# 导入明文版本的实现
sys.path.insert(0, os.path.dirname(__file__))
from plaintext_ml import PlaintextTreeClassifier, PlaintextSGDLogistic, preprocess_pandas

# 设置路径
MP_SPDZ_DIR = '/root/llm-project/NFGen+KAN/MP-SPDZ/'
RESULTS_DIR = '/root/llm-project/NFGen+KAN/Results/plaintext/accuracy/'

def test_adult():
    """测试adult数据集（决策树）"""
    print("=" * 60)
    print("Testing Adult dataset (Decision Tree)")
    print("=" * 60)
    
    # 加载数据
    dataset_path = '/root/llm-project/NFGen+KAN/data/adult-all.csv'
    if not os.path.exists(dataset_path):
        print(f"Warning: Dataset not found at {dataset_path}")
        print("Downloading from URL...")
        dataset_path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/adult-all.csv'
    
    data = pd.read_csv(dataset_path, header=None)
    
    # 使用 MP-SPDZ 的 preprocess_pandas 进行预处理（与easy_adult.mpc保持一致）
    data_processed, attr_types = preprocess_pandas(data)
    
    # label是最后一列
    X = data_processed[:, :-1]
    y = data_processed[:, -1].astype(int)
    
    # 分割数据
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    print(f"Features: {X_train.shape[1]}")
    
    # 使用明文版本的决策树（max_depth=10，与easy_adult.mpc一致）
    tree = PlaintextTreeClassifier(max_depth=10, random_state=0)
    tree.fit(X_train, y_train, attr_types=attr_types[:-1])  # 排除 label 列
    
    # 预测
    y_pred = tree.predict(X_test)
    
    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # 保存结果
    os.makedirs(RESULTS_DIR, exist_ok=True)
    result_file = os.path.join(RESULTS_DIR, 'adult_accuracy.txt')
    with open(result_file, 'w') as f:
        f.write(f"Adult Dataset - Decision Tree\n")
        f.write(f"Accuracy: {accuracy:.4f}\n\n")
        f.write("Classification Report:\n")
        f.write(classification_report(y_test, y_pred))
    
    print(f"\nResults saved to {result_file}")
    return accuracy

def test_breast_cancer_tree():
    """测试breast_cancer数据集（决策树）"""
    print("\n" + "=" * 60)
    print("Testing Breast Cancer dataset (Decision Tree)")
    print("=" * 60)
    
    from sklearn.datasets import load_breast_cancer
    
    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    print(f"Features: {X_train.shape[1]}")
    
    # 使用明文版本的决策树（max_depth=5，与breast_tree.mpc一致）
    tree = PlaintextTreeClassifier(max_depth=5, random_state=0)
    tree.fit(X_train, y_train)
    
    # 预测
    y_pred = tree.predict(X_test)
    
    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # 保存结果
    os.makedirs(RESULTS_DIR, exist_ok=True)
    result_file = os.path.join(RESULTS_DIR, 'breast_cancer_tree_accuracy.txt')
    with open(result_file, 'w') as f:
        f.write(f"Breast Cancer Dataset - Decision Tree\n")
        f.write(f"Accuracy: {accuracy:.4f}\n\n")
        f.write("Classification Report:\n")
        f.write(classification_report(y_test, y_pred))
    
    print(f"\nResults saved to {result_file}")
    return accuracy

def test_breast_cancer_logistic():
    """测试breast_cancer数据集（逻辑回归）"""
    print("\n" + "=" * 60)
    print("Testing Breast Cancer dataset (Logistic Regression)")
    print("=" * 60)
    
    from sklearn.datasets import load_breast_cancer
    
    X, y = load_breast_cancer(return_X_y=True)
    
    # 归一化（与breast_logistic.mpc一致）
    X = X / X.max(axis=0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    print(f"Features: {X_train.shape[1]}")
    
    # 使用明文版本的逻辑回归（20 epochs，batch_size=2，与breast_logistic.mpc一致）
    log_reg = PlaintextSGDLogistic(n_epochs=20, batch_size=2, random_state=0)
    log_reg.fit(X_train, y_train)
    
    # 预测
    y_pred = log_reg.predict(X_test)
    
    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # 保存结果
    os.makedirs(RESULTS_DIR, exist_ok=True)
    result_file = os.path.join(RESULTS_DIR, 'breast_cancer_logistic_accuracy.txt')
    with open(result_file, 'w') as f:
        f.write(f"Breast Cancer Dataset - Logistic Regression\n")
        f.write(f"Accuracy: {accuracy:.4f}\n\n")
        f.write("Classification Report:\n")
        f.write(classification_report(y_test, y_pred))
    
    print(f"\nResults saved to {result_file}")
    return accuracy

def main():
    """主函数"""
    print("Plaintext Accuracy Test")
    print("=" * 60)
    
    results = {}
    
    # 测试adult数据集
    try:
        results['adult'] = test_adult()
    except Exception as e:
        print(f"Error testing adult dataset: {e}")
        import traceback
        traceback.print_exc()
    
    # 测试breast_cancer决策树
    try:
        results['breast_cancer_tree'] = test_breast_cancer_tree()
    except Exception as e:
        print(f"Error testing breast_cancer tree: {e}")
        import traceback
        traceback.print_exc()
    
    # 测试breast_cancer逻辑回归
    try:
        results['breast_cancer_logistic'] = test_breast_cancer_logistic()
    except Exception as e:
        print(f"Error testing breast_cancer logistic: {e}")
        import traceback
        traceback.print_exc()
    
    # 总结
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    for name, acc in results.items():
        print(f"{name}: {acc:.4f}")
    
    # 保存总结
    summary_file = os.path.join(RESULTS_DIR, 'summary.txt')
    with open(summary_file, 'w') as f:
        f.write("Plaintext Accuracy Test Summary\n")
        f.write("=" * 60 + "\n")
        for name, acc in results.items():
            f.write(f"{name}: {acc:.4f}\n")
    
    print(f"\nSummary saved to {summary_file}")

if __name__ == '__main__':
    main()

