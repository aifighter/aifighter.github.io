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

# 4. Organizing programs and data

### call by value

`double grade(double midterm, double final, double homework) `

传入的参数相当于是给函数中的变量赋了初值，因此不会改变原始值，scope只在函数内，结束就销毁了

### throw exception

`throw domain_error("median of an empty vector");`

抛出异常，domain_error是定义在`<stdexcept>`中的

### &与函数传参

`double grade(double midterm, double final, const vector<double>& hw) `

首先&代表了reference，hw相当于给了传入参数的别名，修改hw会直接修改传入参数。加入了const的话就意味着hw不能被修改（不代表原变量一定也是const）。

`double median(vector<double> vec) `

上面这种会传入一份vector的拷贝，也不会修改传入值

### overloading

函数的参数类型数量不同可以实现同名函数的重载。返回类型不同的函数**不能**重载。

### 函数返回&

意味着函数返回的是return后面的东西，而不是它的复制，可以理解成返回的是给一个新的初值为return值的reference

### `cin.clear()`

即`istream.clear()`，确保可以正常获取输入

### `hw.clear()`

hw是`vector<double>`，作用是清空已有数据

### lvalue

即有名字的变量，可以被访问的，例如1，"abc"这些就不是lvalue，当使用reference传递的函数（并且我们想要修改传入的参数）时，不要传入lvalue，否则我们将无妨访问得到的修改。

`istream& read_hw(istream& in, vector<double>& hw) `

这里传入的hw必须是一个lvalue

### try..catch

可以配合函数中的throw使用

```c++
try {
    ...
} catch (domain_error) {
    ...
}
```

用下面的方法可以输出error中的信息

```c++
catch (domain_error e) {
    cout << e.what();
}
```

### struct

```c++
struct Student_info { 
    string name;
    double midterm, final;
    vector<double> homework;
};
```

### 对vector<Student_info>排序

```c++
bool compare(const Student_info& x, const Student_info& y) {
    return x.name < y.name; 
}
sort(students.begin(), students.end(), compare);
```

### header file 

在median.h中，放入函数的声明，以及最小限度的include，不要使用using（因为不确定其他include该头文件的文件是不是想要使用using，此外，函数参数不需要变量名。

此外第1，2及最后1行的写法可以防止该文件被多次include。

```c++
#ifndef GUARD_median_h 
#define GUARD_median_h
#include <vector>
double median(std::vector<double>);
#endif
```

系统的头例如`#include <vector>`不一定是以头文件形式存在的。

### source file

在source file中的using只是local的，不会被其他引入了对应的.h文件的source file所引入

### inline

函数前加入inline，是为了避免频繁调用函数对栈内存重复开辟所带来的消耗。

```c++
inline char* dbtest(int a) {
    return (i % 2 > 0) ? "奇" : "偶";
} 
```

# 5. Using sequential containers and analyzing strings

### vector的erace()方法

`students.erase(students.begin() + i);`

这个方法的时间复杂度是$O(N^2)$，非常耗时

