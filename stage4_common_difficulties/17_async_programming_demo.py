# -*- coding: utf-8 -*-
"""
第四阶段：异步编程难点实战演示
演示async/await关键字、事件循环、协程通信等核心概念
"""

import asyncio
import time
from typing import List, Dict, Any

# 尝试导入aiohttp，如果不可用则标记
try:
    import aiohttp
    AIOHTTP_AVAILABLE = True
except ImportError:
    AIOHTTP_AVAILABLE = False


def demo_sync_vs_async():
    """演示同步与异步的区别"""
    print("=" * 60)
    print("同步与异步对比演示")
    print("=" * 60)
    
    # 同步版本
    def sync_task(name: str, delay: int) -> str:
        """同步任务"""
        print(f"   同步任务 {name} 开始，延迟 {delay} 秒")
        time.sleep(delay)
        print(f"   同步任务 {name} 完成")
        return f"{name} 结果"
    
    # 异步版本
    async def async_task(name: str, delay: int) -> str:
        """异步任务"""
        print(f"   异步任务 {name} 开始，延迟 {delay} 秒")
        await asyncio.sleep(delay)
        print(f"   异步任务 {name} 完成")
        return f"{name} 结果"
    
    # 同步执行
    print("1. 同步执行：")
    sync_start = time.time()
    result1 = sync_task("A", 2)
    result2 = sync_task("B", 3)
    sync_end = time.time()
    print(f"   同步执行总时间：{sync_end - sync_start:.2f}秒")
    
    # 异步执行
    print("\n2. 异步执行：")
    async def main_async():
        task1 = asyncio.create_task(async_task("A", 2))
        task2 = asyncio.create_task(async_task("B", 3))
        await asyncio.gather(task1, task2)
    
    async_start = time.time()
    asyncio.run(main_async())
    async_end = time.time()
    print(f"   异步执行总时间：{async_end - async_start:.2f}秒")


def demo_async_await_basics():
    """演示async/await基础"""
    print("\n" + "=" * 60)
    print("async/await基础演示")
    print("=" * 60)
    
    async def hello() -> str:
        """简单的异步函数"""
        await asyncio.sleep(1)
        return "Hello, async world!"
    
    print("1. 异步函数的创建与调用：")
    async def main():
        # 直接调用异步函数返回协程对象
        coro = hello()
        print(f"   直接调用异步函数返回：{coro}")
        
        # 使用await获取结果
        result = await coro
        print(f"   await获取结果：{result}")
    
    asyncio.run(main())
    
    # 多任务并发
    print("\n2. 多任务并发执行：")
    async def delayed_print(message: str, delay: int):
        await asyncio.sleep(delay)
        print(f"   {message}")
    
    async def main_multiple():
        tasks = [
            asyncio.create_task(delayed_print("Task 1", 1)),
            asyncio.create_task(delayed_print("Task 2", 0.5)),
            asyncio.create_task(delayed_print("Task 3", 1.5))
        ]
        await asyncio.gather(*tasks)
    
    asyncio.run(main_multiple())


def demo_event_loop():
    """演示事件循环"""
    print("\n" + "=" * 60)
    print("事件循环演示")
    print("=" * 60)
    
    async def demo_coroutine():
        print("   协程开始执行")
        await asyncio.sleep(0.5)
        print("   协程执行中间点")
        await asyncio.sleep(0.5)
        print("   协程执行完成")
        return "完成"
    
    print("1. 事件循环的基本使用：")
    
    # 方法1：使用asyncio.run()
    result = asyncio.run(demo_coroutine())
    print(f"   asyncio.run() 结果：{result}")
    
    print("\n2. 手动创建和管理事件循环：")
    
    # 创建事件循环
    loop = asyncio.new_event_loop()
    try:
        # 设置为当前事件循环（在某些环境中需要）
        asyncio.set_event_loop(loop)
        
        # 运行协程
        result = loop.run_until_complete(demo_coroutine())
        print(f"   手动事件循环结果：{result}")
        
        # 运行多个协程
        async def another_coroutine():
            await asyncio.sleep(0.3)
            return "另一个结果"
        
        results = loop.run_until_complete(
            asyncio.gather(demo_coroutine(), another_coroutine())
        )
        print(f"   运行多个协程结果：{results}")
        
    finally:
        # 关闭事件循环
        loop.close()


