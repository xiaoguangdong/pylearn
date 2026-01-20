"""
    该案例演示了自定义进程类
"""
import multiprocessing
import os


class Worker(multiprocessing.Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print(self)
        print(f"当前进程id{os.getpid()},名称是{self.name},父进程的id{os.getppid()}执行了")

if __name__ == '__main__':
    # 创建进程对象
    for i in range(5):
        p = Worker("my_p_"+str(i))
        p.start()
