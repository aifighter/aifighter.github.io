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

## 本章代码

```c++
#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::setprecision;
using std::sort;
using std::streamsize;
using std::string;
using std::vector;


int main() {
    cout << "Please enter your midterm and final exam grades: ";
    double midterm, final;
    cin >> midterm >> final;

    cout << "Enter all your homework grades, "
            "followed by end-of-file: ";
    vector<double> homework;
    double x;
    while (cin >> x)
        homework.push_back(x);

    typedef vector<double>::size_type vec_sz;
    vec_sz size = homework.size();
    if (size == 0) {
        cout << endl << "You must enter your grades. "
                        "Please try again." << endl;
        return 1;
    }
    sort(homework.begin(), homework.end());
    vec_sz mid = size / 2;
    double median;
    median = size % 2 == 0 ? (homework[mid] + homework[mid - 1]) / 2 : homework[mid];

    streamsize prec = cout.precision();
    cout << "Your final grade is " << setprecision(3)
         << 0.2 * midterm + 0.4 * final + 0.4 * median << setprecision(prec) << endl;
    return 0;
}
```



### `<iomanip>`

包含了`std::setprecision`，它是一种manipulator，用于IO中，用法和`std::endl`一样。`std::endl`也是一种manipulator，但是用于太常用放在了`<iostream>`中。

### `cin >> midterm >> final;`

由于`>>`运算符是左结合，而且返回左operand。所以上面的代码和`cin >> midterm; cin >> final;`是一样的。

### string literal以空格隔开默认会concat

`"abc" "def"`等价于`"abcdef"`，即使以回车隔开也是等价的。在C++代码中空格换行等都是一样的。代码以分号或者花括号分割。

### `while (cin >> x)`

`cin >> x`返回的是cin，是istream类型，而cin在条件语句中会被转换为bool。在内部实现中，上一次读入成功则会成为true，否则为false。

### `vector<double>::size_type`

由于我们不能确定某个类型的size()返回的是什么类型，所以使用该类型的size_type是一个好的方法

### typedef

`typedef vector<double>::size_type vec_sz;`

用来给某种类型一个别名

### `sort(homework.begin(), homework.end());`

对vector进行排序需要提供开始位和结束位，升序排列，inplace操作

### `streamsize prec = cout.precision();`

可以获取到目前cout的精度，steamsize是`<ios>`中提供的

