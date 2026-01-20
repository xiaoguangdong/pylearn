"""
    该案例演示了查看目录下的子目录以及文件
"""
import os

# print(os.getcwd())

for root, dirs, files in os.walk(os.getcwd()):
    print("当前路径：", root)
    print("目录：", dirs)
    print("文件：", files)
    print()
