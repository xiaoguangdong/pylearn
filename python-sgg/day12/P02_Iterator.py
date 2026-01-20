"""
    该案例演示了迭代器
"""
from collections.abc import Iterable, Iterator

"""
# 演示大部分容器类型都是可以通过for进行遍历的，我们称其为可迭代类型(Iterable)
import os

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {"one": 1, "two": 2}:
    print(key)
for char in "123":
    print(char)

with open("myfile.txt", "w") as f:
    f.write("H\ne\nl\nl\no\n \nW\no\nr\nl\nd\n")
for line in open("myfile.txt"):
    print(line, end="")
os.remove("myfile.txt")
"""
"""
from collections.abc import Iterable
# 判断是否为可迭代类型
print(isinstance([], Iterable)) # True
print(isinstance((), Iterable)) # True
print(isinstance(set(), Iterable)) # True
print(isinstance({}, Iterable)) # True
print(isinstance("abc", Iterable)) # True
print(isinstance(100, Iterable)) # False
"""
"""

from collections.abc import Iterator
print(isinstance((), Iterator))  # False
print(isinstance(set(), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance("100", Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True
print(isinstance(iter([]), Iterator))  # False
"""

"""
# 自己创建通过容器迭代器对象

list1 = [1,2,3]
it = iter(list1)
# print(type(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for item in it:
    print(item)
"""
# 自定义迭代器  实现容器中元素的反转功能
class Reverse:
    # data表示要迭代的数据
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    # 如果是迭代器 必须实现iter方法
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]

rev = Reverse([1,3,5,7,9])
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))

