---
title: 货币金融学Part2-金融市场
urlname: um3np0
comments: true
mathjax: true
date: 2023-03-30 23:34:00
categories:
- 金融
tags:
- 金融
description: 学习经典教材货币金融学所做的读书笔记，作者Mishkins。第二部分：Financial Markets

---

## 第四章: The meaning of interesting rates

这一章讲了如何计算利率, 最重要的概念是到期年化利率, 另外介绍了四种不同的债券.

还讲了债券到期收益率和实际持有期间收益率的区别, 主要区别在于市场利率的变化导致债券价格的变化.

### 4.1 Measuring interest rates

1. Present Value(现值)

   $PV=\frac{CF}{(1+i)^n}$

   当前价值(present value) = 未来现金流(cash flow)在当前的折现

2. Yield to Maturity

   到期年化收益率

3. Four types of credit market instruments (四种不同债券)

    face value: 到期之后偿还的那个金额(**注意: **face value不一定等于债券的售价)

   1. simple loan(普通贷款)

      到期一次性付清利息+本金

      yield to maturity = interest rate

   2. fixed payment loan (=fully amortized loan) (等额本息贷款)

   3. coupon bond(付息债券)

      - 到期之前每年付利息, 到期之后同时偿还本金

      - 当face value = 售价时, yield to maturity = interest rate

      - 有一种特殊的coupon bond叫做perpetuity(永续债)

        $i_c=\frac{C}{P_c}$

        到期年化收益率 = 每年利息 / 售价

   4. discount bond(折价债券)

      不付利息, 但是售价会比face value低


### 4.2 Interest rates and returns

1. 两个公式

   - $R=\frac{C}{P_t}+\frac{P_{t+1}-P_t}{P_t}$

     $R$: rate of return持有期间的收益率 

     $C$: 持有期间的债券付息

     $P_t$: 购买时的债券价格

     $P_{t+1}$: 出售时的债券价格 

   - $R=i_c+g$

     $i_c$: current yield 即当期债券收益率

     $g$: rate of capital gain 资本收益率

2. 一些结论
   1. 利率上升, 债券价格下降, 久期越长的债券, 价格下降越多
   2. 当持有时间<到期时间时, 市场利率上升, 收益下降

### 4.3 Real and nominal interest rates

1. $i=r+\pi^e$

   $i$: nominal interest rate

   $r$: real interest rate

   $\pi^e$: inflation(expected)

## 第五章: The behavior of interest rates

这一章介绍了利率受哪些因素影响, 使用了两种模型来计算利率, 一种是债券供需模型, 一种是流动性偏好框架.

### 5.1 Determinants of asset demand

1. Wealth(个人的财富), 正相关
2. Expected Return(某个产品的预期收益), 正相关
3. Risk, 负相关
4. Liquidity(流动性), 正相关

### 5.2 Supply and demand in the bond market

[债券供需曲线图](/images/货币金融学/债券供需曲线.jpg)

### 5.3 Changes in equilibrium interest rates(供需均衡利率)

1. 需求改变因素(需求曲线为图中左上到右下)(其他条件不变)

   1. Wealth: 增, 需求增, 曲线右移(手里钱多了, 借出去点)

   2. Expected interest rate: 增, 需求减, 曲线左移

      预计要加息, 那么债券价格将会跌, 我就不想买了=不想借钱出去

      为什么和4.1的Expected Return是反的呢?因为对于长期债券来说, 预期利率的提升会导致收益的下降!

   3. Expected inflation: 增, 需求减, 曲线左移(通胀高了, 实际利率降低, 不想借出去了)

   4. Risk: 增, 需求减, 曲线左移

   5. Liquidity: 增, 需求增, 曲线右移

2. 供给改变因素(供给曲线为图中左下到右上)(其他条件不变)

   1. Expected investment opportunities: 增, 供给增, 曲线右移(机会多了, 多借点)
   2. Expected inflation: 增, 供给增, 曲线右移(通胀一高, 实际利率降了, 那还不多借点)
   3. Government budget deficits: 增, 供给增, 曲线右移(政府赤字, 多借点钱)

