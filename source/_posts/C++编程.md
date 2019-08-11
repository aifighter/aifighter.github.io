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

`students`是`vector<Student_info>`

`students.erase(students.begin() + i);`

erase本身是`O(N)`的，因为它需要把后面的元素一个个往前挪一格

### vector的random access和sequential access

students[i]实际上是一种random access，因为可以任意访问某一个元素

如果只能顺序访问，那么效率也会提升，就需要使用iterator

### iterator

iterator和size_type一样都是在vector的namespace里

有两种方法可以定义container-type的iterator（vector是一种container）

`container-type::const_iterator`

`container-type::iterator`

之前的`students.begin()`和`students.end()`实际上返回的都是iterator，它支持`+`的重载

iterator只是对应变量的地址，要访问实际的变量，需要用dereference运算符`*`来访问

```c++
vector<double> vec;
vec.push_back(1);
vec.push_back(2);
vector<double>::const_iterator iter = vec.begin();
cout << vec[0] << *iter << *(iter + 1) <<endl; 
```

**syntax sugar**：若iter是一个iterator，并且指向的是一个struct，那么可以用`iter->name`代替`(*iter).name`

`iter = students.erase(iter);`

可以在删除iter后返回iter之后的元素位置

### list

用法和vector几乎一模一样，除了不能random_access。

list不支持`<algorithm>`中的sort方法

```c++
list<Student_info> students; 
students.sort(compare);
```

它的erase和push_back效率高于vector，然而顺序访问的效率上，vector要更佳

### `<cctype>`

这个header定义了许多与char相关的操作例如isspace，isalpha等等

### string的类似container的操作

string的很多操作和container类似，比如iterator，通过index访问等等。

另外，string的substr(a, b)截取一段substring

### getline读取一行输入

在`<string>`中定义

`getline(cin, s)`

### vector的insert方法

`a.insert(a.end(), b.begin(), b.end())`

在`a.end()`前插入`[b.begin, b.end())`的所有元素

`a.insert(a.end(), c)`

在`a.end()`前插入c

### container的其他方法

`container<T> c(c2);`定义一个新的container，是c2的复制

`container<T> c(n, t); `n个element，均为c

`container<T> c(b, e); `传入iterator，container的元素是[b, e)的值

`c.erase(b, e)`

### vector的其他方法

`v.reverse()`

`v.resize(n)`

# 6. Using library algorithms

### genetic algorithm

泛型算法，不属于某个特定的数据类型

例如`copy(begin, end, out);`等价于`while (begin != end) *out++ = *begin++;`

### iterator adaptor

`back_inserter(ret)`，ret是一个container，返回一个用于插入的iterator。

例：`copy(bottom.begin(), bottom.end(), back_inserter(ret));`

错误1：`copy(bottom.begin(), bottom.end(), ret);`

错误2：`copy(bottom.begin(), bottom.end(), ret.end());`

这个操作等同于

`ret.insert(ret.end(), bottom.begin(), bottom.end());`

其他还有（c是container，it是itereator）

`front_inserter(c)`

`inserter(c, it) `

### `<algorithm>`中的部分方法

1. find_if

   `InputIterator find_if (InputIterator first, InputIterator last, UnaryPredicate pred)`

   从first到last中第一个满足`pred(*i)`的iter并返回

2. equal

   `bool equal ( InputIterator1 first1, InputIterator1 last1, InputIterator2 first2 )`

   判断两个序列是否相等，第二个序列不需要给end

   `container.rend()`返回一个从末尾开始往前走的iter，因此`equal(s.begin(), s.end(), s.rbegin())`可以用来判断一个string是否回文

3. find

   `InputIterator find (InputIterator first, InputIterator last, const T& val)`

   类似find_if，直接找对应元素

4. search

   `ForwardIterator1 search ( ForwardIterator1 first1, ForwardIterator1 last1, ForwardIterator2 first2, ForwardIterator2 last2)`

   从1中找到2，并返回begin

5. transform

   `transform(students.begin(), students.end(), back_inserter(grades), grade);`

   有点类似apply，对students的每个element执行grade函数，结果插入到grades中

   这里grade重载过，所以需要写一个辅助函数来代替grade

6. accumulate

   `T accumulate (InputIterator first, InputIterator last, T init)`

   定义在`<numeric>`中，用于累加

7. remove_copy

   ```c++
   OutputIterator remove_copy(InputIterator first, InputIterator last, 
                              OutputIterator result, const T& val);
   ```

   把序列中和val相同的去除，其他插入result中

8. 删除vector中满足某条件的元素

   ```c++
   students.erase(remove_if(students.begin()), students.end(),
                  fgrade), students.end());
   ```

   remove_if 会把数组中满足fgrade的数据位置处填入后面的需保留数据，然后将iterator放在需保留数据后面，后面的数据并不会删除。再调用erase即可删除数据。

9. stable_partition

   `stable_partition(students.begin(), students.end(), pgrade);`

   把满足pgrade的放前面，不满足的放后面，返回分割处的iterator

10. algorithm往往不改变container而是作用于container中的元素

### static

static storage class specifier：变量存入静态区，在main函数执行完毕再清除

```c++
bool not_url_char(char c) {
    static const string url_ch = "~;/?:@=&$-_.+!*'(),";
    //...
}
```

在上面的函数中，url_ch不会反复创建，仅在第一次调用函数时创建，作用域依然只是这个函数。

### beg[-1]，i[sep.size()]

begin是一个iterator：那么`beg[-1]`即为`*(beg - 1)`

`i[sep.size()]`即为`*(i + sep.size())`

### 向函数传参函数

```c++
void write_analysis(ostream& out, const string& name, 
                    double analysis(const vector<Student_info>&),
                    const vector<Student_info>& did,
                    const vector<Student_info>& didnt)
```

# 7. Using associative containers

### map

类似于python中的dict，`map<string, int> counters`

`counters[s]`会自动插入一个element

map的iterator本质上是pair，可以通过`it->first`访问key，`it->second`访问对应的值

访问

某一个key的时候，不要用counters[s]，因为若不存在key s，会创建一个新key

而是用

```c++
Grammar::const_iterator it = g.find(word); 
if (it == g.end())
    throw logic_error("empty rule");
```

尽管associative containers不是最快的，但是已经足够优秀

# 8. Writing generic functions

### Template Functions

```c++
template<class T>
T median(vector<T> v) {
    typedef typename vector<T>::size_type vec_sz;
    vec_sz size = v.size(); 
    if (size == 0)
        throw domain_error("median of an empty vector");
    sort(v.begin(), v.end());
    vec_sz mid = size/2;
    return size % 2 == 0 ? (v[mid] + v[mid-1]) / 2 : v[mid]; 
}
```

1. 在调用的时候，直接`median(param1)`即可。
2. 若传参中不包含T而仅仅返回值带T，那么编译器将无法推断T是什么。因此需要这样调用`median<double>(param1)`
3. 在函数中使用类似`vector<T>::size_type`的type时前面要加上typename关键词

### 5种iterators

![5种iterators的区别](/images/iterators.jpg)

`std::back_inserter`生成的是一种特殊的output iterator，可以在后面插入

