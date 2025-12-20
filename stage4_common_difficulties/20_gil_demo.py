# -*- coding: utf-8 -*-
"""
第四阶段：GIL（全局解释器锁）难点实战演示
演示GIL对多线程性能的影响、CPU密集型vs I/O密集型任务、多进程解决方案等核心概念
"""

import threading
import multiprocessing
import time
import sys
import concurrent.futures
from typing import List, Callable, Any

# 尝试导入requests，如果不可用则使用模拟I/O
REQUESTS_AVAILABLE = False
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    pass


def demo_gil_basics():
    """演示GIL的基本概念"""
    print("=" * 60)
    print("GIL基本概念演示")
    print("=" * 60)
    
    print("1. GIL是什么？")
    print("   - GIL (Global Interpreter Lock) 是CPython解释器中的全局锁")
    print("   - 同一时间只允许一个线程执行Python字节码")
    print("   - 影响多线程程序的并行性能")
    
    print("\n2. Python线程的限制：")
    print("   - 即使在多核CPU上，多线程Python程序也无法利用多个核心")
    print("   - 这是因为GIL限制了同一时间只有一个线程执行Python代码")
    
    # 查看当前线程数量
    print(f"\n3. 当前线程信息：")
    print(f"   当前Python版本: {sys.version}")
    print(f"   当前活跃线程数: {threading.active_count()}")
    
    threads = threading.enumerate()
    for thread in threads:
        print(f"   线程: {thread.name}, 守护线程: {thread.daemon}")


def cpu_bound_task(n: int) -> int:
    """CPU密集型任务"""
    result = 0
    for _ in range(n):
        result += sum(i * i for i in range(1000))
    return result


def cpu_thread_task():
    """CPU密集型任务的线程包装函数"""
    return cpu_bound_task(1000)


def io_bound_task(url: str) -> int:
    """I/O密集型任务"""
    if REQUESTS_AVAILABLE:
        response = requests.get(url)
        return len(response.content)
    else:
        # 模拟I/O操作
        time.sleep(0.1)
        return 1000  # 返回模拟的内容长度


