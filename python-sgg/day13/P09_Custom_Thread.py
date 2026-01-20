"""
    该案例演示了自定义Thread类，创建线程对象
"""
import threading
import time


class Worker(threading.Thread):
    def run(self):
        flag = 0
        while True:
            print(threading.current_thread().name, f"{flag}" * 5)
            flag = flag ^ 1  # 替换0和1
            time.sleep(0.5)

if __name__ == '__main__':
    t1 = Worker(name = "线程1")
    t2 = Worker(name = "线程2")
    t1.start()
    t2.start()

