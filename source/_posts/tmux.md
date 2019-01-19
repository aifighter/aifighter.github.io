---
title: tmux简易攻略
comments: true
mathjax: true
date: 2019-01-18 16:00:00
categories:
- 开发
tags:
- 命令行
description: tmux命令行工具最简单使用攻略
---

tmux是终端复用命令行工具，可以在一个terminal下开多个窗口。tmux的功能比较强大，这里我只记录了最少的功能。

![tmux](/images/tmux.png)

**tmux所有操作均在^b之后进行**(^是ctrl键)

- `%`：左右分出两个窗格
- `"`：上下分出两个窗格
- `x`：关闭当前窗格
- `space`：切换窗格布局
- `上下左右`：切换窗格
- `q`：显示所有窗格的序号，在序号出现期间按下对应的数字，即可跳转至对应的窗格

除了窗格之外，还有窗口的概念，不过个人感觉可以不用，窗格是在窗口下的

- `c`：新建窗口
- `p`：上一个窗口
- `n`：下一个窗口
- `&`：关闭当前窗口

感觉这么多够用了，以后需要再补

- `d`: 退出tmux



[十分钟学会tmux](https://www.cnblogs.com/kaiye/p/6275207.html)