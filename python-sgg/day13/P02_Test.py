
"""
# import P01_math_operations as op
# from P01_math_operations import add,mult
from P01_math_operations import *

print(add(3, 5))
print(mult(3, 5))
"""
"""
# 使用生成器表达式创建一个生成器，生成 1 到 10 的偶数。然后使用for循环遍历该生成器，打印每个偶数。
gen = (x for x in range(1,11) if x % 2 == 0)
for x in gen:
    print(x)
"""
"""
创建一个迭代器类MyIterator，用于遍历一个给定列表的元素。实现__iter__和__next__方法。
使用该迭代器类遍历列表[10, 20, 30, 40]，并打印每个元素。
"""
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            value = self.data[self.index]
            self.index += 1
            return value

it = MyIterator([10, 20, 30, 40])

for x in it:
    print(x)