3. 实际应用

   1. Fisher Effect: When expected inflation rises, interest rate rises.

      预期通胀高, 供给增加, 需求减少, 债券价格暴跌, 利率上涨

   2. 经济繁荣, 利率上升(这里的结论是模糊的)

      企业更愿意借钱扩张, 供给增加, 手里有钱的人变多, 需求也增加, 但是供给的增加更强, 导致债券价格下跌, 利率上涨

   3. Secular Stagnation(长期停滞)

      社会不进步了, 通胀率也不高, 投资机会也缺乏.

      供给端: 企业不愿意扩张借钱, 导致供给减少, 利率降低

      需求端: 预期通胀降低, 导致需求增多, 利率降低

      因此长期停滞会导致利率降低, 这也是为什么很多发达国家利率很低的原因.

### 5.4&5.5 The liquidity preference framework

1. 流动性偏好框架
   1. 假设只有两种资产, 一种是money, 一种是bond, 且供需都是平衡的.
   2. 由于机会成本, bond的利率越高, money的需求越低.
   3. money的供给完全由the Federal Reserve决定
2. 需求曲线的移动(其他条件不变):
   1. 经济繁荣, 收入增加, money的需求整体增加, 曲线右移, 利率升高 (结论明确)
   2. 物价上涨, money的需求整体增肌, 曲线右移, 利率升高 (和预期通胀略有区别, 物价上涨的影响是永久的)
3. 供给曲线的移动(其他条件不变):
   1. money policy的改变, supply越多, 利率越低

[流动性偏好框架](/images/货币金融学/流动性偏好框架.jpg)

### 5.6 Money and interest rate

1. 在流动性偏好框架下, 货币增加, 利率下降 (这是在其他条件不变时, 然而事实并非如此)
2. 货币增加, 会导致
   1. 物价上涨, 导致利率上升
   2. 收入增加, 导致利率上升
   3. 预期通胀上升, 导致利率上升(和物价上涨有区别, 这个是二阶导)
3. 在实际应用中, 1和2的效应哪个更强是不确定的. 经验上来说, 往往预期通胀的影响最为凶猛, 但也难以预测

## 第六章: The risk and term structure of interest rates

### 5.1 Risk structure

1. default risk: 违约率越高, 利率越高

   risk premium: 风险溢价

2. liquidity: 流动性越低, 利率越高

3. income tax considerations: 免税条款会降低名义利率

   这也是为什么一些state and local government bond的利率会低于国债

### 5.2 Term structure

1. Expectations theory
   1. 假设长期利率就是短期利率期望的平均,
   2. 可以解释为什么在短期利率很低的时候长期利率会高, 短期利率很高的时候长期利率高
   3. 解释不了为什么长期利率在大部分时间高于短期利率(按照假设应该是大致持平的)

2. Segmented Markets Theory
   1. 分离市场理论, 假设短期债券和长期债券处于两个互不相关的市场, 没有替代关系
   2. 可以解释为什么长期利率在大部分时间高于短期利率, 因为人们是风险厌恶的, 对于短期债券需求更大(债券在持有到期的情况下没有利率风险, 因此短期债券的利率风险低于长期债券)
   3. 解释不了为什么短期债券和长期债券波动几乎同步, 也解释不了为什么短债利率高的时候长债利率较短债低

3. Liquidity Premium and Preferred Habitat Theories

   1. 假设长期利率=短期利率期望的平均+利率补偿(期限越长补偿越高)

      $i_{nt}=\frac{i_t+i^e_{t+1}+...+i^e_{t+(n-1)}}{n}+l_{nt}$

      $i_{nt}$代表当前的n年期债券年化收益率

   2. 利率补偿有两种解释:

      1. 长债的流动性不好, 需要一定的风险溢价
      2. 人们更偏好短债, 因此长债必须有补偿才去买)

   3. 可以解释为什么大部分时间下越长的债利率越高

   4. 可以通过长债利率来判断未来的经济周期、通胀、利率

      1. 陡峭上行, 代表未来利息升高, 通胀可能变高.
      2. 平缓甚至下行, 代表未来利息降低, 经济可能衰退

