"""
    该案例演示set基本操作
"""
"""
# 创建set集合
set1 = {100,200,300}
set2 = set(range(10))
# 注意：如果想声明一个空set，不能用下面的方式，下面会创建一个空的dict
# set3 = {}
set3 = set()
print(set1,type(set1))
print(set2,type(set2))
print(set3,type(set3))
"""
"""
# 添加和删除元素
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
set1 = {i*2 for i in range(10)}
# 向set中添加元素
set1.add(5)
# 从集合中删除元素
# del set1 X
# print(set1.pop())
set1.remove(5)

print(set1,type(set1))
"""

# 检查成员是否为集合中元素
set1 = {1,2,3,4,5}
print(2 in set1)
print(6 in set1)

# 获取集合长度
print(len(set1))

# 获取集合中元素最大值、最小值、加和
print(max(set1))  # 5
print(min(set1))  # 1
print(sum(set1))  # 15

# 集合中元素不能重复
set1.add(1)
set1.add(1)
set1.add(1)

# 遍历
for item in set1:
    print(item)