def demo_cpu_bound_vs_io_bound():
    """演示CPU密集型vs I/O密集型任务在GIL下的表现"""
    print("\n" + "=" * 60)
    print("CPU密集型vs I/O密集型任务演示")
    print("=" * 60)
    
    # CPU密集型任务测试
    print("1. CPU密集型任务：")
    
    # 单个线程
    start_time = time.time()
    cpu_bound_task(1000)
    cpu_bound_task(1000)
    cpu_bound_task(1000)
    single_thread_time = time.time() - start_time
    print(f"   单线程执行时间: {single_thread_time:.4f} 秒")
    
    # 多线程
    start_time = time.time()
    
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=cpu_thread_task)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    multi_thread_time = time.time() - start_time
    print(f"   多线程执行时间: {multi_thread_time:.4f} 秒")
    
    # 多进程
    start_time = time.time()
    
    processes = []
    for _ in range(3):
        process = multiprocessing.Process(target=cpu_thread_task)
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    multi_process_time = time.time() - start_time
    print(f"   多进程执行时间: {multi_process_time:.4f} 秒")
    
    # 比较结果
    print(f"\n   多线程vs单线程: {single_thread_time/multi_thread_time:.2f}倍")
    print(f"   多进程vs单线程: {single_thread_time/multi_process_time:.2f}倍")
    
    print("\n2. I/O密集型任务：")
    
    urls = [
        "https://www.python.org",
        "https://www.google.com", 
        "https://www.github.com",
        "https://www.bing.com",
        "https://www.yahoo.com"
    ]
    
    # 单个线程
    start_time = time.time()
    for url in urls:
        io_bound_task(url)
    single_thread_time = time.time() - start_time
    print(f"   单线程执行时间: {single_thread_time:.4f} 秒")
    
    # 多线程
    start_time = time.time()
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=io_bound_task, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    multi_thread_time = time.time() - start_time
    print(f"   多线程执行时间: {multi_thread_time:.4f} 秒")
    
    # 多进程
    start_time = time.time()
    
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=io_bound_task, args=(url,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    multi_process_time = time.time() - start_time
    print(f"   多进程执行时间: {multi_process_time:.4f} 秒")
    
    # 比较结果
    print(f"\n   多线程vs单线程: {single_thread_time/multi_thread_time:.2f}倍")
    print(f"   多进程vs单线程: {single_thread_time/multi_process_time:.2f}倍")
    
    print("\n3. 结论：")
    print("   - CPU密集型任务：多进程优于多线程")
    print("   - I/O密集型任务：多线程和多进程都有不错的加速效果")
    print("   - GIL主要影响CPU密集型任务的多线程性能")


def demo_gil_release_mechanism():
    """演示GIL的释放机制"""
    print("\n" + "=" * 60)
    print("GIL释放机制演示")
    print("=" * 60)
    
    print("1. GIL的释放条件：")
    print("   - Python线程执行一定数量的字节码后会释放GIL")
    print("   - 在I/O操作（如网络请求、文件读写）时会释放GIL")
    print("   - 调用C扩展时可能会释放GIL")
    
    print("\n2. 字节码计数演示：")
    print("   - CPython每执行100个字节码指令检查一次GIL")
    print("   - 这是通过sys.getswitchinterval()控制的")
    
    # 查看当前的切换间隔
    switch_interval = sys.getswitchinterval()
    print(f"   当前线程切换间隔: {switch_interval} 秒")
    
    # 演示GIL释放
    print("\n3. GIL释放测试：")
    
    def count_thread(name: str, count: int):
        """计数线程"""
        print(f"   线程 {name} 开始计数到 {count}")
        for i in range(count):
            # 空循环，主要执行Python字节码
            pass
        print(f"   线程 {name} 完成计数")
    
    # 创建两个线程，观察它们的执行顺序
    start_time = time.time()
    
    thread1 = threading.Thread(target=count_thread, args=("A", 10000000))
    thread2 = threading.Thread(target=count_thread, args=("B", 10000000))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    end_time = time.time()
    print(f"   总执行时间: {end_time - start_time:.4f} 秒")
    print("   - 注意观察线程A和B是否交替执行")
    print("   - 这表明GIL正在被定期释放和重新获取")


def demo_concurrent_futures():
    """演示concurrent.futures模块的使用"""
    print("\n" + "=" * 60)
    print("concurrent.futures模块演示")
    print("=" * 60)
    
    print("1. 线程池与进程池：")
    print("   - ThreadPoolExecutor：创建线程池")
    print("   - ProcessPoolExecutor：创建进程池")
    
    # CPU密集型任务使用进程池
    print("\n2. CPU密集型任务（进程池）：")
    start_time = time.time()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_bound_task, [1000, 1000, 1000]))
    
    end_time = time.time()
    print(f"   进程池执行时间: {end_time - start_time:.4f} 秒")
    print(f"   结果: {results}")
    
    # I/O密集型任务使用线程池
    print("\n3. I/O密集型任务（线程池）：")
    urls = [
        "https://www.python.org",
        "https://www.google.com", 
        "https://www.github.com",
        "https://www.bing.com",
        "https://www.yahoo.com"
    ]
    
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(io_bound_task, urls))
    
    end_time = time.time()
    print(f"   线程池执行时间: {end_time - start_time:.4f} 秒")
    print(f"   每个URL的内容长度: {results}")
    
    # 混合任务
    print("\n4. 混合任务处理：")
    print("   - 根据任务类型选择合适的执行器")
    print("   - CPU密集型使用ProcessPoolExecutor")
    print("   - I/O密集型使用ThreadPoolExecutor")


def producer(queue: multiprocessing.Queue, items: List[int]):
    """生产者函数"""
    for item in items:
        queue.put(item)
        print(f"   生产者放入: {item}")
        time.sleep(0.1)
    queue.put(None)  # 发送结束信号


