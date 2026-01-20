"""
    该案例演示了装饰器
"""
from codecs import replace_errors

"""
# 如果没有装饰器，有些函数的功能可能不太完善
from math import sqrt

# 开根号
def func(n):
    return sqrt(n)
print(func(-4))
"""
"""
# 通过闭包实现装饰器  完善开根号的函数
from math import sqrt

def decorator(f):
    def inner(n):
        n = abs(n)
        res = f(n)
        return res
    return inner

# 开根号
def func(n):
    return sqrt(n)

# print(func(-4))

inn = decorator(func)
print(inn(-4))
"""
"""
# 通过装饰器语法糖---实现装饰器功能
from math import sqrt

def decorator(f):
    def inner(n):
        n = abs(n)
        res = f(n)
        return res
    return inner

# 开根号
@decorator
def func(n):
    return sqrt(n)

print(func(-4))
"""
"""
# 多层装饰器---装饰器语法糖
from math import sqrt

#第一层装饰  --- 加求绝对值功能
def get_abs(f):
    def inner(n):
        n = abs(n)
        res = f(n)
        return res
    return inner

# 第二层装饰 --- 将结果转换为整数
def get_int(f):
    def inner(n):
        res = f(n)
        res = int(res)
        return res
    return inner

# 开根号
@get_int
@get_abs
def func(n):
    return sqrt(n)

print(func(-4))
"""
"""
# 多层装饰器---手动调用
from math import sqrt

#第一层装饰  --- 加求绝对值功能
def get_abs(f):
    def inner(n):
        n = abs(n)
        res = f(n)
        return res
    return inner

# 第二层装饰 --- 将结果转换为整数
def get_int(f):
    def inner(n):
        res = f(n)
        res = int(res)
        return res
    return inner

# 开根号
def func(n):
    return sqrt(n)

abs_in = get_abs(func)
int_in = get_int(abs_in)

print(int_in(-4))
"""
"""
# 带参数的装饰器
from math import sqrt

def times(count):
    # 装饰 先求绝对值，再开根号
    def get_abs(f):
        def inner(n):
            n = abs(n)
            for i in range(count):
                n = f(n)
            return n
        return inner
    return get_abs

# 开根号
@times(2) # times(2)(func)
def func(n):
    return sqrt(n)

print(func(-16))
"""

from math import sqrt

# 类装饰器
class DecoratorClass:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        x = abs(x)
        return self.f(x)

@DecoratorClass
def func(n):
    return sqrt(n)

# myC = DecoratorClass(func)
# print(myC.__call__(-4))

print(func(-16))
