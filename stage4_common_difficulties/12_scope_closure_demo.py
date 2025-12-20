# -*- coding: utf-8 -*-
"""
第四阶段：变量作用域与闭包难点实战演示
演示LEGB规则、闭包陷阱、类作用域等核心概念
"""

from typing import Callable, List, Optional
import time

# 模块级别的全局变量
total = 0


def demo_scope_legb():
    """演示LEGB作用域规则"""
    print("=" * 60)
    print("LEGB作用域规则演示")
    print("=" * 60)
    
    # 全局变量
    global_var = "全局变量"
    
    def outer_function():
        """外层函数 - 包含闭包"""
        # 非局部变量
        outer_var = "外层变量"
        
        def inner_function():
            """内层函数 - 闭包"""
            # 局部变量
            local_var = "局部变量"
            
            print(f"   局部变量: {local_var}")
            print(f"   外层变量: {outer_var}")
            print(f"   全局变量: {global_var}")
            print(f"   内置函数: {len([1, 2, 3])}")  # 内置函数len
        
        inner_function()
        
        # 使用nonlocal关键字修改外层变量
        def inner_function_nonlocal():
            """使用nonlocal修改外层变量"""
            nonlocal outer_var
            outer_var = "修改后的外层变量"
            print(f"   非局部变量修改: {outer_var}")
        
        inner_function_nonlocal()
    
    outer_function()
    
    # 使用global关键字修改全局变量
    def modify_global():
        """修改全局变量"""
        global global_var
        global_var = "修改后的全局变量"
        print(f"   全局变量修改: {global_var}")
    
    modify_global()


def demo_closure_trap():
    """演示闭包的延迟绑定陷阱"""
    print("\n" + "=" * 60)
    print("闭包延迟绑定陷阱演示")
    print("=" * 60)
    
    # 陷阱1：循环中创建闭包的延迟绑定
    print("1. 闭包延迟绑定陷阱:")
    
    def create_multipliers_wrong():
        """错误示例：延迟绑定导致所有函数都返回同一个值"""
        multipliers = []
        for i in range(4):
            def multiplier(x):
                return x * i  # 这里的i是闭包捕获的变量，延迟绑定
            multipliers.append(multiplier)
        return multipliers
    
    def create_multipliers_correct():
        """正确示例：使用默认参数解决延迟绑定问题"""
        multipliers = []
        for i in range(4):
            def multiplier(x, i=i):  # 使用默认参数立即绑定i的值
                return x * i
            multipliers.append(multiplier)
        return multipliers
    
    # 测试错误示例
    print("   错误示例 - 所有函数都返回相同值:")
    multipliers_wrong = create_multipliers_wrong()
    for i, multiplier in enumerate(multipliers_wrong):
        result = multiplier(2)
        print(f"     multiplier[{i}](2) = {result} (预期: {i*2})")
    
    # 测试正确示例
    print("\n   正确示例 - 使用默认参数立即绑定:")
    multipliers_correct = create_multipliers_correct()
    for i, multiplier in enumerate(multipliers_correct):
        result = multiplier(2)
        print(f"     multiplier[{i}](2) = {result} (预期: {i*2})")
    
    # 陷阱2：修改闭包中捕获的可变对象
    print("\n2. 闭包中修改可变对象:")
    
    def outer():
        """外层函数，包含可变对象"""
        count = [0]  # 使用列表作为可变对象
        
        def inner():
            """内层函数，修改可变对象"""
            count[0] += 1
            return count[0]
        
        return inner
    
    counter = outer()
    print(f"   第一次调用: {counter()}")
    print(f"   第二次调用: {counter()}")
    print(f"   第三次调用: {counter()}")
    
    # 陷阱3：使用global关键字的风险
    print("\n3. 过度使用global的风险:")
    
    def add_wrong(x):
        """错误：使用global修改全局变量"""
        global total
        total += x
        return total
    
    def add_correct():
        """正确：使用闭包"""
        total = 0
        
        def inner(x):
            nonlocal total
            total += x
            return total
        
        return inner
    
    print("   错误示例 (使用global):")
    print(f"     add_wrong(5) = {add_wrong(5)}")
    print(f"     add_wrong(3) = {add_wrong(3)}")
    
    print("\n   正确示例 (使用闭包):")
    correct_counter = add_correct()
    print(f"     correct_counter(5) = {correct_counter(5)}")
    print(f"     correct_counter(3) = {correct_counter(3)}")


