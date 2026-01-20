"""
    该案例演示了多进程方式读写文件
"""
import multiprocessing
import time


# 向文件中写入数据
def write_file():
    with open('test.txt', 'a') as f:
        while True:
            f.write('hello world\n')
            # 手动刷写缓冲区
            f.flush()
            time.sleep(0.5)

# 从文件中读取数据
def read_file():
    with open('test.txt', 'r') as f:
        while True:
            time.sleep(0.5)
            line = f.readline()
            print(line)

if __name__ == '__main__':
    # 创建一个子进程 去向文件中写入数据
    p1 = multiprocessing.Process(target=write_file)
    # 创建一个子进程 从文件中读取数据
    p2 = multiprocessing.Process(target=read_file)

    # 启动进程
    p1.start()
    p2.start()


