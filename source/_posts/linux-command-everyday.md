---
title: 每天一个linux命令
comments: true
mathjax: true
date: 2019-01-19 18:57:00
categories:
- 开发
tags:
- 命令行
description: 每天学习一个实用的linux命令，争取日更
---

### 20180119: ls 

只记录几个看着比较有用的参数

`-a` 显示所有隐藏文件

`-h` human readable

`-l` 显示详细信息

`-R` recursive显示

`-t` 按时间排序

`-F` 在folder后面加上`\`

一些例子：

1. 仅列出文件夹的详细信息

   `ls -l | grep "^d"`

[每天一个linux命令(1)：ls命令](https://www.cnblogs.com/peida/archive/2012/10/23/2734829.html)

---

### 20180120: cd

大部分操作都知道，下面这个小技巧很实用

`cd -`：回到上一个目录

[每天一个linux命令(2)：cd命令](https://www.cnblogs.com/peida/archive/2012/10/24/2736501.html)

---

### 20180121: pwd

一般不加任何参数

[每天一个linux命令（3）：pwd命令](https://www.cnblogs.com/peida/archive/2012/10/24/2737730.html)

---

### 20180122: mkdir

创建目录

`-p`：可以输入一个完整路径，路径中不存在的文件夹都会创建

`-v`：创建的时候输出信息

`-m`：创建的时候设置权限，类似chmod

[每天一个linux命令（4）：mkdir命令](https://www.cnblogs.com/peida/archive/2012/10/25/2738271.html)

---

### 20180123: rm

删除文件或目录

`-f`：force，不给出提示，忽略不存在的文件

`-r`：recursive删除，会删除目录

`-i`：交互式删除，会给出提示

`-v`：显示详细步骤

[每天一个linux命令（5）：rm 命令](https://www.cnblogs.com/peida/archive/2012/10/26/2740521.html)

---

### 20180124: rmdir

用于删除一个空的目录

[每天一个linux命令（6）：rmdir 命令](https://www.cnblogs.com/peida/archive/2012/10/27/2742076.html)

---

### 20180125: mv

当第二个参数类型是文件时，mv命令完成文件重命名。

当第二个参数是已存在的目录名称时，源文件或目录参数可以有多个，mv命令将各参数指定的源文件均移至目标目录中。

-u ：若目标文件已经存在，且 source 比较新，才会更新(update)

[每天一个linux命令（7）：mv命令](https://www.cnblogs.com/peida/archive/2012/10/27/2743022.html)

---

### 20180126: cp

`-n`：不要覆盖已存在的文件(使前面的 -i 选项失效)

[每天一个linux命令（8）：cp 命令](https://www.cnblogs.com/peida/archive/2012/10/29/2744185.html)

---

### 20180127: touch

touch命令用来更改文件的时间戳，若文件不存在则创建文件

`-t`：可以指定时间戳

`touch -t 201211142234.50 log.log`

[每天一个linux命令（9）：touch 命令](https://www.cnblogs.com/peida/archive/2012/10/30/2745714.html)

---

### 20180128: cat

cat 用于输出文件

`cat a.txt b.txt`会在屏幕上将文件都print出来，配合`>,>>`使用可以实现合并文件的操作

`-n`：加上行号

[每天一个linux命令（10）：cat 命令](https://www.cnblogs.com/peida/archive/2012/10/30/2746968.html)

---

### 20180129: nl

nl用于在给文件加上行号，并输出，支持的格式会比cat -n多一些。感觉用处不大

`nl test.txt`

[每天一个linux命令(11)：nl命令](https://www.cnblogs.com/peida/archive/2012/11/01/2749048.html)

---

### 20180130: more

more命令也是用来查看文件的，可以支持翻页等操作

似乎只要记住一种查看文件的方式就好了，不用记那么多

[每天一个linux命令(12)：more命令](https://www.cnblogs.com/peida/archive/2012/11/02/2750588.html)

---

### 20190218: less

less命令也是用来查看文件的

也可以用管道的

在less中，`/字符串`进行向后搜索，`?字符串`进行向前搜索

例子：

`history | less`

[每天一个linux命令（13）：less 命令](https://www.cnblogs.com/peida/archive/2012/11/05/2754477.html)

---

### 20190221: head

`head -n 5 sample.txt`

[每天一个linux命令（14）：head 命令](https://www.cnblogs.com/peida/archive/2012/11/06/2756278.html)

---

### 20190222: tail

`tail -f sample.txt`

`tail -n 5 sample.txt`

-f 可以用来查看正在更新的日志

[每天一个linux命令（15）：tail 命令](https://www.cnblogs.com/peida/archive/2012/11/07/2758084.html)

