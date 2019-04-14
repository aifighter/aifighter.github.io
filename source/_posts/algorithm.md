---
title: 机器学习算法
comments: true
mathjax: true
date: 2019-03-19 00:22:00
categories:
- 算法
tags:
- 算法
description: 工作以来机器学习算法的积累
---

[TOC]

# 1. 二分类评估指标

评价的时候利用的是两个值：prediction score和label

## (1) Precision/Recall/F1

`Precision=TP/(TP+FP)`

`Recall=TP/(TP+FN)`

`F1=2*(P*R)/(P+R)`

## (2) ROC/AUC

> ROC曲线：receiver operating characteristic curve

x轴是假阳率`FPR=FP/(FP+TN)`，实际上就是打扰率，或者叫误杀率

y轴是真阳率`TPR=TP/(TP+FN)`，其实就是Recall

然后取不同分类阈值得到一个个点再作图即位ROC曲线，曲线下面积即为AUC

在欺诈场景下要求打扰率低，所以至关注ROC曲线左下角的部分

## (3) K-S曲线

将样本进行等分，分别画TPR和FPR的曲线，两个曲线之间的差值即为模型辨别“好坏”的能力

x轴是取出样本百分比（其实就是该threshold下判别为正例的），从`0%`到`100%`

y轴有两条曲线，取出样本中的累积正例占总正例比，和取出样本中的累积负例占总负例比

移动到每一个点，可以看到Threshold（即prediction score），样本占比（即这个threshhold可以取出多少样本），正例占比，负例占比，k-s（正负差值）

最完美的是k-s值永远为1，即threshold=0.001时可以取出全部整理出来，0.999时才开始取出负例

## (4) Gain曲线

x轴是取出样本百分比（标出Threshold）

y轴是当前threshold下的recall

自然是一个左下到右上的曲线

## (5) Lift曲线

总的来说是取这个Threshold时相比于随机分类器有多少提升

x轴是取出样本百分比（标出Threshold）

y轴是`Precision/ActualPositiveRate`，即相比于随机分类器的增益

`Precision=TP/(TP+FP)`

`ActualPositiveRate=(TP+FN)/(TP+FP+TN+FN)`

这里的ActualPositiveRate有点疑惑，应该是一个定值

**参考链接**

