#!/usr/bin/env python3
"""
明文版本的机器学习算法实现
基于 MP-SPDZ 的 decision_tree.py 和 ml.py 中的算法逻辑
使用 numpy/pandas 数据类型而不是 MPC 类型
"""
import numpy as np
import pandas as pd


def preprocess_pandas(data):
    """预处理 pandas DataFrame，与 MP-SPDZ 的 decision_tree.preprocess_pandas 保持一致
    
    :returns: 处理后的数据和类型列表
    """
    res = []
    types = []
    for i, t in enumerate(data.dtypes):
        if pd.api.types.is_int64_dtype(t):
            res.append(data.iloc[:, i].to_numpy())
            types.append('c')
        elif pd.api.types.is_object_dtype(t):
            values = list(filter(lambda x: isinstance(x, str),
                                 list(data.iloc[:, i].unique())))
            print('converting the following to unary:', values)
            if len(values) == 2:
                res.append((data.iloc[:, i].to_numpy() == values[1]).astype(float))
                types.append('b')
            else:
                for value in values:
                    res.append((data.iloc[:, i].to_numpy() == value).astype(float))
                    types.append('b')
        else:
            raise ValueError('unknown pandas type: ' + str(t))
    res = np.array(res)
    res = np.swapaxes(res, 0, 1)
    return res, types


class PlaintextTreeClassifier:
    """明文版本的决策树分类器
    基于 MP-SPDZ 的 TreeClassifier 算法逻辑
    """
    
    def __init__(self, max_depth, random_state=0):
        self.max_depth = max_depth
        self.random_state = random_state
        self.tree = None
        
    def fit(self, X, y, attr_types=None):
        """训练决策树
        
        :param X: 训练数据 (numpy array, 行是样本)
        :param y: 训练标签 (numpy array, 二进制标签)
        :param attr_types: 属性类型列表 ('c' 表示连续, 'b' 表示二进制)
                          注意：sklearn 的 DecisionTreeClassifier 会自动处理连续和分类特征
        """
        from sklearn.tree import DecisionTreeClassifier
        
        # 使用 sklearn 的 DecisionTreeClassifier，但设置相同的参数
        # 注意：sklearn 使用 CART 算法，与 MP-SPDZ 的算法可能略有不同
        # 但为了保持一致性，我们使用相同的 max_depth 和 Gini 不纯度
        # MP-SPDZ 使用 ModifiedGini，sklearn 使用标准 Gini，两者类似
        self.tree = DecisionTreeClassifier(
            max_depth=self.max_depth,
            random_state=self.random_state,
            criterion='gini'  # 使用 Gini 不纯度，与 MP-SPDZ 的 ModifiedGini 类似
        )
        self.tree.fit(X, y)
        self.attr_types = attr_types  # 保存属性类型以供参考
        
    def predict(self, X):
        """预测
        
        :param X: 测试数据 (numpy array, 行是样本)
        :returns: 预测标签 (numpy array)
        """
        return self.tree.predict(X)


class PlaintextSGDLogistic:
    """明文版本的逻辑回归分类器
    基于 MP-SPDZ 的 SGDLogistic 算法逻辑
    使用 SGD 优化器，20 epochs，batch_size=2，学习率 0.01（与 MP-SPDZ 的 SGD 默认值一致）
    """
    
    def __init__(self, n_epochs=20, batch_size=2, learning_rate=0.01, random_state=0):
        self.n_epochs = n_epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.weights = None
        self.bias = None
        
    def _sigmoid(self, x):
        """Sigmoid 函数"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
        
    def fit(self, X_train, y_train):
        """训练逻辑回归模型
        
        :param X_train: 训练数据 (numpy array, 行是样本)
        :param y_train: 训练标签 (numpy array, 二进制标签)
        """
        np.random.seed(self.random_state)
        
        n_samples, n_features = X_train.shape
        
        # 初始化权重和偏置
        self.weights = np.random.randn(n_features) * 0.01
        self.bias = 0.0
        
        # SGD 训练
        for epoch in range(self.n_epochs):
            # 随机打乱数据
            indices = np.random.permutation(n_samples)
            X_shuffled = X_train[indices]
            y_shuffled = y_train[indices]
            
            # 批量训练
            for i in range(0, n_samples, self.batch_size):
                X_batch = X_shuffled[i:i+self.batch_size]
                y_batch = y_shuffled[i:i+self.batch_size]
                
                # 前向传播
                z = np.dot(X_batch, self.weights) + self.bias
                predictions = self._sigmoid(z)
                
                # 计算梯度
                error = predictions - y_batch
                grad_weights = np.dot(X_batch.T, error) / len(X_batch)
                grad_bias = np.mean(error)
                
                # 更新权重
                self.weights -= self.learning_rate * grad_weights
                self.bias -= self.learning_rate * grad_bias
                
    def predict_proba(self, X):
        """预测概率
        
        :param X: 测试数据 (numpy array, 行是样本)
        :returns: 预测概率 (numpy array)
        """
        z = np.dot(X, self.weights) + self.bias
        return self._sigmoid(z)
        
    def predict(self, X):
        """预测标签
        
        :param X: 测试数据 (numpy array, 行是样本)
        :returns: 预测标签 (numpy array, 0 或 1)
        """
        proba = self.predict_proba(X)
        return (proba >= 0.5).astype(int)

