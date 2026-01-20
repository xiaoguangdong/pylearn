
"""
    该案例演示了整数数字不同进制的表示形式
        二进制：    以0b开头
        八进制：    以0o开头
        十进制：    正常数字表示
        十六进制：   以0x开头
"""
# 十进制
dec_num = 10
# 二进制
bin_num = 0b1010
# 八进制
oct_num = 0o12
# 十六进制
hex_num = 0xa

print(dec_num)
print(bin_num)
print(oct_num)
print(hex_num)

# 介绍几个函数 ，函数：完成某一个功能的代码块
print("~~~~~~~~")
print("十进制数字：" + str(dec_num))
# bin()函数作用：将十进制数转换为二进制
print("转换为二进制进制数字：" + bin(dec_num))
# oct()函数作用：将十进制数转换为八进制
print("转换为八进制进制数字：" + oct(dec_num))
# hex()函数作用：将十进制数转换为十六进制
print("转换为十六进制进制数字：" + hex(dec_num))

