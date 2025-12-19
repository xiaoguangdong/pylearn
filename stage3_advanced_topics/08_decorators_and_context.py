# -*- coding: utf-8 -*-
"""
第三阶段：装饰器与上下文管理器
演示函数装饰器、类装饰器和with语句
"""

import time
from functools import wraps


def demo_function_decorator():
    """演示函数装饰器"""
    print("=" * 50)
    print("函数装饰器演示")
    print("=" * 50)
    
    # 简单的装饰器
    def simple_decorator(func):
        def wrapper():
            print("  装饰器：函数执行前")
            result = func()
            print("  装饰器：函数执行后")
            return result
        return wrapper
    
    @simple_decorator
    def say_hello():
        print("  你好，世界！")
    
    say_hello()
    print()
    
    # 带参数的装饰器
    def timer_decorator(func):
        @wraps(func)  # 保留原函数的元数据
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"  函数 {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
            return result
        return wrapper
    
    @timer_decorator
    def slow_function():
        time.sleep(0.1)
        return "完成"
    
    result = slow_function()
    print(f"  结果: {result}\n")
    
    # 带参数的装饰器（装饰器工厂）
    def repeat(times):
        """重复执行函数的装饰器"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for i in range(times):
                    print(f"  第 {i+1} 次执行:")
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator
    
    @repeat(3)
    def greet(name):
        print(f"    你好, {name}!")
        return f"问候{name}"
    
    results = greet("Python")
    print(f"  所有结果: {results}\n")
    
    # 类装饰器
    class CountCalls:
        """统计函数调用次数的装饰器"""
        def __init__(self, func):
            self.func = func
            self.count = 0
        
        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"  函数 {self.func.__name__} 被调用了 {self.count} 次")
            return self.func(*args, **kwargs)
    
    @CountCalls
    def example_function():
        return "示例函数"
    
    example_function()
    example_function()
    example_function()
    
    print()


def demo_class_decorator():
    """演示类装饰器"""
    print("=" * 50)
    print("类装饰器演示")
    print("=" * 50)
    
    # 为类添加方法的装饰器
    def add_method(cls):
        """为类添加新方法的装饰器"""
        def new_method(self):
            return f"这是添加到 {cls.__name__} 的新方法"
        cls.new_method = new_method
        return cls
    
    @add_method
    class MyClass:
        def __init__(self, name):
            self.name = name
    
    obj = MyClass("测试")
    print(f"调用新方法: {obj.new_method()}\n")
    
    # 单例模式装饰器
    def singleton(cls):
        """单例模式装饰器"""
        instances = {}
        
        def get_instance(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        
        return get_instance
    
    @singleton
    class Database:
        def __init__(self):
            print("  数据库连接已创建")
            self.data = []
    
    db1 = Database()
    db2 = Database()
    print(f"  db1 is db2: {db1 is db2}")  # 应该是True
    
    print()


def demo_context_manager():
    """演示上下文管理器（with语句）"""
    print("=" * 50)
    print("上下文管理器演示")
    print("=" * 50)
    
    # 使用类实现上下文管理器
    class FileManager:
        """文件管理器上下文管理器"""
        
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            print(f"  打开文件: {self.filename}")
            self.file = open(self.filename, self.mode, encoding="utf-8")
            return self.file
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"  关闭文件: {self.filename}")
            if self.file:
                self.file.close()
            return False  # 不抑制异常
    
    # 使用上下文管理器
    with FileManager("demo.txt", "w") as f:
        f.write("这是测试内容")
        print("  文件写入完成")
    
    with FileManager("demo.txt", "r") as f:
        content = f.read()
        print(f"  读取内容: {content}")
    
    # 清理
    import os
    os.remove("demo.txt")
    print()
    
    # 使用contextlib实现上下文管理器
    from contextlib import contextmanager
    
    @contextmanager
    def timer_context():
        """计时上下文管理器"""
        start = time.time()
        print("  开始计时...")
        try:
            yield
        finally:
            end = time.time()
            print(f"  耗时: {end - start:.4f}秒")
    
    with timer_context():
        time.sleep(0.1)
        print("  执行一些操作...")
    
    print()
    
    # 多个上下文管理器
    class Lock:
        """简单的锁模拟"""
        def __enter__(self):
            print("  获取锁")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("  释放锁")
            return False
    
    with FileManager("demo2.txt", "w") as f, Lock():
        f.write("使用多个上下文管理器")
        print("  写入完成")
    
    os.remove("demo2.txt")
    
    print()


def demo_common_decorators():
    """演示常用装饰器模式"""
    print("=" * 50)
    print("常用装饰器模式演示")
    print("=" * 50)
    
    # 缓存装饰器
    def cache(func):
        """简单的缓存装饰器"""
        cache_dict = {}
        
        @wraps(func)
        def wrapper(*args):
            if args in cache_dict:
                print(f"  缓存命中: {func.__name__}{args}")
                return cache_dict[args]
            result = func(*args)
            cache_dict[args] = result
            print(f"  计算结果: {func.__name__}{args} = {result}")
            return result
        
        return wrapper
    
    @cache
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("斐波那契数列（带缓存）:")
    result = fibonacci(5)
    print(f"  fibonacci(5) = {result}\n")
    
    # 权限检查装饰器
    def require_permission(permission):
        """权限检查装饰器"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # 模拟权限检查
                user_permissions = ["read", "write"]  # 假设用户权限
                if permission not in user_permissions:
                    raise PermissionError(f"需要 {permission} 权限")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @require_permission("read")
    def read_data():
        return "数据内容"
    
    @require_permission("admin")
    def admin_operation():
        return "管理员操作"
    
    try:
        result = read_data()
        print(f"读取数据: {result}")
    except PermissionError as e:
        print(f"权限错误: {e}")
    
    try:
        admin_operation()
    except PermissionError as e:
        print(f"权限错误: {e}")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_function_decorator()
    demo_class_decorator()
    demo_context_manager()
    demo_common_decorators()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

