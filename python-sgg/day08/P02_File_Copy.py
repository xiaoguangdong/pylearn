"""
    该案例了文件的拷贝
"""
"""
def file_copy(source_file_path,dest_file_path):
    # 打开源文件
    source_file = open(source_file_path,"rb")
    # 从源文件中读取数据
    content = source_file.read()

    # 打开目标文件
    dest_file = open(dest_file_path,"wb")
    # 将内容写到目标文件
    dest_file.write(content)

    #关闭源文件
    source_file.close()

    #关闭目标文件
    dest_file.close()
"""

# 优化：一次不要读取全部文件内容，读取指定的字节大小
def file_copy(source_file_path,dest_file_path):
    # 打开源文件
    source_file = open(source_file_path,"rb")
    # 打开目标文件
    dest_file = open(dest_file_path,"wb")

    # 从源文件中读取数据
    content = source_file.read(1024)

    # 将内容写到目标文件
    while content:
        dest_file.write(content)
        content = source_file.read(1024)

    #关闭源文件
    source_file.close()

    #关闭目标文件
    dest_file.close()

file_copy("d:\\hua.png","E:\\大模型课程\\01_尚硅谷大模型技术之Python基础\\4.视频\\day08\\hua.png")
