"""
    该案例演示了continue和break和pass关键字
"""
# 案例：打印0-9，跳过偶数。
# continue关键词
# for i in range(10):
#     # 判断当前遍历出来的元素是否能够被2整除
#     if i % 2 == 0:
#         # 跳出当前正在进行的本次循环，继续下一次循环
#         continue
#     print(i)

# break关键词
# for i in range(10):
#     # 判断当前遍历出来的元素是否能够被2整除
#     if i % 2 == 0:
#         # 跳出当前正在进行的本次循环，继续下一次循环
#         break
#     print(i)
#
# print("end")

# 案例：求0-9每个数自己幂自己的加和，如果大于10000000则循环终止。
# sum = 0
# for i  in range(10):
#     sum = sum + i ** i
#     if sum > 10000000:
#         break
#     print(i, sum)

# pass关键字  --- 占位
# while True:
#     pass

# 循环 + else
# target = 3
# for i in [1,2,3,4,5]:
#     if i == target:
#         print(f"当前要查找的值{target}在列表中")
#         break
# else:
#     print("在当前列表中没有找到目标元素")

for n in range(2,10):
    # 遍历寻找因子
    for x in range(2,n):
        if n % x == 0:
            print('%d等于%d*%d' %(n,x,n//x))
            break  # 跳出循环
    else :
        print('%d是一个质数' %n)