def demo_class_scope():
    """演示类作用域"""
    print("\n" + "=" * 60)
    print("类作用域演示")
    print("=" * 60)
    
    class ScopeChallenge:
        """演示类作用域的挑战"""
        
        class_var = 100  # 类变量
        
        def __init__(self):
            self.instance_var = 200  # 实例变量
        
        def instance_method(self):
            """实例方法：可以访问实例变量和类变量"""
            local_var = 300  # 局部变量
            return (self.instance_var, self.class_var, local_var)
        
        @classmethod
        def class_method(cls):
            """类方法：只能访问类变量"""
            local_var = 400  # 局部变量
            return (cls.class_var, local_var)
        
        @staticmethod
        def static_method():
            """静态方法：不能访问实例变量或类变量"""
            local_var = 500  # 局部变量
            return local_var
    
    # 测试
    print("1. 类和实例变量的访问:")
    obj = ScopeChallenge()
    print(f"   类变量 (通过类): {ScopeChallenge.class_var}")
    print(f"   类变量 (通过实例): {obj.class_var}")
    print(f"   实例变量: {obj.instance_var}")
    
    print("\n2. 方法调用:")
    print(f"   实例方法: {obj.instance_method()}")
    print(f"   类方法 (通过类): {ScopeChallenge.class_method()}")
    print(f"   类方法 (通过实例): {obj.class_method()}")
    print(f"   静态方法 (通过类): {ScopeChallenge.static_method()}")
    print(f"   静态方法 (通过实例): {obj.static_method()}")
    
    print("\n3. 修改变量:")
    # 修改类变量
    ScopeChallenge.class_var = 101
    print(f"   修改类变量后:")
    print(f"     类访问: {ScopeChallenge.class_var}")
    print(f"     实例访问: {obj.class_var}")
    
    # 修改实例变量
    obj.instance_var = 201
    print(f"   修改实例变量后: {obj.instance_var}")
    
    # 通过实例修改类变量（实际上是创建了一个同名的实例变量）
    obj.class_var = 202
    print(f"   通过实例修改类变量后:")
    print(f"     类访问: {ScopeChallenge.class_var}")
    print(f"     实例访问: {obj.class_var}")
    print(f"     实例.__dict__: {obj.__dict__}")


def demo_practical_scenarios():
    """演示实际应用场景"""
    print("\n" + "=" * 60)
    print("实际应用场景演示")
    print("=" * 60)
    
    # 场景1：使用闭包创建计数器
    print("1. 使用闭包创建计数器:")
    
    def create_counter(initial=0):
        """创建计数器"""
        count = initial
        
        def increment(step=1):
            nonlocal count
            count += step
            return count
        
        def decrement(step=1):
            nonlocal count
            count -= step
            return count
        
        def reset():
            nonlocal count
            count = initial
            return count
        
        def get_value():
            return count
        
        return increment, decrement, reset, get_value
    
    inc, dec, reset, get = create_counter(10)
    print(f"   初始值: {get()}")
    print(f"   增加1: {inc()}")
    print(f"   增加5: {inc(5)}")
    print(f"   减少2: {dec(2)}")
    print(f"   重置: {reset()}")
    print(f"   当前值: {get()}")
    
    # 场景2：使用闭包实现配置化函数
    print("\n2. 使用闭包实现配置化函数:")
    
    def create_formatter(prefix="", suffix="", separator=", "):
        """创建格式化函数"""
        def formatter(*args):
            """格式化参数"""
            formatted = separator.join(str(arg) for arg in args)
            return f"{prefix}{formatted}{suffix}"
        
        return formatter
    
    # 创建不同的格式化器
    list_formatter = create_formatter("[", "]", ", ")
    tuple_formatter = create_formatter("(", ")", ", ")
    sql_formatter = create_formatter("'", "'", "', '")
    
    print(f"   列表格式: {list_formatter(1, 2, 3)}")
    print(f"   元组格式: {tuple_formatter('a', 'b', 'c')}")
    print(f"   SQL格式: {sql_formatter('Alice', 'Bob', 'Charlie')}")
    
    # 场景3：使用闭包实现缓存
    print("\n3. 使用闭包实现简单缓存:")
    
    def create_cache(max_size=100):
        """创建缓存"""
        cache = {}
        keys = []  # 用于跟踪LRU
        
        def get(key):
            """获取缓存值"""
            if key in cache:
                # 更新LRU
                keys.remove(key)
                keys.append(key)
                return cache[key]
            return None
        
        def set(key, value):
            """设置缓存值"""
            if key in cache:
                keys.remove(key)
            elif len(cache) >= max_size:
                # 移除最旧的项
                oldest_key = keys.pop(0)
                del cache[oldest_key]
            
            cache[key] = value
            keys.append(key)
        
        def clear():
            """清空缓存"""
            cache.clear()
            keys.clear()
        
        return get, set, clear
    
    get, set, clear = create_cache(max_size=3)
    
    # 设置缓存
    set("a", 1)
    set("b", 2)
    set("c", 3)
    
    print(f"   获取'a': {get('a')}")  # 会更新LRU
    
    set("d", 4)  # 移除最旧的'b'
    print(f"   获取'b': {get('b')}")  # None
    print(f"   获取'c': {get('c')}")  # 3
    print(f"   获取'd': {get('d')}")  # 4


def main():
    """主函数"""
    print("=" * 60)
    print("变量作用域与闭包难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. LEGB作用域规则")
    print("2. 闭包的延迟绑定陷阱及解决方案")
    print("3. 类作用域与实例/类/静态方法")
    print("4. 实际应用场景")
    print("=" * 60)
    
    # 运行各个演示
    demo_scope_legb()
    demo_closure_trap()
    demo_class_scope()
    demo_practical_scenarios()
    
    print("\n" + "=" * 60)
    print("难点总结:")
    print("1. LEGB规则: Local → Enclosing → Global → Built-in")
    print("2. 闭包陷阱: 延迟绑定、可变对象修改、global过度使用")
    print("3. 解决方案: 默认参数、nonlocal关键字、合理设计作用域")
    print("4. 类作用域: 实例变量、类变量、三种方法类型的区别")
    print("=" * 60)


if __name__ == "__main__":
    main()