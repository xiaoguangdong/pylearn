"""
    该案例演示了线程安全的问题
"""
import threading
import time


# 实现了买票功能的函数
def func1():
    global ticket_num
    while True:
        # 获取锁
        lock.acquire()
        if ticket_num <= 0:
            # 释放锁
            lock.release()
            break
        time.sleep(5)
        ticket_num -= 1
        lock.release()
        print(f"{threading.current_thread().name}卖了1张表,还剩{ticket_num}张")

if __name__ == '__main__':
    ticket_num = 100
    # 创建互斥锁对象
    lock = threading.Lock()
    threads = [threading.Thread(target=func1,name="窗口" + str(i)) for i in range(1,4) ]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print("done")

