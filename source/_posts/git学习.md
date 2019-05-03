---
title: git学习
urlname: lub96et7
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
手动处理conficts
git merge --continue
```

如何对分支设置upstream？这样pull的时候就不用指定分支了

```
git branch -vv 查看当前本地分支与remote映射关系
git branch -u origin/dev dev 对dev分支设置upstream为origin/dev
```

如何暂存修改？

```
git stash save "some comment" 或者 git stash
跳转到其他分支做一系列操作，再回来
git stash list 查看stash的list，里面有stash的名字
git stash apply stash@{0} apply后面加上stash的名字（不加默认是最新一个）
```

如何merge某个分支的某个commit？

这个commit必须是别的分支中的某个另外的commit，不然好像没什么意义。

```
git cherry-pick {commit-id} 相当于把这个commit-id拉过来merge
处理冲突
git cherry-pick --continue 相当于commit了，会生成一次commit记录
(git cherry-pick --abort) 中途停止cherry-pick
```

如何撤销某次commit？

revert做的事情是把某次commit做的事情反着来一遍，不是回到某次commit，不一样的。

```
git revert {commit-id}
处理冲突（如果存在）
git revert --continue
```

如何将多个commit合并？

```
git rebase -i {开始commit-id} {结束commit-id}
按照提示做，修复冲突
git rebase --continue
```

如何挽救一次错误操作？

```
git reflog 找到对应的commit号
git reset {commit-id}
```

