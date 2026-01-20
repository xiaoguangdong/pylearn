"""
    该案例演示了进程之间不共享变量
"""
import multiprocessing
import os


# 向list中添加10个元素
def func(list1):
    for i in range(10):
        list1.append(i)
        print(f"当前进程id:{os.getpid()}",list1)

if __name__ == "__main__":
    list1 = []
    p1 = multiprocessing.Process(target=func, args=(list1,))
    p2 = multiprocessing.Process(target=func, args=(list1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("done",os.getpid(),list1)