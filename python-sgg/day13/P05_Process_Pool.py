"""
    该案例演示了进程池
"""
import os
import time
import multiprocessing

# 提供一个函数，打印10个数字，每间隔0.5秒打印一次
def func():
    for i in range(10):
        print(f"当前进程id:{os.getpid()},打印了{i}")
        time.sleep(0.5)

if __name__ == '__main__':
    # 指定池的大小(创建进程的数量)
    process_num = 5
    pool = multiprocessing.Pool(process_num)
    for i in range(process_num):
        # 从池中拿进程对象，执行任务(将任务交给池中对象执行)
        # 同步
        # pool.apply(func)
        # 异步
        pool.apply_async(func)

    # 关闭进程池
    pool.close()
    # 阻塞主进程（当前进程执行完毕之后，主进程再继续执行）
    pool.join()
    print("done")
