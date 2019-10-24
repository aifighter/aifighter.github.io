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

下面的写法可以catch任意的error

```c++
try {
    ...
} catch (...) {
    ...
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

# 9. Defining new types

### `::`与`.`

`::` 用在type的member上，比如`Student_info::read`

`.` 用在某个instance上，比如`s.read`

### constant member function

`double Student_info::grade() const { ... }`

此类函数确保不会修改成员变量

constant的对象可以call constant member function而不能call非constant的

### struct与class的区别

struct中默认是public

class的默认是private

```c++
// 以下两个等价
struct Student_info { 
    private:
    std::string name;
    public:
    double grade() const;
};
class Student_info { 
    std::string name;
    public:
    double grade() const; 
};
```

### class constructor

`Student_info::Student_info(): midterm(0), final(0) { }`

对于Student_info类中，若不定义构造函数，那么成员变量将会被初始化：

（1）built-in type如midterm和final这两个浮点数将会被初始化为内存中的随机值

（2）其他类的object将会被使用该类的默认构造函数构造，如string和vector，将会被初始化成空string和空vector

为了让类的成员变量都被初始化成有意义的值，可以使用上面的写法

# 10. Managing memory and low-level data structures

### Pointer

A pointer is a value that represents the address of an object.

```c++
int x = 5;
int* p = &x;
*p = 6;
```

### Pointers to functions

一般不需要用*号，因为c++会自动将不传参的函数名认为是取地址

```c++
int next(int n) 
{
    return n + 1; 
}
// these two statements are equivalent 
fp = &next;
fp = next;
// these two statements are equivalent 
i = (*fp)(i);
i = fp(i);
// these two statements are equivalent 
double analysis(const vector<Student_info>&)
double (*analysis)(const vector<Student_info>&)
```

### Arrays

>  "a pointer is a random-access iterator"

`p[n]` 等价于 `*(p + n)`

```c++
double coords[NDim];
*coords = 1.5;
*(coords+1) = 2;
vector<double> v;
copy(coords, coords + NDim, back_inserter(v));
const int month_lengths[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
```

### string literal

等价于下面这个

`const char hello[] = { 'H', 'e', 'l', 'l', 'o', '\0' };`

### sizeof

`static const size_t ngrades = sizeof(numbers)/sizeof(*numbers); `

sizeof是获得对象的大小，以bytes计

size_t是sizeof返回的类型

### "?\?\?"

在C++中，字符串中不能连续出现两个问号，需要这样。

### 给main函数传参

`int main(int argc, char** argv)`

argc是传入的参数的个数，argv是指向char*的数组，其中第一个参数是命令自身

用法` ./cmake-build-debug/accelerated_cpp hello c`

### 读写文件

```c++
ifstream infile("in");
ofstream outfile("out");
string s;
while (getline(in, s)) {
    outfile << s << endl;
}
```

### cerr和clog

都是往std error写东西的，用法和cout差不多

### 3种内存分配

1. automatic memory management

   用于local variable

   ```c++
   int* invalid_pointer()
   {
       int x; // 前面加static的话则不会有问题
       return &x; // instant disaster! 
   }
   ```

2. static allocate

   用static关键词，一次分配，直到程序结束时永久有效

3. dynamic allocate

   任意时候删除

### new delete

1. object

   `p = new T(args)`

   分配一个object T并且把指向T的指针返回，括号内的值可以用来初始化这个object

   `delete p `

2. 数组array

   `T* p = new T[n]`

   `delete[] p`

   delete后面的括号是告诉compiler要删除整个数组而不是首个元素

### array和指向array的指针的区别

```c++
double a[] = {1,2};
delete[] a; // 不可以
double* b = new double[2];
delete[] b; // 可以
```

# 11. Defining abstract data types

这一章构建了一个Vec类，功能类似于vector

### explicit

构造函数前加入explicit可以阻止不应该允许的经过转换构造函数进行的隐式转换的发生

`explicit Vec(size_type n, const T& val = T()) { create(n, val); }`

它阻止了这样的写法：

`Vec a = 10`

确保了这种构造函数只能这样调用

`Vec a(10)`或者`Vec a = Vec(10)`

### 用typedef来增加模版类的可读性

```c++
template <class T> class Vec { 
public:
    typedef T* iterator;
    typedef const T* const_iterator; 
    typedef size_t size_type; 
    typedef T value_type;
    
	Vec() { create(); }
	explicit Vec(size_type n, const T& val = T()) { create(n, val); }
    
    size_type size() const { return limit - data; }
    T& operator[](size_type i) { return data[i]; }
    const T& operator[](size_type i) const { return data[i]; }
    
    // new functions to return iterators
	iterator begin() { return data; } 
    const_iterator begin() const { return data; }
	iterator end() { return limit; } 
    const_iterator end() const { return limit; }

private:
    iterator data;
    iterator limit;
};
```

###  size()

返回的type是size_type，虽然我们return了一个int，但是最后会自动做好转换的

### 重载index

回顾一下在函数定义前加入const的含义是只有const类型的object才会调用这个函数

同时这个函数返回引用，可以做修改成员值的功能

### 复制构造函数 copy constructor

```c++
Vec(const Vec& v) { create(v.begin(), v.end()); }
```

接收的参数是一个constant的reference

它的作用是在以下的场景中被用到，在vector中，下面的b和a会是不相关的两个object

```c++
vector<int> b = a;
median(a);
```

### 赋值运算符 assignment operator

`operator=`

赋值运算符，用于给一个已经存在的operator赋上新的值，举个例子 

```c++
string a = "cbc"; // implicit，寻找参数为const char*的constructor，explicit就是避免这种用法
string b = a; // copy constructor
string c; // default constructor
c = a; // assignment operator
```

```c++
template <class T>
Vec<T>& Vec<T>::operator=(const Vec& rhs) {
    // check for self-assignment
    if (&rhs != this) {
        // free the array in the left-hand side
        uncreate();
        // copy elements from the right-hand to the left-hand side
        create(rhs.begin(), rhs.end());
    }
    return *this;
}
```

上面的函数定义不是在header中的，那么`Vec<T>`不能被略写成`Vec`

### this

在c++中的类定义中，this指的是这个类的object的指针

### 析构函数 destructor

```c++
template <class T> class Vec { 
public:
    ~Vec() { uncreate(); }
    // as before 
};
```

何时会调用析构函数：（1）out of scope （2）delete动态创建的指针

### 默认函数

constructor，destructor，copy constructor，assignment operator都有默认的实现

### Rule of three

> If your class needs a destructor, it probably needs a copy constructor and an assignment
> operator too.

在Vec这个例子中，一定是需要destructor的，因为默认的destructor会做这样的事情：

```c++
delete data;
delete limit;
```

这样子是删除不干净数据的。

rule of three 告诉我们同时也要定义一下copy constructor and assignment operator

### 实现push_back

策略是当空间不够用时double一下

```c++
void push_back(const T& t) { 
    if (avail == limit)
        grow();
    unchecked_append(t);
}
// 之前定义的data和limit就不够用了，加一个avail指向有数据的last element
iterator data; // first element in the Vec
iterator avail; // (one past) the last element in the Vec 
iterator limit; // (one past) the allocated memory
```

### `<memory>`中的allocator类

new和delete在分配空间时会使用默认构造函数来构造对象，有时会浪费性能

allocator类可以只分配空间不初始化

```c++
template<class T> class allocator { 
public:
    T* allocate(size_t);
    void deallocate(T*, size_t); 
    void construct(T*, const T&); 
    void destroy(T*);
    // ... 
};
template<class Out, class T> void uninitialized_fill(Out, Out, const T&); 
template<class In, class Out> Out uninitialized_copy(In, In, Out);
```

### 整个Vec类的实现

三个构造函数，注意c++的指针为0意味着空指针

```c++
template <class T> void Vec<T>::create() {
    data = avail = limit = 0; 
}
template <class T> void Vec<T>::create(size_type n, const T& val) {
    data = alloc.allocate(n);
    limit = avail = data + n; 
    uninitialized_fill(data, limit, val);
}
template <class T> void Vec<T>::create(const_iterator i, const_iterator j) {
    data = alloc.allocate(j - i);
    limit = avail = uninitialized_copy(i, j, data); 
}
```

析构函数

```c++
template <class T> void Vec<T>::uncreate() {
    if (data) {
        // destroy (in reverse order) the elements that were constructed 
        iterator it = avail;
        while (it != data)
            alloc.destroy(--it);
		// return all the space that was allocated 
        alloc.deallocate(data, limit - data);
    }
    // reset pointers to indicate that the Vec is empty again 
    data = limit = avail = 0;
}
```

push_back中用到的函数

```c++
template <class T> void Vec<T>::grow() {
    // when growing, allocate twice as much space as currently in use 
    size_type new_size = max(2 * (limit - data), ptrdiff_t(1)); // ptrdiff_t是各式转换7u75
    // allocate new space and copy existing elements to the new space 
    iterator new_data = alloc.allocate(new_size);
    iterator new_avail = uninitialized_copy(data, avail, new_data);
    // return the old space
    uncreate();
    // reset pointers to point to the newly allocated space 
    data = new_data;
    avail = new_avail;
    limit = data + new_size;
}
// assumes avail points at allocated, but uninitialized space 
template <class T> void Vec<T>::unchecked_append(const T& val) {
    alloc.construct(avail++, val); 
}
```

# 12. Making class objects act like values

### virtual, final, override

virtual意味着父类指针可以指向子类方法

final的类不能被继承，final的方法不能被重写

纯虚函数：virtual method()=0; 必须被重写

override就是被重写的方法

### 自动类型转换

带有单个参数的constructor就是自动类型转换所调用的函数

如果构造函数不想被用于默认转换，那么可以加上explicit关键词

```c++
double d = 10;
double d2;
d2 = 10; 
// 下面的函数就是会将string literal转换成Str
Str(const char* cp) {
    std::copy(cp, cp + std::strlen(cp), std::back_inserter(data)); 
}

```



