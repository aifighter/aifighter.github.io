---
title: Python面向对象编程
urlname: gqkvutfq
comments: true
mathjax: true
date: 2019-01-17 13:53:00
categories:
- 开发
tags:
- Python
description: 平时用到面向对象的编程比较多一些，记录一些平时没太关注的东西
---

### `__new__()`

类的实例化首先调用`__new__`创建对象，再调用`__init__`初始化对象，object类是所有类的父类

### 实例属性

一般不建议在`__init__`外定义实例属性

### 类属性

```python
class A:
    a = 10
```

### 私有属性

双下划线：类外无法访问

单下划线：只是一个标注，没有实际作用

### 三个内置函数

```python
hasattr(str, "__len__") # 用来判断一个类（实例）是否拥有某个属性（方法）
setattr(Animal, "age", 8) # 用来设定属性或方法的值
getattr(dog, "age", 404) # 用来获取属性（方法），若没有改属性（方法）则返回第三个
```

### @property

@property可以让类的方法像属性一样被调用，主要可以用在入参检验上

```python
class Student(object):
    def __init__(self, birth):
        self._birth = birth
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth
```

### 类方法，静态方法

类方法和静态方法都用于与类相关，但不依赖或改变类与实例

类方法可以用来创建类的实例，静态方法则不适合（因为静态方法需要硬编码类名）

如：

```python
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    @classmethod
    def get_instance_with_c(self, a, c):
        b = c * 2
        return cls(a, b)
```

