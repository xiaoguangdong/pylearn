"""
    该案例演示了线程对象的创建
"""
import threading
import time


# 交替打印 00000 和 11111
def func():
    flag = 0
    while True:
        print(threading.current_thread().name, f"{flag}" * 5)
        flag = flag ^ 1  # 替换0和1
        time.sleep(0.5)

if __name__ == '__main__':
    # 创建线程对象
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("done")

