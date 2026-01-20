
"""
    该案例演示了模块的导入
"""
"""
# 全局导入   没有起别名
import P01_My_Add

print(P01_My_Add.num)
print(P01_My_Add.add(10, 20))
"""
"""
# 全局导入  起别名
import P01_My_Add as ma
print(ma.num)
print(ma.add(10, 20))
"""
"""
# 局部导入   from 模块名 import 成员1 [as 别名1],成员2 [as 别名2]...
# 只能调用导入的成员，没有导入的成员不能访问
from P03_My_Multi import mutil

print(num)
print(mutil(10, 20))
"""
"""
# 局部导入 from 模块名 import 成员1 [as 别名1],成员2 [as 别名2]...
# 对于重名成员，后导入的会将先导入的覆盖掉
from P03_My_Multi import num
from P01_My_Add import num,add
print(num)
"""
"""
# 局部导入 from 模块名 import 成员1 [as 别名1],成员2 [as 别名2]...
# 通过别名区分不同模块的变量
from P01_My_Add import num as n1
from P03_My_Multi import num as n2
print(n1)
print(n2)
"""
"""
# 局部导入   from 模块名 import *
# 导入所有不以_开头的成员 
from P03_My_Multi import *
print(num)
print(mutil(10,20))
print(_str1)
"""
"""
# 模块导入顺序
import sys
print(sys.path)
sys.path.append("D:/")
print(sys.path)
"""
"""
# 局部导入 from 模块名 import *
# __all__ 限制可以导入的成员
from P01_My_Add import *
print(num)
# print(num1)
# print(_str1)
print(add(10,20))
"""
"""
# 使用全局导入  _开头以及__all__限制都不起作用
import P01_My_Add
print(P01_My_Add.num)
print(P01_My_Add.num1)
print(P01_My_Add._str1)
print(P01_My_Add.add(10,20))
"""
"""
# 疑问：from decimal import Decimal   导入的是_decimal下的成员Decimal

# from P01_My_Add import add
# import P01_My_Add
from P01_My_Add import *
"""
"""
# dir()
import math

print(dir(math))
class MyClass:
    def __init__(self):
        self.x = 1
        self.y = 2

    def method1(self):
        pass
obj = MyClass()
print(dir(obj))

num1 = 10
def add(a,b):
    pass
class MyClass:
    pass
print(dir())
"""



