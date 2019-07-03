---
title: C++编程
urlname: fwncrf6q
comments: true
mathjax: true
date: 2019-06-27 14:15:00
categories:
- 开发
tags:
- C++
description: 重新学习一下C++编程
---

# 3. Working with batches of data

### `<iomanip>`

包含了`std::setprecision`，它是一种manipulator，用于IO中，用法和`std::endl`一样。`std::endl`也是一种manipulator，但是用于太常用放在了`<iostream>`中。

### `cin >> midterm >> final;`

由于`>>`运算符是左结合，而且返回左operand。所以上面的代码和`cin >> midterm; cin >> final;`是一样的。

### string literal以空格隔开默认会concat

`"abc" "def"`等价于`"abcdef"`，即使以回车隔开也是等价的。在C++代码中空格换行等都是一样的。代码以分号或者花括号分割。

### `while (cin >> x)`

`cin >> x`返回的是cin，是istream类型，而cin在条件语句中会被转换为bool。在内部实现中，上一次读入成功则会成为true，否则为false。