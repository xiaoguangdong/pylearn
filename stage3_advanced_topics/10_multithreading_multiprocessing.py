# -*- coding: utf-8 -*-
"""
第三阶段：多线程与多进程基础
演示并发与并行概念、threading和multiprocessing模块
"""

import threading
import multiprocessing
import time
import queue


def demo_concurrency_vs_parallelism():
    """演示并发与并行概念"""
    print("=" * 50)
    print("并发与并行概念演示")
    print("=" * 50)
    
    print("并发 (Concurrency):")
    print("  多个任务交替执行，看起来同时进行")
    print("  适用于IO密集型任务")
    print("  例如：同时处理多个网络请求")
    
    print("\n并行 (Parallelism):")
    print("  多个任务真正同时执行")
    print("  需要多核CPU")
    print("  适用于CPU密集型任务")
    print("  例如：同时计算多个数学问题")
    
    print()


def demo_threading_basic():
    """演示threading模块基础"""
    print("=" * 50)
    print("threading模块基础演示")
    print("=" * 50)
    
    # 简单的线程
    def worker(name, delay):
        """工作函数"""
        print(f"  线程 {name} 开始工作")
        time.sleep(delay)
        print(f"  线程 {name} 完成工作")
    
    print("创建线程:")
    thread1 = threading.Thread(target=worker, args=("线程1", 1))
    thread2 = threading.Thread(target=worker, args=("线程2", 1))
    
    start_time = time.time()
    thread1.start()
    thread2.start()
    
    thread1.join()  # 等待线程完成
    thread2.join()
    
    end_time = time.time()
    print(f"总耗时: {end_time - start_time:.2f}秒（并发执行）\n")
    
    # 线程同步 - Lock
    print("线程同步（Lock）:")
    counter = 0
    lock = threading.Lock()
    
    def increment():
        nonlocal counter
        for _ in range(100000):
            with lock:  # 使用锁保护共享资源
                counter += 1
    
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=increment)
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    print(f"  计数器值: {counter} (应该是200000)")
    
    print()
    
    # 线程间通信 - Queue
    print("线程间通信（Queue）:")
    q = queue.Queue()
    
    def producer():
        """生产者线程"""
        for i in range(5):
            q.put(f"产品{i}")
            print(f"  生产: 产品{i}")
            time.sleep(0.1)
    
    def consumer():
        """消费者线程"""
        while True:
            item = q.get()
            if item is None:  # 结束信号
                break
            print(f"  消费: {item}")
            q.task_done()
    
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    consumer_thread.start()
    producer_thread.start()
    producer_thread.join()
    
    q.put(None)  # 发送结束信号
    consumer_thread.join()
    
    print()


def demo_multiprocessing_basic():
    """演示multiprocessing模块基础"""
    print("=" * 50)
    print("multiprocessing模块基础演示")
    print("=" * 50)
    
    # 简单的进程
    def cpu_bound_task(n):
        """CPU密集型任务"""
        result = 0
        for i in range(n):
            result += i ** 2
        return result
    
    print("单进程执行:")
    start_time = time.time()
    result1 = cpu_bound_task(10000000)
    result2 = cpu_bound_task(10000000)
    single_time = time.time() - start_time
    print(f"  结果: {result1}, {result2}")
    print(f"  耗时: {single_time:.2f}秒")
    
    print("\n多进程执行:")
    start_time = time.time()
    p1 = multiprocessing.Process(target=cpu_bound_task, args=(10000000,))
    p2 = multiprocessing.Process(target=cpu_bound_task, args=(10000000,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    multi_time = time.time() - start_time
    print(f"  耗时: {multi_time:.2f}秒")
    print(f"  加速比: {single_time/multi_time:.2f}x")
    
    print()
    
    # 进程池
    print("进程池:")
    def square(x):
        return x ** 2
    
    with multiprocessing.Pool(processes=4) as pool:
        numbers = range(10)
        results = pool.map(square, numbers)
        print(f"  输入: {list(numbers)}")
        print(f"  输出: {results}")
    
    print()
    
    # 进程间通信 - Queue
    print("进程间通信（Queue）:")
    def producer_process(q):
        """生产者进程"""
        for i in range(5):
            q.put(f"数据{i}")
            print(f"  进程生产: 数据{i}")
            time.sleep(0.1)
    
    def consumer_process(q):
        """消费者进程"""
        while True:
            item = q.get()
            if item is None:
                break
            print(f"  进程消费: {item}")
    
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer_process, args=(q,))
    p2 = multiprocessing.Process(target=consumer_process, args=(q,))
    
    p2.start()
    p1.start()
    p1.join()
    q.put(None)
    p2.join()
    
    print()


def demo_practical_examples():
    """演示实际应用示例"""
    print("=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    # 1. 多线程下载（模拟）
    print("多线程下载（模拟）:")
    def download_file(url, delay):
        """模拟下载文件"""
        print(f"  开始下载: {url}")
        time.sleep(delay)
        print(f"  完成下载: {url}")
        return f"{url}的内容"
    
    urls = ["file1.txt", "file2.txt", "file3.txt"]
    threads = []
    
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url, 0.5))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"  总耗时: {end_time - start_time:.2f}秒\n")
    
    # 2. 多进程计算（CPU密集型）
    print("多进程计算（CPU密集型）:")
    def calculate_factorial(n):
        """计算阶乘"""
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    numbers = [1000, 1001, 1002, 1003]
    
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, numbers)
    multi_time = time.time() - start_time
    
    start_time = time.time()
    single_results = [calculate_factorial(n) for n in numbers]
    single_time = time.time() - start_time
    
    print(f"  单进程耗时: {single_time:.2f}秒")
    print(f"  多进程耗时: {multi_time:.2f}秒")
    print(f"  加速比: {single_time/multi_time:.2f}x")
    print(f"  结果验证: 多进程结果长度={len(results)}, 单进程结果长度={len(single_results)}")
    
    print()


def demo_threading_vs_multiprocessing():
    """演示threading vs multiprocessing的选择"""
    print("=" * 50)
    print("threading vs multiprocessing 选择指南")
    print("=" * 50)
    
    print("使用 threading 的场景:")
    print("  - IO密集型任务（网络请求、文件读写）")
    print("  - 需要共享内存和状态")
    print("  - 任务执行时间短")
    print("  - 需要轻量级并发")
    
    print("\n使用 multiprocessing 的场景:")
    print("  - CPU密集型任务（计算、图像处理）")
    print("  - 需要真正的并行执行")
    print("  - 任务可以独立执行")
    print("  - 需要利用多核CPU")
    
    print("\n注意事项:")
    print("  - Python的GIL（全局解释器锁）限制线程的并行执行")
    print("  - 对于CPU密集型任务，multiprocessing更有效")
    print("  - 对于IO密集型任务，threading通常足够")
    print("  - 进程间通信比线程间通信开销更大")
    
    print()


if __name__ == "__main__":
    # 注意：在Windows上使用multiprocessing需要这个保护
    multiprocessing.freeze_support()
    
    # 运行所有演示
    demo_concurrency_vs_parallelism()
    demo_threading_basic()
    demo_multiprocessing_basic()
    demo_practical_examples()
    demo_threading_vs_multiprocessing()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