def consumer(queue: multiprocessing.Queue):
    """消费者函数"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"   消费者取出: {item}")
        time.sleep(0.2)


def increment_counter(counter: multiprocessing.Value, times: int):
    """增加计数器值"""
    for _ in range(times):
        with counter.get_lock():
            counter.value += 1


def square(n: int) -> int:
    """计算平方"""
    return n * n


def demo_multiprocessing_techniques():
    """演示多进程编程技巧"""
    print("\n" + "=" * 60)
    print("多进程编程技巧演示")
    print("=" * 60)
    
    # 1. 进程间通信
    print("1. 进程间通信（Queue）：")
    
    # 创建队列和进程
    queue = multiprocessing.Queue()
    items = [1, 2, 3, 4, 5]
    
    p1 = multiprocessing.Process(target=producer, args=(queue, items))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    # 2. 共享内存
    print("\n2. 共享内存：")
    
    counter = multiprocessing.Value('i', 0)  # 'i'表示整数类型
    
    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=increment_counter, args=(counter, 1000))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"   最终计数器值: {counter.value}")
    
    # 3. 进程池
    print("\n3. 进程池高级用法：")
    
    with multiprocessing.Pool(processes=4) as pool:
        # 使用map
        results_map = pool.map(square, range(10))
        print(f"   map结果: {results_map}")
        
        # 使用imap
        print(f"   imap结果: ", end="")
        for result in pool.imap(square, range(10)):
            print(result, end=" ")
        print()
        
        # 使用apply_async
        results_async = [pool.apply_async(square, (i,)) for i in range(10)]
        results = [res.get() for res in results_async]
        print(f"   apply_async结果: {results}")


def demo_gil_workarounds():
    """演示GIL的解决方案"""
    print("\n" + "=" * 60)
    print("GIL解决方案演示")
    print("=" * 60)
    
    print("1. 使用多进程代替多线程：")
    print("   - 对于CPU密集型任务，多进程是首选解决方案")
    print("   - 每个进程都有自己的Python解释器和GIL")
    
    print("\n2. 使用C扩展：")
    print("   - 在C扩展中可以释放GIL，允许真正的并行执行")
    print("   - 许多科学计算库（如NumPy）使用这种方式")
    
    print("\n3. 使用Jython或IronPython：")
    print("   - 这些Python实现没有GIL")
    print("   - 但它们与CPython的兼容性可能有限")
    
    print("\n4. 使用异步编程：")
    print("   - 对于I/O密集型任务，异步编程是高效的解决方案")
    print("   - 它使用单线程但可以处理大量并发I/O操作")
    
    print("\n5. 使用PyPy：")
    print("   - PyPy的JIT编译器可以显著提高Python程序的性能")
    print("   - 虽然PyPy也有GIL，但由于执行速度快，很多情况下可以替代多进程")


def main():
    """主函数"""
    print("=" * 60)
    print("GIL（全局解释器锁）难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. GIL基本概念")
    print("2. CPU密集型vs I/O密集型任务")
    print("3. GIL释放机制")
    print("4. concurrent.futures模块")
    print("5. 多进程编程技巧")
    print("6. GIL的解决方案")
    print("=" * 60)
    
    # 运行各个演示
    demo_gil_basics()
    demo_cpu_bound_vs_io_bound()
    demo_gil_release_mechanism()
    demo_concurrent_futures()
    demo_multiprocessing_techniques()
    demo_gil_workarounds()
    
    print("\n" + "=" * 60)
    print("GIL难点总结:")
    print("1. GIL限制了Python多线程程序的并行性能")
    print("2. CPU密集型任务：多进程优于多线程")
    print("3. I/O密集型任务：多线程和多进程都有不错的加速效果")
    print("4. 选择合适的并发模型很重要")
    print("5. 可以使用concurrent.futures简化并发编程")
    print("6. 多进程间通信需要特殊的机制（如Queue、共享内存）")
    print("=" * 60)


if __name__ == "__main__":
    main()
