"""
    该案例演示了列表相关操作
"""
# 创建新的列表
list1 = [100,200,300,400,500]
# print(list1)
# print(type(list1))
# 通过索引获取列表中元素
# print(list1[2])
# print(list1[-3])
#列表切片
# 复制整个列表
# list2 = list1[0:len(list1)]
# print(id(list1), id(list2))
# print(list1[0:len(list1)])
# print(list1[:])
# 取索引从2开始到4(不包含)的元素
# print(list1[2:4])
# 取索引从2开始到末尾的元素
# print(list1[2:])
# 取索引从0开始到2(不包含)的元素
# print(list1[0:2])
# print(list1[:2])
# 取索引从2开始到-1(不包含)的元素
# print(list1[2:4])
#print(list1[2:-1])
# 倒序取元素
# print(list1[::-1])

# list切片
#步长是正数：按照从左->右的方向切片的， 起始索引必须在结束索引左边
# print(list1[0:-1:2])
#步长是负数：按照从右->左的方向切片的， 起始索引必须在结束索引右边
# print(list1[0:3:-1])


# range
#步长是正数：生成的数列是递增的， start < stop
#步长是负数：生成的数列是递减的， start > stop
# print(type(range(0,10,1)))


#向列表中添加元素
# print(list1.insert(3, 800))
# 在指定的索引位置添加元素
# list1.insert(3, 800)
# 在列表的末尾追加元素
# list1.append(800)

# 列表相加
# list2 = [1,2,3]
# list3 = ["a","b","c"]
# print(list2 + list3)

# 列表相乘
# list3 = ["a","b","c"]
# print(list3*3)

# 修改列表元素-通过下标修改
# list1[2] = "a"
# 修改列表元素-通过切片修改
# list1[1:3] = ["a","b","c"]

# 判断成员是否为列表元素
# print(300 in list1)
# print(800 in list1)

#获取列表长度
# print(len(list1))
# 求列表中元素的最大值、最小值、加和
# list1.append("a")
# print(max(list1))
# print(min(list1))
# print(sum(list1))

# 列表元素的遍历
# 直接对列表进行遍历
# for item in list1:
#     print(item)

# 通过下标获取列表中的元素
# list[下标]
# 循环次数： len(list)
# for循环，先生成一个序列，起始值要和下标对应，从0开始
# for i in range(0,len(list1)):
#     print(i,list1[i])

# 通过enumerate直接遍历出下标和值
# for i,item in enumerate(list1):
#     print(i,item)


# 从列表中删除元素
# 通过del语句删除列表元素
# del list1[2]

# list1.insert(3,300)
#删除第一次出现的x
# print(list1.remove(300))
# print(list1.pop(3))

# list2 =[100,200,300,[500,600,700]]

# for i in list2[3]:
#     print(i)

# print(len(list2))

# 列表推导式  在已经存在可迭代对象的基础上，通过运算或者过滤，得到新的列表
# 基础列表推导式
# list2 = [i*2 for i in range(5)]
# 带条件的列表推导式
# list2 = [i*2 for i in range(10) if i % 2 == 0]

# list2 = [i *2  for i in list1]

# 包含多个循环的列表推导式
# list2 = [1,2,3]
# list3 = ["a","b","c"]
# list4 = [(i,j) for i in list2 for j in list3]
# print(list4)


# zip 拉链函数
list2 = [1,2,3,4]
list3 = ["a","b","c"]
zipped = zip(list2, list3)
list4 = list(zipped)
print(list4)
# print(type(list4))

print(list(zipped))
for item in list4:
    print(item)
for item in list4:
    print(item)