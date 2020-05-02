---
title: 决策树RF与GBDT
urlname: 5h5youv9
comments: true
mathjax: true
date: 2020-04-29 23:55:00
categories:
- 算法
tags:
- 算法
description: 决策树的原理，随机森林与梯度提升决策树的原理与区别
---

# 1. 决策树

### 1.1 划分规则

1. 信息熵

   $$H(y)=\sum_y{-p(y)logp(y)}$$

2. 数据集$D$的经验熵

   $$H(D)=-\sum_{k=1}^K{\frac{N_K}{N}log{\frac{N_K}{N}}}$$

   其中：数据集共有K类，每一类有$N_K$个样本

   这个经验熵可以理解成数据集D的先验知识，越大代表信息量越大，分类越分散。

3. 特征A在数据集D上的经验熵

   $$H_A(D)=-\sum_{i=1}^{n_A}\frac{N_{a_i}}{N}log\frac{N_{a_i}}{N}$$

   它反应的是D中样本在A上的分布情况

4. 数据集D对于特征A的经验条件熵为：
   $$
   H(D|A)=\sum_{i=1}^{n_A}p(A=a_i)H(y|A=a_i) \\
   =\sum_{i=1}^{n_A}\frac{N_{a_i}}{N}[-\sum_{k=1}^{K}\frac{N_{a_i,k}}{N_{a_i}}log\frac{N_{a_i,k}}{N_{a_i}}]
   $$
   其中$n_A$为条件A的不同取值数量，K为类别数量，这个反应了条件A对数据集D的区分程度，越大代表条件A的区分度越高。

5. 信息增益

   $$g(D,A)=H(D)-H(D|A)$$

   越高越好，代表了条件A带来的对数据集分类的不确定性的改善

6. 信息增益比

   $$g_R(D,A)=\frac{g(D,A)}{H_A(D)}$$

   它是修正了信息增益倾向于可选特征值较多的特征的问题

### 1.2 生成算法

1. ID3: 使用信息增益
2. C4.5: 使用信息增益比

### 1.3 其他

如剪枝，缺失值处理，CART树等等

# 2. 随机森林

1. 使用bootstrap sampling，有放回地进行采样
2. 每一颗树都是用部分的特征进行学习

# 3. GBDT

### 1.1 GBDT

1. 加法模型

   GBDT可以看成是由K棵树组成的加法模型
   $$
   y=f_K(\vec{x})=\sum_{k=1}^{K}h_k(\vec{x})
   $$


2. 学习过程
   $$
   f_0(\vec{x})=0 \\
   f_1(\vec{x})=f_0(\vec{x})+h_1(\vec{x}) \\
   f_k(\vec{x})=f_{k-1}(\vec{x})+h_k(\vec{x})
   $$


3. 单颗树学习目标

   假设损失函数为
   $$
   L(\hat{y},f(\vec{x}))
   $$
   利用泰勒公式
   $$
   f(x+\Delta{x})\approx{f(x)+f'(x)\Delta{x}+\frac{1}{2}}f''(x)(\Delta{x})^2
   $$
   舍去二次项，那么
   $$
   L(\hat{y},f_k(\vec{x}))
   =L(\hat{y},f_{k-1}(\vec{x})+h_k(\vec{x}))
   \approx{L(\hat{y},f_{k-1}(\vec{x}))}+\frac{\partial{L(\hat{y},f_{k-1}(\vec{x}))}}{f_{k-1}(\vec{x})}h_k(\vec{x})
   $$
   这里是把$f_{k-1}(\vec{x})$看成了泰勒公式中的$x$，$h_k(\vec{x})$看成了$\Delta{x}$

   我们新学习一棵树，是为了让$L$更小，也就是${L(\hat{y},f_{k}(\vec{x}))}<{L(\hat{y},f_{k-1}(\vec{x}))}$，那么就需要让$\frac{\partial{L(\hat{y},f_{k-1}(\vec{x}))}}{f_{k-1}(\vec{x})}h_k(\vec{x})<0$，因此新的树的学习目标可以设置为
   $$
   h_k(\vec{x})=-\frac{\partial{L(\hat{y},f_{k-1}(\vec{x}))}}{f_{k-1}(\vec{x})}
   $$

4. 学习率

   在实际学习中，会加入一个学习率$\nu$，使得整个学习稳得一逼
   $$
   f_k(\vec{x})=f_{k-1}(\vec{x})+{\nu}h_k(\vec{x})
   $$


### 1.2 xgboost

与上面的GBDT有两个区别

1. 在计算loss的近似的时候使用到了泰勒展开中的二阶导
2. 加入了正则项

### 1.3 LightGBM

相比于xgboost，计算效率更高，并行化更好，准确率更高