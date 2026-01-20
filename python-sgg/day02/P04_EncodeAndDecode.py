
"""
    该案例演示了字符的编码以及解码
        编码：将字符转换为字节的形式
        解码：将字节转换为字符的形式
"""
str1 = "你好中国"
print(str1)
print(type(str1))
# 编码
byte1 = str1.encode(encoding='gbk')
print(byte1)
print(type(byte1))

# 解码
# str2 = byte1.decode(encoding='utf-8')
# print(str2)

# 注意：编码和解码需要指定相同的字符集
str3 = byte1.decode(encoding='gbk')
print(str3)
