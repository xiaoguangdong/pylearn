"""
    该案例演示了读写文件操作
"""

"""
# 向文件中写入数据
# 打开文件（建立程序和文件之间的通道）
f = open("test.txt","w")

# 向文件中写入数据
f.write("hello world\n")
f.write("nihao python\n")

# 关闭和文件之间的建立的通道
f.close()
"""
# 从文件中读取数据
# 打开文件（建立程序和文件之间的通道）
f = open("test.txt","r")
# 从文件中读取数据   read() 默认读取所有数据
# print(f.read())
# 从文件中读取指定的字节大小数据
# print(f.read(5))
# print(f.read(8))

# 读取一行数据
# print(f.readline())
# print(f.readline())

# 读取所有行
print(f.readlines())

# 关闭和文件之间的建立的通道
f.close()