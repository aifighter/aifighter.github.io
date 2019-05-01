---
title: git学习
comments: true
mathjax: true
date: 2019-01-21 23:38:00
categories:
- 开发
tags:
- 命令行
description: 学习好git，不怕代码找不到啦
---

如何checkout远程分支？

```
git fetch origin 先fetch远程信息
git branch -a   查看远程分支
git checkout -b xxxx（本地分支名称） yyyy(上条命令查找到的远程分支的名称)
```

如何checkout出某个版本的单个文件？

```
git checkout filename 相当于撤销对该文件的修改
git checkout HEAD~1 filename 某个文件回到上个版本
git checkout HEAD~10 filename 某个文件回到10个版本前
```

如何merge远程分支？

```
git fetch
git merge origin/dev
手动处理conficts再commit
```

如何对分支设置upstream？这样pull的时候就不用指定分支了

```
git branch -vv 查看当前本地分支与remote映射关系
git branch -u origin/dev dev 对dev分支设置upstream为origin/dev
```

