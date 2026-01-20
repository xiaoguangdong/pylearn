"""
    该案例演示了进程之间通过Queue共享数据
"""
import multiprocessing
import os
import random
import time


# 向队列中放数据
def func1(qu):
    while True:
        num = random.randint(1, 50)
        qu.put(num)
        print(f"进程id{os.getpid()}向队列中放入了数据{num}")
        time.sleep(0.3)

# 从队列中取数据
def func2(qu):
    while True:
        num = qu.get()
        print(f"进程id{os.getpid()}从队列取出了数据{num}")

if __name__ == '__main__':
    # qu = multiprocessing.Queue(50)
    # p1 = multiprocessing.Process(target=func1, args=(qu,))
    # p2 = multiprocessing.Process(target=func2, args=(qu,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    qu = multiprocessing.Manager().Queue(50)
    # p1 = multiprocessing.Process(target=func1, args=(qu,))
    # p2 = multiprocessing.Process(target=func2, args=(qu,))
    pool = multiprocessing.Pool(2)
    pool.apply_async(func1, args=(qu,))
    pool.apply_async(func2, args=(qu,))
    pool.close()
    pool.join()
    print("done")