def demo_asyncio_advanced():
    """演示异步编程高级特性"""
    print("\n" + "=" * 60)
    print("异步编程高级特性演示")
    print("=" * 60)
    
    # 1. 任务超时处理
    print("1. 任务超时处理：")
    
    async def long_running_task():
        await asyncio.sleep(3)
        return "任务完成"
    
    async def main_timeout():
        try:
            # 设置1秒超时
            result = await asyncio.wait_for(long_running_task(), timeout=1.0)
            print(f"   任务结果：{result}")
        except asyncio.TimeoutError:
            print(f"   任务超时！")
    
    asyncio.run(main_timeout())
    
    # 2. 任务取消
    print("\n2. 任务取消：")
    
    async def cancellable_task():
        try:
            print("   可取消任务开始")
            await asyncio.sleep(5)
            print("   可取消任务完成")
            return "完成"
        except asyncio.CancelledError:
            print("   任务被取消！")
            raise
    
    async def main_cancel():
        task = asyncio.create_task(cancellable_task())
        
        # 等待1秒后取消任务
        await asyncio.sleep(1)
        task.cancel()
        
        try:
            await task
        except asyncio.CancelledError:
            print("   主函数捕获到任务取消")
    
    asyncio.run(main_cancel())
    
    # 3. 异步上下文管理器
    print("\n3. 异步上下文管理器：")
    
    class AsyncContextManager:
        async def __aenter__(self):
            print("   进入异步上下文")
            return "上下文资源"
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("   退出异步上下文")
    
    async def main_context():
        async with AsyncContextManager() as resource:
            print(f"   使用上下文资源：{resource}")
    
    asyncio.run(main_context())


def demo_async_network_requests():
    """演示异步网络请求"""
    print("\n" + "=" * 60)
    print("异步网络请求演示")
    print("=" * 60)
    
    if not AIOHTTP_AVAILABLE:
        print("   警告：aiohttp模块未安装，跳过网络请求演示。")
        print("   请运行 'pip install aiohttp' 安装后再运行此部分。")
        return
    
    async def fetch_url(url: str) -> Dict[str, Any]:
        """异步获取URL内容"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return {
                    "url": url,
                    "status": response.status,
                    "content_length": int(response.headers.get("Content-Length", 0))
                }
    
    async def main_network():
        urls = [
            "https://www.python.org",
            "https://www.google.com",
            "https://www.github.com",
            "https://www.bing.com"
        ]
        
        print(f"1. 并发请求 {len(urls)} 个URL：")
        
        # 创建任务列表
        tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
        
        # 等待所有任务完成
        results = await asyncio.gather(*tasks)
        
        # 输出结果
        for result in results:
            print(f"   URL: {result['url']:<25} 状态: {result['status']:<5} 大小: {result['content_length']:,}字节")
    
    try:
        asyncio.run(main_network())
    except aiohttp.ClientError as e:
        print(f"   网络请求错误：{e}")
    except Exception as e:
        print(f"   其他错误：{e}")


def main():
    """主函数"""
    print("=" * 60)
    print("异步编程难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. 同步与异步的区别")
    print("2. async/await基础语法")
    print("3. 事件循环的工作原理")
    print("4. 异步编程高级特性")
    print("5. 异步网络请求实战")
    print("=" * 60)
    
    # 运行各个演示
    demo_sync_vs_async()
    demo_async_await_basics()
    demo_event_loop()
    demo_asyncio_advanced()
    demo_async_network_requests()
    
    print("\n" + "=" * 60)
    print("异步编程难点总结:")
    print("1. async函数返回协程对象，必须使用await或事件循环执行")
    print("2. await只能在async函数内部使用")
    print("3. asyncio.gather()用于并发执行多个任务")
    print("4. 异步IO操作需要使用专门的异步库（如aiohttp替代requests）")
    print("5. 事件循环是异步编程的核心，负责调度协程执行")
    print("=" * 60)


if __name__ == "__main__":
    main()
