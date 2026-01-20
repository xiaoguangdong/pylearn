"""
    每日一考讲解
"""
# 现有列表 my_list = [10, 20, 30, 40, 50]，请编写代码实现：
# 向列表末尾添加一个元素 60。
#  取出列表中索引为 2 的元素。
# 计算列表中所有元素的和。
# my_list = [10, 20, 30, 40, 50]
# my_list.append(60)
# print(my_list[2])
# del my_list[0]
# my_list.remove()
# my_list.pop()

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [(i,j) for i in list1 if i >= 2 for j in list2 if j >= 5]
# for i in list1:
#     if i >= 2:
#         for j in list2:
#             if j >= 5:
#                 (i,j)

# list3 = [(i,j) for i in list1  for j in list2 if i >= 2 and j >= 5]
# for i in list1:
#     for j in list2:
#         if i >= 2 and j >= 5:
#             (i, j)

# 使用for循环的嵌套，打印如下图形的*
#     *
#    ***
#   *****
#  *******
# *********
# a = [1,3,5,7,9]
# b = 4
# for i in range(0,1):
#     for j in a:
#         print(" "*b+"*"*j)
#         b-=1
# print(list3)

# for i in range(0,5):
#     xi = 'x'*(2*i+1)
#     print(f'{xi:^9}')

# height = 5
# for i in range(height*2):
#     output = "*" * i
#     if i % 2 == 0:
#         continue
#     print(f"{output:^{height*2}}")

# n = 5
# for i in range(1,n + 1):
#     for j in range(n - i ):
#           print(" ", end="")
#     for k in range(2 * i - 1):
#           print("★", end="")
#     print()

"""
for i in range(5):
    for j in range(0,5-i):
        print(" ",end="")
    print("*"*(2*i+1))
"""

