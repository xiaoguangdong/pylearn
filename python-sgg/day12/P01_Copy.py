"""
    该案例演示了浅拷贝和深拷贝
"""
import copy

"""
# 浅拷贝  [:]   list()   copy()
list1 = [1,2,3,[100,200,300]]
list2 = list1.copy()

# 对list中的不可变类型数据进行修改
# list1[0] = 10
# 对list中的可变类型数据进行修改
# list1[3].append(400)

print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3]),list1)
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3]),list2)
"""
"""
# 深拷贝
import copy
list1 = [1,2,3,[100,200,300]]
list2 = copy.deepcopy(list1)

# list1[0] = 10
list1[3].append(400)

print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3]),list1)
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3]),list2)
"""
"""
# 拷贝的特殊情况
# （1）非容器类型（如数字、字符串、和其他“原子”类型的对象）无法拷贝
var1 = 1
var2 = copy.copy(var1)
var3 = copy.deepcopy(var1)
var1 = 10

print(id(var1), var1)
print(id(var2), var2)
print(id(var3), var3)
"""
"""
# （2）元组变量如果只包含原子类型对象（不可变），则不能对其深拷贝
tup1 = (1,2,3)
tup2 = copy.deepcopy(tup1)

print(id(tup1), tuple(tup1))
print(id(tup2), tuple(tup2))
"""
tup1 = (1,2,3,[10,20])
tup2 = copy.deepcopy(tup1)

print(id(tup1), tuple(tup1))
print(id(tup2), tuple(tup2))


