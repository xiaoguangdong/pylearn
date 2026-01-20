"""
    该案例再次对匿名函数进行说明
"""
# list1  要处理的集合
# func   对集合中元素的处理逻辑

def my_map(list1, func):
    for i, item in enumerate(list1) :
        func(item)
        list1[i] = func(item)
    return list1

list1 = list(range(1,5))
print(my_map(list1, lambda item: item * 2))