"""
    该案例演示了线程安全问题
"""
import threading
import time


def func():
    global g_num
    for _ in range(10):
        tmp = g_num  + 1
        # time.sleep(0.3)
        g_num = tmp
        print(f"当前线程{threading.current_thread().name}:{g_num}")

if __name__ == '__main__':
    # 定义一个全局变量
    g_num = 0

    # 创建3个线程对象
    threads = [threading.Thread(target=func,name="线程" + str(i)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print(f"当前线程{threading.current_thread().name}",g_num)