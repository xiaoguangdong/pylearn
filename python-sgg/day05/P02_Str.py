
"""
    该案例演示了字符串的操作
"""
"""
# 创建字符串
str1 = 'abcdefg'
str2 = "abcdefg"
# 三引号可以保留字符串的样式
# str3 = '''abcdefg'''
"""

"""
# 获取字符以及字符串切片
print(str1[3])
print(str1[-4])
print(str1[1:5])
print(str1[2:])
print(str1[:5])
print(str1[:])
print(str1[::-1])
"""

# 字符串相加
str1 = "hello"
str2 = "world"
print(str1,id(str1))
# 不可变
# str1[1] = "a"
str1 = str1 + str2
print(str1,id(str1))

"""
# 字符串乘法
print("~"*100)
"""
"""
# 判断字符是否在字符串中
str1 = "hello"
print("h" in str1)
print("w" in str1)
"""

# 原始字符串
str1 ="hello\t\t\tworld"
str1 =r"hello\t\t\tworld"
str1 =R"hello\t\t\tworld"
print(str1)

