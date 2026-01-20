"""
该案例演示了set集合常用的函数
"""

"""
set1 = {100,200,300,400,500}
# set.add(x)	添加元素
set1.add(600)
print(set1)
"""
"""
set1 = {100,200,300,400,500}
# set.update(x)	添加元素，x可以为列表、元组、字符串、字典等可迭代对象
set1.update([600,700])
print(set1)
"""
"""
# set.union(x)	添加元素后返回一个新的集合，x可以为列表、元组、字符串、字典等可迭代对象
set1 = {100,200,300}
set2 = {300,400,500}
set3 = set1.union(set2)
print(set3)
"""
"""
# set.remove(x)	从集合中移除x，x不存在则报错
set1 = {100,200,300}
set1.remove(600)
print(set1)
"""
"""
# set.discard(x) 	从集合中移除x，x不存在也不报错
set1 = {100,200,300}
set1.discard(200)
print(set1)
"""
"""
# set.pop()	随机取出集合中的一个元素，如果集合为空则报错
set1 = {100,200,300}
print(set1.pop())
print(set1)
"""
"""
# set.clear()	清空集合
set1 = {100,200,300}
set1.clear()
print(set1)
"""
"""
# set.difference(x1,...)	求set1和x1的差集，返回一个新的集合
set1 = {100,200,300}
set2 = {300,400,500}
print(set1.difference(set2))
print(set2.difference(set1))
"""
"""
# set.difference_update(x1,...)	求set1和x1的差集
set1 = {100,200,300}
set2 = {300,400,500}
set1.difference_update(set2)
set2.difference_update(set1)
print(set1)
print(set2)
"""
"""
# set.intersection(x1,...)	求set1和x1的交集，返回一个新的集合
set1 = {100,200,300}
set2 = {300,400,500}
print(set1.intersection(set2))
print(set2.intersection(set1))
"""
"""
# set.intersection_update(x1,...)	求set1和x1的交集
set1 = {100,200,300}
set2 = {300,400,500}
set1.intersection_update(set2)
print(set1)
"""
"""
# set1 & set2	两集合求交集
set1 = {100,200,300}
set2 = {300,400,500}
print(set1 & set2)
"""
"""
# set1 | set2	两集合求并集
set1 = {100,200,300}
set2 = {300,400,500}
print(set1 | set2)
"""
"""
# set1 - set2	两集合求差集
set1 = {100,200,300}
set2 = {300,400,500}
print(set1 - set2)
print(set2 - set1)
"""
"""
# set1.isdisjoint(set2)	判断两集合是否没有交集
set1 = {100,200,300}
set2 = {300,400,500}
print(set1.isdisjoint(set2))
"""
"""
# set1.issubset(set2)	判断set1是否为set2的子集
set1 = {300,400}
set2 = {300,400,500}
print(set1.issubset(set2))
# set1.issuperset(set2)	判断set2是否为set1的子集
set1 = {300,400}
set2 = {300,400,500}
print(set2.issuperset(set1))
"""
"""
# set1.symmetric_difference(set2)	求两集合中不重复的元素，返回一个新的集合
set1 = {300,400,600}
set2 = {300,400,500}
print(set1.symmetric_difference(set2))

# set1.symmetric_difference_update(set2)	求两集合中不重复的元素
set1 = {300,400,600}
set2 = {300,400,500}
set1.symmetric_difference_update(set2)
print(set1)
"""
"""
# set.copy()	拷贝集合
set1 = {300,400,600}
set2 = set1.copy()
print(set1,id(set1))
print(set2,id(set2))
"""
set1 = {300,400,600}
print(len(set1),max(set1),min(set1),sum(set1))
# len(set)	返回集合元素个数
# max(set)	求集合中元素的最大值
# min(set)	求集合中元素的最小值
# sum(set)	求集合中元素的加和
