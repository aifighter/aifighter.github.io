---
title: LogLoss与最大似然估计
urlname: 36lw4rkt
comments: true
mathjax: true
date: 2020-04-08 20:50:00
categories:
- 算法
tags:
- 算法
description: 经典的交叉熵损失函数或对数损失函数的来源
---

> Log Loss来源于最大似然估计

### 问题

给定数据集$\mathcal{D}=\{(\vec{x_1}, y_1),(\vec{x_2}, y_2)...(\vec{x_N}, y_N)\}$

### 最大似然

假设模型给出的预测为$p(y_i|\vec{x_i})$，那么训练集的出现概率为$\prod{p(y_i|\vec{x_i})}$

最大似然就是要让训练集出现的概率最大那么相当于：
$$
max\prod{p(y_i|\vec{x_i})}
\rightarrow
{max\sum{log(p(y_i|\vec{x_i}))}}
\rightarrow
{min\sum{-log(p(y_i|\vec{x_i}))}} \\
\rightarrow
\frac{1}{N}{min\sum{-log(p(y_i|\vec{x_i}))}}
$$

### 对数损失函数

从上面就可以看到实际上在优化的损失函数就是下式，其中$\tilde{y}$是标签，$\hat{y}$是预测值
$$
L(\tilde{y}, \hat{y})=-log(p(\tilde{y}|\vec{x}))
$$

### 二分类

当$\tilde{y}=1$时，$p(\tilde{y}|\vec{x})=\hat{y}$

当$\tilde{y}=0$时，$p(\tilde{y}|\vec{x})=1-\hat{y}$

因此综合的损失函数，Binary Crossentropy为
$$
L(\tilde{y}, \hat{y})=-\tilde{y}log(\hat{y})-(1-\tilde{y})log(1-\hat{y})
$$