[1. model evaluation](http://chem-eng.utoronto.ca/~datamining/dmc/model_evaluation_c.htm)

##(6) IV值（information value）

是特征的有效性，[链接](http://ucanalytics.com/blogs/information-value-and-weight-of-evidencebanking-case/)

主要用于风控，对某个变量v（比如说交易金额）的某一个分箱i
$$
woe_i=ln(\frac{p_{y_1}}{p_{y_0}})=ln(\frac{\#B_i/\#B_T}{\#G_i/\#G_T})
$$
那么这个变量v的IV值就是woe_i的加权平均
$$
IV_i=(\frac{\#B_i}{\#B_T}-\frac{\#G_i}{\#G_T})\times ln(\frac{\#B_i/\#B_T}{\#G_i/\#G_T}) =(\frac{\#B_i}{\#B_T}-\frac{\#G_i}{\#G_T})\times woe_i\\
IV = \sum_{k=0}^{n}{IV_i}
$$
IV值衡量了该变量的预测能力

WOE衡量的是正样本占比和副样本占比是不是有足够的差异，IV值则是WOE的一个加权平均（同时去除了负WOE的影响）

# 2. Word2vec

> 第一个教程：
>
> [Word2Vec Tutorial Part 1 - The Skip-Gram Model](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)
>
> [Word2Vec Tutorial Part 2 - Negative Sampling](http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/)
>
> 第二个教程：
>
> [Word2vec Tutorial | RaRe Technologies](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjwzZm8tsrYAhWMlOAKHa74B2sQFgg3MAE&url=https%3A%2F%2Frare-technologies.com%2Fword2vec-tutorial%2F&usg=AOvVaw2NkfvzvA9WKVZK0-_xqZOE)

the Continuous Bag-of-Words model (CBOW)：context预测target，对小数据集更好

the Skip-Gram model：target预测context，对大数据集更好

## (1) [Word2Vec Tutorial Part 1 - The Skip-Gram Model](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)

### 设计思想

word2vec用了这样一个思想，我们训练一个网络执行某个特定任务，然而训练完成后不使用该网络执行该任务，而是从隐藏层得到我们所需的东西。该任务被称为“伪任务”（fake task）。

这个思想还被用在unsupervised learning提取图像特征上

### 伪任务

![training_data](/images/algorithm/training_data.png)

任务是从单词预测上下文，这里的window size是2

实际就是训练一个分类器

### 网络细节

![skip_gram_net_arch](/images/algorithm/skip_gram_net_arch.png)

假设有10000个单词，那么输入是10000维的one-hot

假设希望word2vec的维度是300，那么隐藏层的neuron个数就是300

输出层是一个10000分类的softmax

每个训练样本都是一对单词，如(the, quick)

### 直观理解

1. “拥有相似上下文的词将拥有相似的语义信息”
2. 由于输入是one-hot，所以隐藏层输出的永远是这个word的vector
3. 相似上下文的词的输出层将类似，那么vector也一定会比较类似

## (2) [Word2Vec Tutorial Part 2 - Negative Sampling](http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/)

### 存在问题

1. 参数过多：假设10000个单词，300维vector，那么参数量`10000*300*2`
2. 由于参数多，因此需要大量训练数据来防止过拟合

### 改进一：“Phrases”

把常常一起出现的单词当作Phrase，比如“New York”，缩小vocabulary的量

### 改进二：Subsampling Frequent Words

越常出现的单词越可能被删除，有一个经验公式（单词出现频率，被删除概率）

### 改进三：Negative Sampling

比如训练样本(fox, quick)，那么quick被认为是正样本，而其他9999个词都是负样本。每次更新参数的时候需要更新`300*10000+300`个（因为one-hot，所以第一层永远更新300个）。

现在取负样本个数为5，那么按“出现频率高的词被选为负样本高”的原则从其他9999个词中选出5个负样本。那么此时只需更新`300*5+300`个参数，大大减小了参数，并且防止了过拟合。

此时的Loss就不再是softmax loss，而是nce loss（tensorflow中）

选取negative sample的时候运用的是经验公式，即按出现频率的0.75次方来按比例选取

## (3) [Word2vec on Tensorflow](https://www.tensorflow.org/tutorials/word2vec)

demo代码：

[tensorflow/examples/tutorials/word2vec/word2vec_basic.py](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/examples/tutorials/word2vec/word2vec_basic.py)

[models/tutorials/embedding/word2vec.py](https://www.tensorflow.org/code/tensorflow_models/tutorials/embedding/word2vec.py)

几个核心步骤

1. 词到embedding（实现的时候不一定要出现one-hot，只要从词的编号到vector就行了）

   ```python
   embeddings = tf.Variable(
       tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
   ```


2. 定义输出层参数

   ```python
   nce_weights = tf.Variable(
     tf.truncated_normal([vocabulary_size, embedding_size],
                         stddev=1.0 / math.sqrt(embedding_size)))
   nce_biases = tf.Variable(tf.zeros([vocabulary_size]))
   ```

3. 输入输出的Placeholder

   ```python
   # Placeholders for inputs
   train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
   train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
   ```

4. 从输入的词到embedding，居然这种函数都有

   ```python
   embed = tf.nn.embedding_lookup(embeddings, train_inputs)
   ```

5. 定义损失函数和optimizer

   ```python
   # Compute the NCE loss, using a sample of the negative labels each time.
   loss = tf.reduce_mean(
     tf.nn.nce_loss(weights=nce_weights,
                    biases=nce_biases,
                    labels=train_labels,
                    inputs=embed,
                    num_sampled=num_sampled,
                    num_classes=vocabulary_size))
   # We use the SGD optimizer.
   optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)
   ```

6. 训练过程

   ```python
   for inputs, labels in generate_batch(...):
     feed_dict = {train_inputs: inputs, train_labels: labels}
     _, cur_loss = session.run([optimizer, loss], feed_dict=feed_dict)
   ```


##  (4) 应用

### Paper 1. [用word2vec来预测用户check-in](https://arxiv.org/pdf/1601.01356.pdf)

- 该paper用于地点推荐（比如饭店，住宿等等）
- 核心是将(user, loc, user, loc…)这样的序列送入word2vec
- 在推荐的时候采用三种策略：
  1. 距离user最近（cosine similarity）的items
  2. 距离user最近的users的items（随机取）
  3. 距离user最近的users的items中最近的那些
- 综合来说skip-gram效果更好，策略1效果更好



# 3. Velocity变量

一个velocity变量由5个元素定义：主体 客体 窗口 累计函数-count 过滤条件

**Example 1** 一个用户过去一个月交易金额大于100的笔数：主体-user_id 客体-event_id 窗口-30days 累计函数-count 过滤条件-amount>100

**Example 2** 一个IP过去一周交易中欺诈总金额：主体-ip 客体-amount 窗口-7days 累计函数-sum 过滤条件-is_fraud=1

# 4. tf-idf 

> tf-idf是一种统计方法，用以评估一字词对于一个文件集或一个[语料库](https://zh.wikipedia.org/wiki/%E8%AA%9E%E6%96%99%E5%BA%AB)中的其中一份[文件](https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6)的重要程度。

1. tf

   **词频**（term frequency，tf）指的是某一个给定的词语在该文件中出现的频率。 

   在文件j中的词语i的tf定义为
   $$
   tf_{i,j}=\frac{n_{i,j}}{\sum_k{n_{k,j}}}
   $$

2. idf

   **逆向文件频率**（inverse document frequency，idf）是一个词语普遍重要性的度量。某一特定词语的idf，可以由总文件数目除以包含该词语之文件的数目，再将得到的商取[对数](https://zh.wikipedia.org/wiki/%E5%B0%8D%E6%95%B8)得到

   对单词i，idf定义为，加1是防止词语不在语料中：
   $$
   {idf}_i=log\frac{|D|}{1+|{j:t_i \in d_j}|}
   $$

3. tf-idf

   词频高且该词在所有文件中出现频率低则会tf-idf高

   在文件j中的词语i的tf-idf定义为
   $$
   tfidf_{i,j}=tf_{i,j} \times {idf}_i
   $$









# 5. 决策树

1. 何时划分停止

   （1）当前节点的样本都是同一个种类，取该种类

   （2）当前属性集为空，或是样本在所有剩下的属性上取值相同，取多数的种类

   （3）当前节点包含的样本为空（二划分应该不会有这种情况），取父节点的种类

2. 划分选择

   （1）信息增益 Information Entropy

   信息熵定义为，这是一个大于0的值，越小越好（全部都是同一个种类就是0）
   $$
   Ent(D)=-\sum_{k=1}^{|\gamma|}p_klog_2 p_k
   $$
   依据属性a的划分的信息增益定义为
   $$
   Gain(D,a)=Ent(D)-\sum_{v=1}^{V}\frac{|D^v|}{|D|}Ent(D^v)
   $$
   增益越大，则划分越好

   （2）增益率

   信息增益对划分较多的属性有偏好，因此增益率是在信息增益上的一个调整

   例子：C4.5算法

   （3）基尼指数

   数据集D的基尼值定义为
   $$
   Gini(D)=1-\sum_{k=1}^{\gamma}p_k^2
   $$
   直观理解是：按分布随机分类一个样本，分错掉的概率，所以是越接近0越好，和信息熵很像

   属性a的基尼指数定义为：
   $$
   Gini\_index(D,a)=\sum_{v=1}^{V}\frac{|D^v|}{|D|}Gini(D^v)
   $$

3. 三种数据类型

   上面的计算都是针对多划分，而一般来说决策树都是二划分

   1. Boolean Data
   2. Numerical Data：从排序后的每两个数的均值划分
   3. Categorical Data
      1. 无序的：当种类个数太多时将无法处理导致报错
      2. 有序的：排序后与Numerical处理差不多

# 6. Gradient Boosting

[博文链接](https://gormanalysis.com/gradient-boosting-explained/)

**为什么Boosting可以防止过拟合**

因为对每组特征的划分可以考察整个训练数据集而不是单个训练集。看下面的例子

![gb_tree1B_4](/images/algorithm/gb_tree1B_4.png)

这是普通的决策树

![gb_tree1_3](/images/algorithm/gb_tree1_3.png)

![gb_tree2_3](/images/algorithm/gb_tree2_3.png)

这是采用了Boosting的DT，可以看到第二棵树的分裂考虑了所有样本，而单棵树的分裂中出现了LikesHats（这是噪声）

## Draft 1 基本思想

1. 建一个模型F使得
   $$
   F_1(x)=y
   $$

2. 建一个模型h使得
   $$
   h_1(x)=y-F_1(x)
   $$

3. 得到新的模型
   $$
   F_2(x)=F_1(x)+h_1(x)
   $$

4. 重复上述过程多次得到最终的模型

## Draft2 应对squared error

现在针对的回归问题的损失函数是squared error，所以初始化模型为：
$$
F_0(x)=\arg\min_\gamma\sum_{i=1}^{n}{L(y_i,\gamma)}=\arg\min_\gamma\sum_{i=1}^{n}{(\gamma-y_i)^2}=\frac{1}{n}\sum_{i=1}^{n}y_i
$$
之后可以使用Draft1中的方法重复m次得到Fm

## Draft 3 使用梯度下降

现在遇到的问题是我们的损失函数不是squared error而是absolute error，那现在的方法将不太好用：

1. 计算复杂（每次分裂都需要计算一次中位数（absolute error的最优解是中位数，squared error是平均		值）
2. 我们必须使得每个weak learner（通常情况就是决策树）都支持这种损失函数



**解决方法：**

	之前都是对残差`y-Fk(x)`来构建模型，现在每次对梯度建立模型



**具体步骤：**

1. 初始化F0
   $$
   F_0(x)=\arg\min_\gamma\sum_{i=1}^{n}{L(y_i,\gamma)}
   $$

2. For m = 1 to M:

   （1）计算每个sample的pseudo residual:
   $$
   r_{im}=-[\frac{\partial{L(y_i, F_{m-1}(x_i))}}{\partial{F_{m-1}(x_i)}}]
   $$
   （2）对`r_m`构建一个模型
   $$
   h_m(x)=r_m
   $$
   （3）得到新的模型
   $$
   F_m(x)=F_{m-1}(x)+\gamma_m h_m(x)
   $$
   	**$\gamma_m$的选取**（即line search）
		
   	其中对每一组分裂中的sample可以选择不一样的`\gamma_m`来最小化这几个sample的损失函数L
		
   	举例来说，squared error的所有`\gamma`都取1就行了，absolute roor则需要使得`F_m(x)`是这组分裂的中位数。



**举个例子**

Squared error
$$
L(F(x), \gamma)=\sum_{i=1}^{n}{(F(x)-y_i)^2}
$$

| Age  | F0    | PseudoResidual0 | h0     | gamma0 | F1    | PseudoResidual1 | h1     | gamma1 | F2    |
| ---- | ----- | --------------- | ------ | ------ | ----- | --------------- | ------ | ------ | ----- |
| 13   | 40.33 | -27.33          | -21.08 | 1      | 19.25 | -6.25           | -3.567 | 1      | 15.68 |
| 14   | 40.33 | -26.33          | -21.08 | 1      | 19.25 | -5.25           | -3.567 | 1      | 15.68 |
| 15   | 40.33 | -25.33          | -21.08 | 1      | 19.25 | -4.25           | -3.567 | 1      | 15.68 |
| 25   | 40.33 | -15.33          | 16.87  | 1      | 57.2  | -32.2           | -3.567 | 1      | 53.63 |
| 35   | 40.33 | -5.333          | -21.08 | 1      | 19.25 | 15.75           | -3.567 | 1      | 15.68 |
| 49   | 40.33 | 8.667           | 16.87  | 1      | 57.2  | -8.2            | 7.133  | 1      | 64.33 |
| 68   | 40.33 | 27.67           | 16.87  | 1      | 57.2  | 10.8            | -3.567 | 1      | 53.63 |
| 71   | 40.33 | 30.67           | 16.87  | 1      | 57.2  | 13.8            | 7.133  | 1      | 64.33 |
| 73   | 40.33 | 32.67           | 16.87  | 1      | 57.2  | 15.8            | 7.133  | 1      | 64.33 |

Absolute error
$$
L(F(x), \gamma)=\sum_{i=1}^{n}{|(F(x)-y_i)|}
$$

| Age  | F0   | PseudoResidual0 | h0   | gamma0 | F1   | PseudoResidual1 | h1      | gamma1 | F2    |
| ---- | ---- | --------------- | ---- | ------ | ---- | --------------- | ------- | ------ | ----- |
| 13   | 35   | -1              | -1   | 20.5   | 14.5 | -1              | -0.3333 | 0.75   | 14.25 |
| 14   | 35   | -1              | -1   | 20.5   | 14.5 | -1              | -0.3333 | 0.75   | 14.25 |
| 15   | 35   | -1              | -1   | 20.5   | 14.5 | 1               | -0.3333 | 0.75   | 14.25 |
| 25   | 35   | -1              | 0.6  | 55     | 68   | -1              | -0.3333 | 0.75   | 67.75 |
| 35   | 35   | -1              | -1   | 20.5   | 14.5 | 1               | -0.3333 | 0.75   | 14.25 |
| 49   | 35   | 1               | 0.6  | 55     | 68   | -1              | 0.3333  | 9      | 71    |
| 68   | 35   | 1               | 0.6  | 55     | 68   | -1              | -0.3333 | 0.75   | 67.75 |
| 71   | 35   | 1               | 0.6  | 55     | 68   | 1               | 0.3333  | 9      | 71    |
| 73   | 35   | 1               | 0.6  | 55     | 68   | 1               | 0.3333  | 9      | 71    |

![gb_maeTrees_1](/images/algorithm/gb_maeTrees_1.png)

## Draft4 Shrinkage

每个step更新model的时候乘以一个范围在(0,1)的learning rate
$$
F_m(x)=F_{m-1}(x)+v \cdot \gamma_m h_m(x)
$$

## Draft5 Random Sampling

传说中的BootStrap方法，可以从两个维度，row（即样本数量），column（即特征数量）

## Gradient Boost In Practice

[XGBoost](http://www.kdd.org/kdd2016/papers/files/rfp0697-chenAemb.pdf)

[LightGBM](https://github.com/Microsoft/LightGBM)

# 7. Neural Attention Model

## （1）是什么，为什么

**Encoder-decoder模型**

下图是NLP中的Encoder-Decoder模型，许多NLP任务可以抽象成为这样子一个模型。

用于由一种形式的text生成另外一种形式的text，如：翻译，摘要，embedding（这是我想的）

![屏幕快照 2018-02-02 上午11.19.40](/images/algorithm/屏幕快照 2018-02-02 上午11.19.40.png)

输入是m个word：
$$
X=\{x_1, x_2, ..., x_m\}
$$
输出是n个word：
$$
Y=\{y_1, y_2, ..., y_n\}
$$
Encoder是将输入句子X转换成中间语义C：
$$
C=\mathcal{F}(x_1, x_2, ..., x_m)
$$
Decoder是将中间语义C和已经生成的历史信息y来生成当前单词
$$
y_i=\mathcal{G}(C,y_1,y_2,...,y_{i-1})
$$

> Encoder-Decoder是个创新游戏大杀器，一方面如上所述，可以搞各种不同的模型组合，另外一方面它的应用场景多得不得了，比如对于机器翻译来说，<X,Y>就是对应不同语言的句子，比如X是英语句子，Y是对应的中文句子翻译。再比如对于文本摘要来说，X就是一篇文章，Y就是对应的摘要；再比如对于对话机器人来说，X就是某人的一句话，Y就是对话机器人的应答。

**存在的问题**

生成每一个y的时候，每一个x的贡献权重都是一样的，这很不符合人类习惯

**Attention机制**

![屏幕快照 2018-02-02 上午11.42.08](/images/algorithm/屏幕快照 2018-02-02 上午11.42.08.png)

每个单词的生成变成了这样
$$
y_1=\mathcal{G}(C_1) \\
y_2=\mathcal{G}(C_2, y_1) \\
y_3=\mathcal{G}(C_3, y_1, y_2) \\
$$
那么相应的，生成中间语义C的过程也要改变，举例将Tom Chase Jerry翻译成“汤姆追杰瑞”来说
$$
C_{汤姆}=g(0.6*f('Tom')+0.2*f('chase')+0.2*f('Jerry'))
$$
那么这个权重是怎么来的呢？我们假设Encoder和Decoder都是RNN。

非AM模型的将是这样的，C是固定的

![屏幕快照 2018-02-02 上午11.53.36](/images/algorithm/屏幕快照 2018-02-02 上午11.53.36.png)

加入了AM模型之后是这样的，C是动态计算的

![屏幕快照 2018-02-02 上午11.54.55](/images/algorithm/屏幕快照 2018-02-02 上午11.54.55.png)

由于y_i的得出前先有隐层H_i和输入单词的隐层h_1~h_m

那么可以定义一个F(h,H)+softmax来计算得到权重，F(h,H)应该是一种相似性函数，如cosine similarity（我猜的），或者是另外一个可以bp的参数

> 通过函数F(hj,Hi)来获得目标单词Yi和每个输入单词对应的对齐可能性，这个F函数在不同论文里可能会采取不同的方法，然后函数F的输出经过Softmax进行归一化就得到了符合概率分布取值区间的注意力分配概率分布数值。可以把AM模型理解成单词对齐模型。

## （2）论文一：Yoshua Bengio在ICLR2015的论文

第一篇提出Attension机制的论文：https://arxiv.org/pdf/1409.0473.pdf

基本上就是上面的架构，用于Neural Machine Translation

![屏幕快照 2018-02-02 下午12.18.13](/images/algorithm/屏幕快照 2018-02-02 下午12.18.13.png)

核心：
$$
p(y_i|y_1,...,y_{i-1}, {x})=g(y_{i-1},s_i,c_i)
$$
其中s_i是RNN的隐层输出
$$
s_i=f(s_{i-1}, y_{i-1},c_i)
$$
c_i就是之前计算的加权过的输入
$$
c_i=\sum_{j=1}^{T_x}\alpha_{ij}h_j \\
\alpha_{ij}=\frac{exp(e_{ij})}{\sum_{k=1}^{T_x}exp(e_{ik})}\\
e_{ij}=a(s_{i-1}, h_j)
$$
这个a就是一个alignment model which scores how well the inputs around position j and the output at position i match，a是一个全连接的神经网络



# 8. CS231-CNN Architecture

## 1. AlexNet & ZFNet

1. ILSVRC2012: AlexNet，8 layers，第一层`11*11`，参数数量60M
2. ILSVRC2013: ZFNet （AlexNet的基础上的调参）

## 2. VGG

ILSVRC2014: VGG，参数数量138M

`3*3`的卷积，16-19层

**3个`3*3`卷积与1个`7*7`卷积的感受区域是相同的，但是参数更少27/49**

## 3. GoogleNet

ILSVRC2014: Inception Net，参数数量5M![屏幕快照 2018-05-08 下午3.14.30](/images/algorithm/屏幕快照 2018-05-08 下午3.14.30.png)

Inception module的缺点是计算量很大而且输出维度越来越高

红色的`1*1`conv层是为了减小参数数量，减小输出depth

## 4. ResNet

![屏幕快照 2018-05-08 下午5.19.02](/images/algorithm/屏幕快照 2018-05-08 下午5.19.02.png)

学习residual，使学习变得“容易”，最差情况（F(x)输出全0），也能得到一个Identity的结果

## 5. 计算量

![屏幕快照 2018-05-08 下午5.32.39](/images/algorithm/屏幕快照 2018-05-08 下午5.32.39.png)

## 6. 其他网络

1. 一系列ResNet的改进

   1. 更宽但是更浅
   2. 每个ResBlock是多路的，类似Inception
   3. Deep Networks with Stochastic Depth，每次训练时随机扔掉一些Res Block，Inference的时候全部用上（dropout的想法）（这个思路后面的paper也有用到）

2. FractalNet

   用的不多

3. DenseNet

   排列组合的连接

4. SqueezeNet

   50x fewer参数，对比AlexNet


## 7. MobileNet

深度学习网络的一种加速方式，主要是把卷积操作变成了一个分两步的操作，称为**depthwise separable convolution**

假设卷积输入为 $100(D_F)*100(D_F)*16(M)$，输出为$100(D_F)*100(D_F)*32(N)$，卷积核的大小为$3(D_K)*3(D_K)$

那么正常卷积的参数个数为$3*3*16*32$

MobileNet的做法是分两步

**第一步**

用M个$3*3$的卷积核分别对M个channel去卷积，不做相加，堆叠起来

这样输出是$100*100*16$

计算量：$100*100*3*3*16$

**第二步**

对第一步的输出做$1*1$的卷积，输出的channel数为N

输出是$100*100*32$

计算量：$100*100*1*1*16*32$

**计算量对比**

原来的计算量$100*100*3*3*16*32$，现在减少到约9分之1

## 8. ShuffleNet

是进一步进行网络压缩和加速的算法，核心是channel shuffle、pointwise group convolutions和depthwise separable convolution

depthwise separable convolution在MobileNet中已经详细说明，主要记录channel shuffle和pointwise group convolutions的思想

**Group Convolution**

其实就是AlexNet里面的把feature map（both输入输出）分成2（可以改变为更多）部分分别去做卷积

**Channel Shuffle**

更加简单了假设9个channel分成3个group去卷积，那我不要(123)(456)(789)这样分，而是(147)(258)(369)这样


# 9. CS231-Detection and Segmentation

## 1. Semantic Segmentation

分类图片中的每一个像素（不会把两只牛分开为两个object）![屏幕快照 2018-05-09 下午2.59.28](/images/algorithm/屏幕快照 2018-05-09 下午2.59.28.png)

所以最后的标签必须是pixel level的，输出应该是`H*W*C`，C是目标num_category

其中最为重要的操作为反卷积（Transposed Convolution）

反卷积也有learnable的kernel，下图是一维卷积下的反卷积![屏幕快照 2018-05-09 下午3.10.29](/images/algorithm/屏幕快照 2018-05-09 下午3.10.29.png)

## 2. Classification and localization

分类加上Bounding Box

label中加入四个值(x,y,w,h)

其他应用：human pose estimation

## 3. Object Detection

和localization的主要区别是输出的数量是不一定的

1. R-CNN

   第一步，region proposal networks（找出可能包含object的RoI(region of interest)）（约2000个）该方法为传统方法

   第二步，把region变成同样的size

   第三步，CNN+SVM，输出classification（里面有background这个类）和一系列连续值代表offset（因为bounding box不准）

   问题：慢

   ![屏幕快照 2018-05-09 下午4.51.23](/images/algorithm/屏幕快照 2018-05-09 下午4.51.23.png)

2. Fast R-CNN

   解决R-CNN的问题，只做一次大的卷积，然后把RoI映射到feature map上，但是RoI还是传统方法

   另外放弃了SVM，增加了一种RoI pooling使得projected RoI的size相同

   大大提升了速度，速度瓶颈在region proposal这边，快了20倍

   注意：Fast R-CNN的RegionProposal是在feature map之后做的，这样可以不用对所有的区域进行单独的CNN Forward步骤。

   ![屏幕快照 2018-05-09 下午5.02.12](/images/algorithm/屏幕快照 2018-05-09 下午5.02.12.png)

3. Faster R-CNN

   解决了Fast R-CNN的速度瓶颈，把Region proposal放到deep learning中变成RPN

   快了10倍

   ![屏幕快照 2018-05-09 下午5.18.34](/Users/lxc/work/notes/learning/屏幕快照 2018-05-09 下午5.18.34.png)

4. YOLO/SSD

   分格，规定base box的形状来做CNN，输出classification+localization

5. 总结

   region based要慢一些，不过要准一些

## 4. Instance Segmentation

任务是1和3的合体，还可以加上pose estimation

方法基本上是Faster-RCNN和Semantic Segmentation的合体

Mask RCNN （何凯明）

![屏幕快照 2018-05-09 下午5.39.59](屏幕快照 2018-05-09 下午5.39.59.png)

![屏幕快照 2018-05-09 下午5.38.14](屏幕快照 2018-05-09 下午5.38.14.png)



# 10. Loss Functions

## 1. Binary cross entropy

y是标签，p是预测值

$Loss = - y * log(p) - (1-y)*log(1-p)$

## 2. Focal Loss

He Kaiming提出的用于object detection的

$Loss = - \alpha *(1-p)^\gamma*y * log(p) - (1-\alpha)*p^\gamma*(1-y)*log(1-p)$

核心有两个参数，如alpha=0.75，gamma=2：

1. alpha：控制黑白样本的学习速率
2. gamma：让分错的学习率增加，比如标签是1，预测p=0.1则权重加大，预测p=0.9则权重变小



# 11. CS231-Visualizing and Understanding

## 1. Visualizing filters

即把kernel weights可视化出来，有如下几个缺点：

1. 只有第一个卷积层可以可视化成图像（因为channel个数为3），其他只能将每个channel作为一个grey image
2. 只有第一层具有明显含义，因为只有第一层是直接连接到输入图像的

Q：为什么可视化filter可以看到pattern？

A：因为当两个vector相乘时，两个vector相同可以得到最大程度的激活

## 2. Last layer: nearest neighbors, PCA, t-SNE

1. 即将最后一个全连接层做nearest neighbor search，多用于图像检索
2. 将最后一层降维至两维，然后再画图看

## 3. Visualizing Activations

直接看图片的feature map，下图即在alexnet的第五个卷积层找到了某个发现人脸的feature map

![屏幕快照 2018-05-11 下午2.46.16](屏幕快照 2018-05-11 下午2.46.16.png)

## 4. Maximally Activating Patches

下图中的每一行代表：

1. 输入一堆图片到cnn中
2. 取出某一层的某个channel的某个neuron的激活值
3. 按激活值从大到大排序
4. 显示出该neuron的感知区域

![屏幕快照 2018-05-11 下午2.52.47](屏幕快照 2018-05-11 下午2.52.47.png)

## 5. Saliency Maps

思想是看每个pixel对该class的预测值会有多少影响

即计算$\frac{\partial{score}}{\partial{pixel}}$

![屏幕快照 2018-05-14 上午10.59.37](屏幕快照 2018-05-14 上午10.59.37.png)

## 6. Intermediate features via (guided) backprop

与Saliency Map的思路基本相同，区别在于：

1. 计算的不是$\frac{\partial{score}}{\partial{pixel}}$，分式上面是某个隐层的某个neuron

2. 反向传播的时候对ReLU的处理比较特别，用的是guided propagation

   ![屏幕快照 2018-05-14 下午2.34.38](屏幕快照 2018-05-14 下午2.34.38.png)

   （1）正常反向，relu的输入为正的部分反向传播

   （2）“deconvnet”反向，relu的输出为正的部分反向传播

   （3）guided backprop：（1）（2）结合

![屏幕快照 2018-05-14 下午2.45.45](屏幕快照 2018-05-14 下午2.45.45.png)

再把它和方法4结合就得到上图的结果

## 7. Gradient Ascent

- gradient descent是为了minimize loss function
- 这里gradient ascent是为了maximize某个activation（这个activation可以是class score，也可以是中间层的neuron）
- 这里的$y=f(x)$，y是某个activation，x是输入image，而weights是固定的
- 直接做gradient ascent只会得到一些噪声，需要加一些regularizer来使生成的图像make sense

总结一下：

	$I^*=argmax(f(I)+R(I))$

## 其他

1. Occlusion Experiment

   去掉一部分图片（如32*32）看分类结果，然后sliding window画出一个类似heatmap的东西

   heatmap的值就是去掉这一小块图片后的预测值

   思想是看这一小块图片是不是对预测结果很重要



# 12. CTR算法

> 点击率(Click through rate)是点击特定链接的用户与查看页面，电子邮件或广告的总用户数量之比。 它通常用于衡量某个网站的在线广告活动是否成功，以及电子邮件活动的有效性。 
> **点击率是广告点击次数除以总展示次数（广告投放次数）**
>
> 目前，CTR的数值平均接近0.2%或0.3%，超过2%被认为是非常成功的。

## 1. FM(Factorization Machines)

2010年的论文

FM解决的是高维稀疏的特征组合的问题

最简单的是线性模型

$y=w_0+\sum_{i=1}^{n}w_ix_i$

我们希望得到的模型是可以考虑特征之间关联的，如二阶多项式模型

$y=w_0+\sum_{i=1}^{n}w_ix_i+\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}w_{ij}x_ix_j$

存在的问题：

1. 特征维度很高导致时间复杂度大大增加，达到$O(n^2)$
2. 训练的时候大部分$w_{ij}$学习不到

FM的做法是这样的，对每一个维度的特征引入一个k维的辅助向量

$v_i=(v_{i1}, v_{i2}, …, v_{ik})^\top$

这样$w_{ij}$就可以使用$v_i^\top*v_j$来估计，那么模型就变成了：

$y=w_0+\sum_{i=1}^{n}w_ix_i+\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}(v_i^\top*v_j)x_ix_j$

优点有两个：

1. 时间复杂度大大减小，达到O(kn)（之所以可以到O(kn)是因为上面模型的计算可以简化）
2. 即使是训练样本中没有出现的特征组合，也可以得到估计

参考资料：

PAPER：https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf

https://www.cnblogs.com/pinard/p/6370127.html

https://blog.csdn.net/John_xyz/article/details/78933253

## 2. FFM

2016年的论文：https://arxiv.org/pdf/1703.04247.pdf

FFM即在FM的基础上加入了Field-aware，即认为输入特征是分field的，其实是有道理的，因为同一组one-hot应该看成一个field

假设有n个特征，f个field，那么前面的k维的辅助向量就变成了k*f维

$w_{ij}$就变成使用$v_{i, f_j}^\top*v_{j, f_i}$来估计

## 3. DeepFM

个人认为是最好的处理连续+离散型特征的方式

![屏幕快照 2018-06-09 下午7.44.24](屏幕快照 2018-06-09 下午7.44.24.png)

1. 首先，每个feature（一个categorical算一个feature）都映射到K维embedding
2. 类似FM层求二次交叉项（用矩阵运算）和一次项（即LR）
3. Embedding平铺做DNN
4. 将FM和DNN合并输出一个打分

实现思路：

1. FM一次项部分，连续变量用Dense(1)，离散变量用Embedding(out=1)，然后Concat再Dense(1)
2. FM的二次项部分，连续变量用Dense(K)，离散用Embedding(out=K)，然后变成(N,K)的矩阵，再用简化的矩阵运算
3. DNN部分(N,K)的矩阵Flatten后直接用DNN，66666

参考资料：

https://blog.csdn.net/songbinxu/article/details/80151814



# 13. CS231-Generative Models

![屏幕快照 2018-06-12 下午6.03.12](屏幕快照 2018-06-12 下午6.03.12.png)

上图是generative models的分类：

Explicit density model学习的是条件概率

即学习下面这个式子

$p(x)=\prod_{i=1}^{n}p(x_i|x_1,…,x_{i-1})$

第i个pixel是根据前i-1个pixel的值来生成的一个分布

## 1. PixelRNN, PixelCNN

学习的是：$p(x)=\prod_{i=1}^{n}p(x_i|x_1,…,x_{i-1})$

PixelRNN即一个一个pixel连接成一个序列来学，label就是生成下一个pixel（从左上到右下）。缺点训练慢，generation也慢。

PixelCNN的优点在于train的时候速度会比较快，CNN的时候只看自己左上方的pixel，不过在generation的时候还是比较慢，还得一个个pixel来。

## 2. VAE - Variational AutoEncoders

学习的是：$p_{\theta}(x)=\int{p_{\theta}(x)}p_{\theta}(x|z)$

Autoencoder的加强版，Pipeline如图所示

![v2-8769151d6bd61bceead581d4aa0c2b37_1200x500](v2-8769151d6bd61bceead581d4aa0c2b37_1200x500.jpg)

与AutoEncoder的区别：

1. 在编码过程迫使其生成的隐含向量能够粗略的遵循一个标准正态分布，先生成两个序列一个表示均值一个表示方差，然后再用标准正态分布去乘均值方差
2. Loss一个是生成图像的mse，另一个是看latent vector是否符合正态分布
3. 最后生成的时候给均值方差来生成图像

## 3. GANs

不直接学习概率密度函数，而是通过2-player-game来从train分布来生成图片

Generator：从随机分布采样的输入生成图像，尽可能让Discriminator打高分

Discriminator：给真实图像打高分，给生成的图像打低分

![屏幕快照 2018-07-24 下午7.16.41](屏幕快照 2018-07-24 下午7.16.41.png)

**Loss func**

$\max\limits_{\theta_d}[E_{x\sim p_{data}}logD_{\theta_d}(x) + E_{z\sim p_{z}}log(1-D_{\theta_d}(G_{\theta_g}(z)))]$

$\max\limits_{\theta_g}E_{z\sim p_{z}}logD_{\theta_d}(G_{\theta_g}(z))$

之所以第二个式子取log而不是log(1-..)的原因是让它在生成的图片结果接近0时梯度变大

**训练过程**

每个iteration做如下工作：

1. 通过先验知识p(z)比如说正态分布来sample m个z $\{z^{(1)}, z^{(2)}, …,z^{(m)}\}$
2. 从真实图像$p_{data}(x)$中采样m张真实图像$\{x^{(1)}, x^{(2)}, …,x^{(m)}\}$
3. 用gradient ascent来优化Loss Func1
4. 将1～3重复k次（k一般取1）
5. 通过先验知识p(z)比如说正态分布来sample m个z $\{z^{(1)}, z^{(2)}, …,z^{(m)}\}$
6. 用gradient ascent来优化Loss Func2

**很多应用**

1. 对两个z1和z2做插值可以得到两张生成的图片的转变过程

2. 对不同语义的z可以做语义上的加减法

   Smiling woman  - neutral woman + neutral man = smiling man

# 13. One(Few) shot learning

主要参考资料为下面的blog以及原始论文

https://blog.csdn.net/mao_feng/article/details/78939864

Few shot leanring要解决的核心问题有两个：

1. 目标类别的样本非常少
2. 最好不改变原有网络的结构

以cifar10为例，我们拥有其中5类的大量数据，而另外5类的样本非常少。

关于support set：

在做inference的时候不仅需要$x_i$，还需要一些带标签的support set

**1. 基于Finetuning**

常规方法

**2. 基于Metric**

Metric是学习度量空间的方法，因为图像这类信息很难使用类似L2距离来计算相似度。

（1）孪生网络 （Siamese Neural Networks）

用大量样本（前5类）训练一个pairwise loss的网络

预测时，从预测类别（带标签）中每类选取5个sample，新的样本和这25个sample比较距离，选取最近的那类

（2）匹配网络（matching networks）

Matching Networks for One Shot Learning，是deepmind在2016年的论文

学习的是这个模型$P(\hat{y}|\hat{x}, S)$，其中S是拥有k个样本的support set，模型需要做到的是预测x与support set中的哪一类最相似

> 比如，在训练时给定一张暹罗猫的图片和一张柯基的图片作为S，对于一张新的哈士奇的图片模型可以将其分类为狗；在测试时拿来一张熊二的图片和一张兔八哥的图片，又拿来一张小熊维尼的图片问机器这个新图片是属于哪一类的，机器就会告诉你这个是熊（跟那个熊二是一个类的）

首先给出模型的定义：

$P(\hat{y}|\hat{x}, S)=\sum_{i=1}^ka(\hat{x},x_i)y_i$，其中xi,yi是support set中的样本，a就是我们需要学习的attention函数

下面给出attention mechanism的定义，其中c是cosine距离函数，f和g分别是support set和待预测样本的embedding函数

$a(\hat{x},x_i)=e^{c(f(\hat{x}),g(x_i))}/\sum_{j=1}^{k}e^{c(f(\hat{x}),g(x_i))}$

论文特别强调了f和g要全局考虑到S（称为full context embeddings），即$g(x_i)$实际上是$g(x_i, S)$，$f(\hat{x})$实际上是$g(\hat{x}, S)$，所以f和g都是LSTM模型，其中会包含将x映射到feature的传统模型（如vgg）

在训练的时候，每次抽取一个标签子集，再从中取出样本子集用于训练

（3）原型网络 （Prototypical Networks）

它学习一个度量空间， 通过计算和每个类别的原型表达的距离来进行分类。文章基于这样的想法：每个类别都存在一个聚在某单个原型表达周围的embedding，该类的原型是support set在embedding空间中的均值。然后，分类问题变成在embedding空间中的最近邻。

**3. 基于Meta Learning**

# 14. RL - 增强学习

## 1. 背景知识

1. 马尔可夫链

   下一个状态$S_{t+1}$只与当前状态$S_t$有关，可以通过乘以转移概率矩阵P得到

2. 隐马尔可夫模型

   除了可见状态链外还有一个不可见状态链，如有三个不同面数的骰子，每次随机选一只骰子掷出的点数

3. 马尔可夫决策过程

   马尔可夫决策过程(Markov Decision Process, MDP)也具有马尔可夫性，与上面不同的是MDP考虑了动作，即系统下个状态不仅和当前的状态有关，也和当前采取的动作有关

|         | 不考虑动作        | 考虑动作                  |
| ------- | ------------ | --------------------- |
| 状态完全可见  | 马尔科夫链(MC)    | 马尔可夫决策过程(MDP)         |
| 状态不完全可见 | 隐马尔可夫模型(HMM) | 不完全可观察马尔可夫决策过程(POMDP) |

# 15. Keras

> Book reading：
>
> Francois Chollet-Deep Learning with Python-Manning Publications (2017)

## 1. What is deep learning

作者认为深度学习是Learning representations from data

## 2. Before we begin: the mathematical building blocks of neural networks					 		

数据是由Tensor表示的，常见的tensor有

- Vector data—2D tensors of shape(samples,features)

- Timeseries data or sequence data—3D tensors of shape (samples, timesteps,

  features)

- Images—4D tensors of shape(samples,height,width,channels)or(samples,

  channels, height, width)

- Video —5D tensors of shape (samples, frames, height, width, channels) or

  (samples, frames, channels, height, width)

另外讲了一些如前向传播反向传播，sgd，optimizer，loss等知识

## 3. Getting started with neural networks

Keras的Backend Engine有三种：Tensorflow，Theano，CNTK。CPU的Backend又有BLAS和Eigen，GPU的Backend是CUDA和Cudnn。

构建Keras model有两种方式，Sequential和Functional API。Sequential只能处理单输入单输出并且，一路级联的模型。

这个章节还给了三个例子分别为二分类，多分类和回归

**Fit History**

Note that the call to model.fit() returns a History object. This object has a member history, which is a dictionary containing data about everything that happened during training.

**sparse_categorical_crossentropy**

和categorical_crossentropy一样，label可以接受Integer

**K-fold**

当训练数据量很小时，validation可以使用K-fold来做

**Normalization**

连续变量记得加入normalization

## 4. Fundamentals of machine learning

### 4.1 首先讲了机器学习的分类

1. supervised
2. unsupervised
3. self-supervised
4. reinforcement learning

### 4.2 算法的evaluation的方式

1. simple hold out 最常用
2. K-fold validation
3. 当数据量极小时，ITERATED K-FOLD VALIDATION WITH SHUFFLING



## 4.3 Data preprocessing, feature engineering, and feature learning

数据预处理：

- Vectorization：把数据变成tensor
- Normalization：连续值都需要做，目标：值要小，数据要在一个分布中
- 缺失值：填充0，若测试集有缺失值，最好在训练集中加入缺失值

特征工程：

- 定义：

  > Feature engineering is the process of using your own knowledge about the data and about the machine-learning algorithm at hand (in this case, a neural network) to make the algorithm work better by applying hardcoded (nonlearned) transformations to the data before it goesinto the model. 

### 4.4 过拟合问题

- 增加训练数据：总是有效


- 减小网络参数

- Regularization

  ```python
  model = models.Sequential()
  model.add(layers.Dense(16, kernel_regularizer=regularizers.l2(0.001),
  activation='relu', input_shape=(10000,))) model.add(layers.Dense(16, kernel_regularizer=regularizers.l2(0.001),
                         activation='relu'))
  model.add(layers.Dense(1, activation='sigmoid'))
  ```

- Dropout实现过程，实际上输出要扩大

  ```python
  layer_output *= np.random.randint(0, high=2, size=layer_output.shape)
  layer_output /= 0.5
  ```

### 4.5 Pipeline

1. 准备训练集
2. Choose how you’ll measure success on your problem. Which metrics willyou monitor on your validation data?
3. Determine your evaluation protocol: hold-out validation? K-fold valida-tion? Which portion of the data should you use for validation?
4. 训练出一个比dumb model要好的model：a model withstatistical power.
5. 训练出overfit的model
6. 解决过拟合

## 5. CNN

1. ImageGenerator

   可以解决内存不够的问题

   ```python
   from keras.preprocessing.image import ImageDataGenerator

   # All images will be rescaled by 1./255
   train_datagen = ImageDataGenerator(rescale=1./255)
   test_datagen = ImageDataGenerator(rescale=1./255)

   train_generator = train_datagen.flow_from_directory(
           # This is the target directory
           train_dir,
           # All images will be resized to 150x150
           target_size=(150, 150),
           batch_size=20,
           # Since we use binary_crossentropy loss, we need binary labels
           class_mode='binary')

   validation_generator = test_datagen.flow_from_directory(
           validation_dir,
           target_size=(150, 150),
           batch_size=20,
           class_mode='binary')
   ```

   train_dir里面一个文件夹代表一个category

2. Data Augmentation

   以前理解错了，以为是扩大训练集。

   实际作用，每次处理一张图片时，先随机变换一下，数据集还是这些，是基于ImageDataGenerator的

   ```python
   train_datagen = ImageDataGenerator(
       rescale=1./255,
       rotation_range=40,
       width_shift_range=0.2,
       height_shift_range=0.2,
       shear_range=0.2,
       zoom_range=0.2,
       horizontal_flip=True,)

   # Note that the validation data should not be augmented!
   test_datagen = ImageDataGenerator(rescale=1./255)

   train_generator = train_datagen.flow_from_directory(
           # This is the target directory
           train_dir,
           # All images will be resized to 150x150
           target_size=(150, 150),
           batch_size=32,
           # Since we use binary_crossentropy loss, we need binary labels
           class_mode='binary')

   validation_generator = test_datagen.flow_from_directory(
           validation_dir,
           target_size=(150, 150),
           batch_size=32,
           class_mode='binary')

   history = model.fit_generator(
         train_generator,
         steps_per_epoch=100,
         epochs=100,
         validation_data=validation_generator,
         validation_steps=50)
   ```

3. 用预训练网路

   两个方法：1. 先提feature，再训练dnn网络 2. 合成一个网络，然后freeze layers

   第二个会比较好一点，因为可以用data augmentation。

   为什么要freeze layers？

   Because the Dense layers on top are randomly initialized, very large weight updates would be propagated through the network, effectively destroying the representations previously learned.

   ```python
   # 注意conv_base本身就是一个model，这样最方便
   model = models.Sequential()
   model.add(conv_base)
   model.add(layers.Flatten())
   model.add(layers.Dense(256, activation='relu'))
   model.add(layers.Dense(1, activation='sigmoid'))
   conv_base.trainable = False
   ```

4. Fine-tuning

   流程：

   	1  Add your custom network on top of an already-trained base network.
		
   	2  Freeze the base network.
		
   	3  Train the part you added.
		
   	4  Unfreeze some layers in the base network.
		
   	5  Jointly train both these layers and the part you added.

   写法：

   ```python
   conv_base.trainable = True
   set_trainable = False
   for layer in conv_base.layers:
       if layer.name == 'block5_conv1':
           set_trainable = True
       if set_trainable:
           layer.trainable = True
       else:
           layer.trainable = False
   ```

5. 可视化CNN

   （1）可视化中间层的输出（activations）

   （2）Visualizing convnet filters，没看懂

   （3）Visualizing heatmaps of class activation，没看懂 CS231N 回头去学习

## 6. Sequence Model

1. 不会采用n-grams，只会采用1-gram-one-hot以及embedding，原因是n-grams可以被model学出来

2. 预处理text时可以采用keras自带的工具，很好用，可以指定词表大小并预处理文本

   ```python
   from keras.preprocessing.text import Tokenizer

   samples = ['The cat sat on the mat.', 'The dog ate my homework.']

   # We create a tokenizer, configured to only take
   # into account the top-1000 most common words
   tokenizer = Tokenizer(num_words=1000)
   # This builds the word index
   tokenizer.fit_on_texts(samples)

   # This turns strings into lists of integer indices.
   sequences = tokenizer.texts_to_sequences(samples)

   # You could also directly get the one-hot binary representations.
   # Note that other vectorization modes than one-hot encoding are supported!
   one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')

   # This is how you can recover the word index that was computed
   word_index = tokenizer.word_index
   print('Found %s unique tokens.' % len(word_index))
   ```

3. 当词表非常大的时候，可以采用one-hot hashing trick

   这甚至都不需要词表，就可以把text给encoding

