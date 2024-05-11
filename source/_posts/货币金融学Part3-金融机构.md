---
title: 货币金融学Part3-金融机构
urlname: 0zle2w
comments: true
mathjax: true
date: 2023-04-21 22:19:00
categories:
- 金融
tags:
- 金融
description: 学习经典教材货币金融学所做的读书笔记，作者Mishkins。第三部分：Financial Institutions

---

## 第八章: An economic analysis of financial structure

这一章主要讲了金融中的结构, 一个非常重要的特征是直接融资的重要性小于间接融资. 在金融机构中, 金融中介的重要性非常大. 信息不对称会导致逆向选择和道德风险, 这章也介绍了这些带来的问题和如何解决这些问题.

### 8.1 Basic facts about financial structure 

主要讲了间接融资(Indirect Finance)和金融中介(Financial Intermediates)的重要性

### 8.2 Transaction costs

金融中介(Financial Intermediates)的一个巨大作用是降低交易成本(Transaction costs), 让更多人可以参与进金融市场.

### 8.3~8.6 Asymmetric Information

Asymmetric Information(信息不对称)会导致:

1. Adverse selection
   1. 发生交易(如借贷, 买卖)前, 往往财务越有问题的越会来进行借款. 而出借方由于担心对方的信息不透明(比如借钱方刻意隐瞒真实情况)而使得交易不能发生, 使得市场功能失灵.
   2. 解决办法有: 信息中介机构(如标普公司等), 政府干预(督促公司信息透明, 披露详尽)
   3. 解决办法还有金融中介: 比如二手车交易市场的二手车平台, 借贷市场中的银行
2. Moral hazard
   1. 指交易后, 一方做出违背交易约定的事情(比如拿信用贷炒股)
   2. 股票中: 大股东不管理公司, 那么公司的管理者可能会中饱私囊或者干活划水
      1. 解决方法有: 增加监督(效果有限), 政府干预(制定强监管)
      2. 解决办法还有金融中介: 如风投(venture-capital firm)和私募股权公司(private-equity firm), 他们投资一些一级市场的公司股权, 同时起到监督作用
   3. 债券(或债务)中: 借债一方可能拿借的钱去做高风险的事情
      1. 解决办法有: 抵押物和公司的高净资产, 制定限制性的合约
      2. 解决办法还有金融中介: 银行

## 第九章: Banking and the management of financial institutions

这一章主要讲了银行的经营, 冰哥的书里要详细得多。

### 9.1 The Bank Balence Sheet

资产 = 负债 + 资本

total assets = total liabilities + capital

1. 负债(没什么特殊的不列了)

2. 资产(列一些重要的)

   1. reserves and cash items 

      存放在美联储的准备金以及银行本身的现金(是真正的现金)

      其中required reserve ratio是准备金率

   2. securities

      全部是债券, 不允许持有股票

      其中例如短期国债可以被视为secondary reserves(次级准备金)


### 9.2 Basic Banking

讲了一些基础概念

### 9.3 General Principals

讲了流动性管理、准备金、资产管理、负债管理，资本比例管理，其中资本比例相关的最重要

$ROE=ROA\times EM$

$EM=\frac{总资产}{资本}$

 当ROA不变时，EM越高，ROE越高，所以银行需要权衡资本充足率与ROE之间的平衡

如何提升EM或者降低EM?

提升EM, 即降低资本比例, 方法有三: 1. 回购股票 2. 提升分红 3. 扩表

降低EM, 即提升资本比例, 方法也有三: 1. 发行股票 2. 降低分红 3. 缩表

### 9.4 Managing Credit Risk

管理Credit Risk: 主要是做好调查、维护好长期客户关系, 做好信贷配给

### 9.5 Managing Interest Rate Risk

利率上升, 资产的久期比负债的久期短会更受益. 利率下降则相反.

这里面又个Macaulay’s duration看不懂, 以后再说吧, 感觉也不重要.

### 9.6 Off-balance-sheet activities

银行的表外业务包括: 

1. 贷款出售

2. 手续费收入

3. 交易行为

   交易行为通常风险较高，VaR(Value at Risk)是一个衡量交易风险的数值

## 第十章: Econimoc Analysis of Financial Regulation

这一章讲两块独立的内容。首先讲了政府提供的金融安全保护机制会导致信息不对称，反而引起一系列的金融风险。然后讲了八种监管手段。

### 10.1 Asymmetric Information

Government safety net

根本原因: 信息不对称, 银行用户不知道银行存在的风险, 导致危机下容易造成挤兑

措施:

- deposit insurance 存款保险
- government support 政府援助

副作用:

- 银行的经营有恃无恐, 风险更高
- 大而不能倒, 政府不会让大机构破产, 往往会进行注资重组并购, 更使得大额存款也有恃无恐

### 10.2 Types of financial regulation

讲了8种金融监管手段

1. 资产种类限制: 比如限制银行持有股票（重要）
2. 资本要求: 主要限制杠杆率，涉及到巴塞尔协议（I、II、III）（重要）
3. Prompt corrective action 采取纠正行为，如资本金不足则要求整改
4. 金融牌照的发放与金融检查
5. Assessment of risk management 对管理层风控能力的考察
6. 信息披露
7. 消费者保护
8. 竞争限制

## 第十一章: Banking Industry: Structure and Competition

### 11.1 Historical development of the banking system

讲了美国银行业的历史，读过就OK了

### 11.2 Financial innovation and the growth of the "shadow banking system"

讲了历史上的金融创新，其中包括影子银行系统（主要是资产证券化）

- Adjustable-rate mortgage 可调利率房贷
- Financial derivatives 金融衍生品
- Bank Credit and Debit Cards 信用卡和借记卡
- Electronic Banking 指ATM、手机APP等非人工柜台
- Junk bonds and commercial paper 信息化的进步使得这类市场也发展迅速（垃圾债+短期商业票据市场）
- Shadow Banking System 影子银行系统，非银金融机构们，主要做资产证券化（securitization）
- Subprime mortgage market 次级房贷，就是上面的影子银行系统搞的
- Money market mutual funds 货币基金，避免用户的钱作为存款被要求存款准备金，而且利率高于活期
-  Sweep accounts 对公账户的，也可以让公司的钱投资一些短期证券，同时减少存款准备金

此外讲了传统银行经营的经营变化

- 负债端：信用成本上升，用户存款比例下降
- 资产端：竞争力下降，因为上面的那些金融创新抢占了银行的传统信贷市场
- 银行的应对：配置更高风险的资产，扩大表外业务，做影子银行系统的工作等等

### 11.3 

