"""
    该案例演示了运算符
"""
# ~~~~~~~~~~~算术运算符~~~~~~~~~~~~~~~~
# num1 = 10
# num2 = 4
# # +	加
# print(num1 + num2)
# # -	减、或取负
# print(num1 - num2)
# # *	乘
# print(num1 * num2)
# # /	除
# print(num1 / num2)
# # //	整除，除后向下取整
# print(num1 // num2)
# # %	模，返回除法的余数
# print(num1 % num2)
# # **	幂
# print(num2 ** 3)

# ~~~~~~~~~~~赋值运算符~~~~~~~~~~~~~~~~
# =	赋值
num1 = 10
# +=	加法赋值
# num1 += 5  # ==>num1 = num1 + 5
# -=	减法赋值
# num1 -= 5
# *=	乘法赋值
# num1 *= 5
# /=	除法赋值
# num1 /= 5
# //=	整除赋值
# num1 //= 4
# %=	模赋值
# num1 %= 4
# **=	幂赋值
# num1 **= 4
# print(num1)
# :=	海象运算符，在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增
# num2 = num1 * 2
# print((num2 := num1 * 2) > num1)
# ~~~~~~~~~~~比较运算符~~~~~~~~~~~~~~~~
# num1 = 10
# num2 = 20
# # ==	相等，比较两者的值
# print(num1 == num2)
# # !=	不相等
# print(num1 != num2)
# # >	大于
# print(num1 > num2)
# # <	小于
# print(num1 < num2)
# # >=	大于等于
# print(num1 >= num2)
# # <=	小于等于
# print(num1 <= num2)
# ~~~~~~~~~~~逻辑运算符~~~~~~~~~~~~~~~~
# and	与，描述的是并且的关系，参与运算的两个数同时true，表达式返回true            x and y，若x为False返回x的值，否则返回y的值
# or	或，描述的是或者的关系，参与运算的两个数只要有一个为true，表达式返回true     x or y，若x为True返回x的值，否则返回y的值
# not	非，not x，若x为True返回False，若x为False返回True
# b1 = False
# b2 = True

# print(b1 and b2)  # False
# print(b1 or b2)   # True
# print(not b1)    # True

# print( 5 and 8)
# print( 0 and 8)

# print( 5 or 8) #
# print( 0 or 8)

# ~~~~~~~~~~~位运算符~~~~~~~~~~~~~~~~
# num1 = 17
# num2 = 13
#
# print(f"正数与运算: {num1} & {num2}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num2:3} : {num2:08b}")
# print(f"{num1 & num2:3} : {num1 & num2:08b}")
# print()
#
# print(f"正数或运算: {num1} | {num2}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num2:3} : {num2:08b}")
# print(f"{num1 | num2:3} : {num1 | num2:08b}")
# print()
#
# print(f"正数异或运算: {num1} ^ {num2}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num2:3} : {num2:08b}")
# print(f"{num1 ^ num2:3} : {num1 ^ num2:08b}")
# print()
#
# print(f"非运算: ~{num1}")
# print(f"{num1:3}原码 : {num1:08b}")
# print(f"{num1:3}取反 : {(1 << 8) - 1 ^ num1:08b}，得到结果的补码")
# print(f"{~num1:3}原码 : {~num1:08b}，计算出结果的原码")
#
#


# num1 = 17
# num2 = 13
# num3 = -12
#
# num1 = 4
# print(num1 << 1)
#
# print(f"有负数的与运算: {num3} & {num1}")
# print(f"{num3:3}原码 : {num3:03b}")
# print(f"{num3:3}反码 : {((1 << 8) - 1) + num3:08b}")
# print(f"{num3:3}补码 : {(1 << 8) + num3:08b}")
# print(f"{num1:3}补码 : {num1:08b}")
# print(f"{num1 & num3:3}补码 : {num1 & num3:08b}，得到结果")
# print()
#
# print(f"有负数的或运算: {num3} | {num1}")
# print(f"{num3:3}原码 : {num3:08b}")
# print(f"{num3:3}反码 : {(1 << 8) - 1 + num3:08b}")
# print(f"{num3:3}补码 : {(1 << 8) + num3:08b}")
# print(f"{num1:3}补码 : {num1:08b}")
# print(f"{num1 | num3:3}补码 : {(1 << 8) + (num1 | num3):08b}，得到结果的补码")
# print(f"{num1 | num3}原码 : {num1 | num3:08b}，计算出结果的原码")



# num1 = 17
# num2 = -12

# offset = 1
# print(f"左移运算: {num1} << {offset}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num1 << offset:3} : {num1 << offset:08b}")
# print()

# offset = 3
# print(f"右移运算: {num1} >> {offset}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num1 >> offset:3} : {num1 >> offset:08b}")
# print()
#
# offset = 3
# print(f"右移运算: {num2} >> {offset}")
# print(f"{num2:3}原码\t\t: {num2:08b}")
# print(f"{num2:3}反码\t\t: {(1 << 8) - 1 + num2:08b}")
# print(f"{num2:3}补码\t\t: {(1 << 8) + num2:08b}")
# print(f"{num2:3}补码>>{offset}\t: {(((1 << 8) + num2) >> offset) | (0xff >> 5 << 5):08b}，得到结果的补码")
# print(f"{num2 >> offset:3}\t\t\t: {num2 >> offset:08b}，计算出原码")


# ~~~~~~~~~~~成员运算符~~~~~~~~~~~~~~~~
num1 = 10
num2 = 60
numbers = [10,20,30,40,50]
print(num1 in numbers)
print(num2 in numbers)

# -------------身份运算符---------------
# m = 20
# n = 20
# q = 30
# print(m is n)  # True 判断m和n在内存中是否指向同一个地址
# print(n is q)  # False
# print(n is not q)  # True
#
# # id() 用于获取对象在内存中的地址
# print(id(m) == id(n)) # True
#
# print("*" * 20)
# # -------------is和==的区别---------------
a = [1,2,3]
b = a

print(b is a)  # True
print(b == a)  # True
#
# b = a[:]
# a = [1, 2, 3, 4, 5]
#
# a[:]      # [1, 2, 3, 4, 5]  完整复制
# a[1:3]    # [2, 3]          从索引1到3（不包含3）
# a[:3]     # [1, 2, 3]       从头到索引3
# a[2:]     # [3, 4, 5]       从索引2到结尾
# a[::2]    # [1, 3, 5]       步长为2，取奇数位
# a[::-1]   # [5, 4, 3, 2, 1]  反转列表

print(b)
print(b is a)  # False
print(b == a)  # True


# num2 = -12
# offset = 1
# offset = 2

# print(f"左移运算: {num2} << {offset}")
# print(f"{num2:3}原码\t\t: {num2:08b}")
# print(f"{num2:3}反码\t\t: {(1 << 8) - 1 + num2:08b}")
# print(f"{num2:3}补码\t\t: {(1 << 8) + num2:08b}")
# print(f"{num2:3}补码<<{offset}\t: {(((1 << 8) + num2) << 2) & 0xff:08b}，得到结果的补码")
# print(f"{num2 << offset:3}\t\t\t: {num2 << offset:08b}，计算出原码")
# print()


# import sys;print(sys.path) #没有问题

"""
import sys
for i in sys.path:
    print(i) #没有问题
"""
# import sys;for i in sys.path:;print(i) # 报错
