# -*- coding: utf-8 -*-
"""
第四阶段：装饰器与元类难点实战演示
演示函数装饰器、类装饰器、带参数装饰器、元类、元编程等高级主题
"""

import time
import functools
from typing import Callable, Any, Type, Dict, List
from datetime import datetime
import inspect


# ==================== 装饰器部分 ====================

def demo_basic_decorators():
    """演示基本装饰器"""
    print("=" * 60)
    print("基本装饰器演示")
    print("=" * 60)
    
    # 1. 简单装饰器
    print("1. 简单装饰器（无参数）:")
    
    def simple_decorator(func: Callable) -> Callable:
        """简单装饰器：打印函数调用信息"""
        @functools.wraps(func)  # 保留原函数信息
        def wrapper(*args, **kwargs):
            print(f"   调用函数: {func.__name__}")
            print(f"   参数: args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"   返回值: {result}")
            return result
        return wrapper
    
    @simple_decorator
    def add_numbers(a: int, b: int) -> int:
        """两数相加"""
        return a + b
    
    result = add_numbers(10, 20)
    print(f"   最终结果: {result}")
    
    # 检查函数信息是否保留
    print(f"\n   函数信息:")
    print(f"     名称: {add_numbers.__name__}")
    print(f"     文档: {add_numbers.__doc__}")
    print(f"     模块: {add_numbers.__module__}")
    
    # 2. 带参数的装饰器
    print("\n2. 带参数的装饰器:")
    
    def repeat(times: int):
        """重复执行指定次数"""
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for i in range(times):
                    print(f"   第{i+1}次执行:")
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator
    
    @repeat(times=3)
    def greet(name: str) -> str:
        """打招呼"""
        return f"Hello, {name}!"
    
    results = greet("Alice")
    print(f"   所有结果: {results}")


def demo_class_decorators():
    """演示类装饰器"""
    print("\n" + "=" * 60)
    print("类装饰器演示")
    print("=" * 60)
    
    # 1. 类作为装饰器
    print("1. 类作为装饰器:")
    
    class Timer:
        """计时装饰器类"""
        
        def __init__(self, func: Callable):
            functools.update_wrapper(self, func)
            self.func = func
            self.execution_times = []
        
        def __call__(self, *args, **kwargs):
            start_time = time.perf_counter()
            result = self.func(*args, **kwargs)
            end_time = time.perf_counter()
            
            execution_time = end_time - start_time
            self.execution_times.append(execution_time)
            
            print(f"   函数 {self.func.__name__} 执行时间: {execution_time:.6f}秒")
            print(f"   平均执行时间: {sum(self.execution_times)/len(self.execution_times):.6f}秒")
            return result
        
        def __get__(self, instance, owner):
            """支持实例方法"""
            if instance is None:
                return self
            return functools.partial(self.__call__, instance)
    
    @Timer
    def calculate_factorial(n: int) -> int:
        """计算阶乘"""
        result = 1
        for i in range(1, n + 1):
            result *= i
            time.sleep(0.001)  # 模拟耗时操作
        return result
    
    print(f"   5的阶乘: {calculate_factorial(5)}")
    print(f"   10的阶乘: {calculate_factorial(10)}")
    
    # 2. 带参数的类装饰器
    print("\n2. 带参数的类装饰器:")
    
    class Retry:
        """重试装饰器类"""
        
        def __init__(self, max_attempts: int = 3, delay: float = 1.0):
            self.max_attempts = max_attempts
            self.delay = delay
        
        def __call__(self, func: Callable):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                
                for attempt in range(self.max_attempts):
                    try:
                        print(f"   第{attempt + 1}次尝试...")
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        print(f"   失败: {e}")
                        if attempt < self.max_attempts - 1:
                            time.sleep(self.delay)
                
                raise RuntimeError(f"函数 {func.__name__} 在 {self.max_attempts} 次尝试后仍然失败") from last_exception
            
            return wrapper
    
    @Retry(max_attempts=3, delay=0.5)
    def unreliable_operation():
        """不可靠的操作（模拟失败）"""
        import random
        if random.random() < 0.7:  # 70%概率失败
            raise ValueError("随机失败")
        return "操作成功"
    
    try:
        result = unreliable_operation()
        print(f"   结果: {result}")
    except Exception as e:
        print(f"   最终失败: {e}")


def demo_property_method_decorators():
    """演示属性装饰器"""
    print("\n" + "=" * 60)
    print("属性装饰器演示")
    print("=" * 60)
    
    class SmartProduct:
        """智能产品类 - 演示@property, @classmethod, @staticmethod"""
        
        tax_rate = 0.13  # 类属性
        
        def __init__(self, name: str, price: float):
            self._name = name
            self._price = price
            self._discount = 0.0
        
        @property
        def name(self) -> str:
            """产品名称（只读属性）"""
            return self._name
        
        @property
        def price(self) -> float:
            """价格（带折扣计算）"""
            return self._price * (1 - self._discount)
        
        @price.setter
        def price(self, value: float):
            """价格设置器"""
            if value < 0:
                raise ValueError("价格不能为负数")
            self._price = value
        
        @property
        def discount(self) -> float:
            """折扣率"""
            return self._discount
        
        @discount.setter
        def discount(self, value: float):
            """折扣设置器"""
            if not 0 <= value <= 1:
                raise ValueError("折扣率必须在0到1之间")
            self._discount = value
        
        @property
        def price_with_tax(self) -> float:
            """含税费价格（只读）"""
            return self.price * (1 + self.tax_rate)
        
        @classmethod
        def update_tax_rate(cls, new_rate: float):
            """更新税率（类方法）"""
            if new_rate < 0:
                raise ValueError("税率不能为负数")
            cls.tax_rate = new_rate
            print(f"   税率已更新为: {new_rate*100:.2f}%")
        
        @staticmethod
        def calculate_discount_price(original_price: float, discount_rate: float) -> float:
            """计算折扣价格（静态方法）"""
            if not 0 <= discount_rate <= 1:
                raise ValueError("折扣率必须在0到1之间")
            return original_price * (1 - discount_rate)
    
    # 创建产品实例
    print("1. 创建产品实例:")
    product = SmartProduct("智能手表", 1999.99)
    print(f"   产品名称: {product.name}")
    print(f"   原价: ¥{product.price:.2f}")
    print(f"   含税费价格: ¥{product.price_with_tax:.2f}")
    
    # 修改价格和折扣
    print("\n2. 修改价格和折扣:")
    product.price = 1799.99
    product.discount = 0.2  # 20%折扣
    print(f"   新价格: ¥{product.price:.2f}")
    print(f"   折扣率: {product.discount*100:.0f}%")
    print(f"   折扣后价格: ¥{product.price:.2f}")
    print(f"   含税费折扣价格: ¥{product.price_with_tax:.2f}")
    
    # 使用类方法
    print("\n3. 使用类方法更新税率:")
    SmartProduct.update_tax_rate(0.16)
    print(f"   更新后含税费价格: ¥{product.price_with_tax:.2f}")
    
    # 使用静态方法
    print("\n4. 使用静态方法计算折扣:")
    original = 2000.0
    discount = 0.15
    discounted = SmartProduct.calculate_discount_price(original, discount)
    print(f"   原价 ¥{original:.2f}, 折扣 {discount*100:.0f}% = ¥{discounted:.2f}")
    
    # 演示属性保护
    print("\n5. 演示属性保护:")
    try:
        product.price = -1000
    except ValueError as e:
        print(f"   设置负价格: {e}")
    
    try:
        product.discount = 1.5  # 超过100%折扣
    except ValueError as e:
        print(f"   设置无效折扣: {e}")


# ==================== 元类部分 ====================

def demo_metaclasses():
    """演示元类的基本概念"""
    print("\n" + "=" * 60)
    print("元类基本概念演示")
    print("=" * 60)
    
    # 1. 使用type创建类（元类的基本使用）
    print("1. 使用type动态创建类:")
    
    # 定义类的方法
    def greet_method(self):
        return f"Hello, {self.name}!"
    
    # 使用type创建类
    DynamicClass = type("DynamicClass",  # 类名
                      (object,),        # 父类
                      {'greet': greet_method,  # 方法
                       'class_var': 100,       # 类变量
                       '__init__': lambda self, name: setattr(self, 'name', name)  # 初始化方法
                      })
    
    # 创建实例并使用
    obj = DynamicClass("Alice")
    print(f"   类名: {DynamicClass.__name__}")
    print(f"   父类: {DynamicClass.__bases__}")
    print(f"   类变量: {DynamicClass.class_var}")
    print(f"   实例方法调用: {obj.greet()}")
    
    # 2. 自定义元类
    print("\n2. 自定义元类:")
    
    class MyMeta(type):
        """自定义元类，用于拦截类的创建过程"""
        
        def __new__(cls, name, bases, attrs):
            """创建类时调用"""
            print(f"   元类 __new__ 被调用: 创建类 '{name}'")
            print(f"   父类: {bases}")
            print(f"   属性: {list(attrs.keys())}")
            
            # 添加新属性
            attrs['created_by'] = 'MyMeta'
            
            # 验证必须有文档字符串
            if not attrs.get('__doc__'):
                raise TypeError(f"类 '{name}' 必须有文档字符串")
            
            # 修改属性名（将所有方法名转为小写）
            modified_attrs = {}
            for key, value in attrs.items():
                if callable(value) and not key.startswith('__'):
                    modified_attrs[key.lower()] = value
                else:
                    modified_attrs[key] = value
            
            return super().__new__(cls, name, bases, modified_attrs)
        
        def __init__(cls, name, bases, attrs):
            """初始化类时调用"""
            print(f"   元类 __init__ 被调用: 初始化类 '{name}'")
            super().__init__(name, bases, attrs)
    
    try:
        # 使用自定义元类
        class Person(metaclass=MyMeta):
            """人 类"""
            species = "Homo sapiens"
            
            def say_hello(self, name):
                return f"Hello {name}, I'm a {self.species}"
            
            def calculate_age(self, birth_year):
                current_year = datetime.now().year
                return current_year - birth_year
        
        print("\n   类创建成功!")
        print(f"   created_by属性: {Person.created_by}")
        
        # 注意方法名已被转换为小写
        person = Person()
        print(f"   调用say_hello(): {person.say_hello('Bob')}")
        print(f"   调用calculate_age(): {person.calculate_age(1990)}")
        
    except TypeError as e:
        print(f"   类创建失败: {e}")
    
    # 3. 元类的实际应用 - 单例模式
    print("\n3. 元类应用 - 单例模式:")
    
    class SingletonMeta(type):
        """单例元类"""
        _instances = {}
        
        def __call__(cls, *args, **kwargs):
            """拦截实例创建"""
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
    
    class DatabaseConnection(metaclass=SingletonMeta):
        """数据库连接类"""
        
        def __init__(self, connection_string):
            print(f"   初始化数据库连接: {connection_string}")
            self.connection_string = connection_string
            # 模拟连接过程
            time.sleep(0.1)
        
        def query(self, sql):
            return f"执行查询: {sql}"
    
    # 创建多个实例（实际上是同一个实例）
    conn1 = DatabaseConnection("mysql://localhost:3306/db1")
    conn2 = DatabaseConnection("mysql://localhost:3306/db1")
    
    print(f"   conn1 is conn2: {conn1 is conn2}")
    print(f"   两个实例是否相同: {id(conn1) == id(conn2)}")


# ==================== 元编程部分 ====================

def demo_metaprogramming():
    """演示元编程技术"""
    print("\n" + "=" * 60)
    print("元编程技术演示")
    print("=" * 60)
    
    # 1. 使用装饰器进行元编程
    print("1. 使用装饰器进行元编程:")
    
    def register_class(cls):
        """注册类到注册表的装饰器"""
        if not hasattr(register_class, 'registry'):
            register_class.registry = {}
        register_class.registry[cls.__name__] = cls
        return cls
    
    @register_class
    class UserService:
        """用户服务类"""
        pass
    
    @register_class
    class OrderService:
        """订单服务类"""
        pass
    
    print(f"   注册的服务类: {list(register_class.registry.keys())}")
    
    # 2. 使用inspect模块进行元编程
    print("\n2. 使用inspect模块进行元编程:")
    
    def inspect_function(func):
        """检查函数的元信息"""
        print(f"   函数名: {func.__name__}")
        print(f"   文档字符串: {func.__doc__}")
        print(f"   参数: {inspect.signature(func)}")
        print(f"   模块: {func.__module__}")
    
    def sample_function(x: int, y: str, z: bool = True) -> dict:
        """示例函数，演示inspect功能"""
        return {"x": x, "y": y, "z": z}
    
    inspect_function(sample_function)
    
    # 3. 使用装饰器创建类方法
    print("\n3. 使用装饰器创建类方法:")
    
    def class_method_decorator(func):
        """将普通方法转换为类方法"""
        return classmethod(func)
    
    class ExampleClass:
        """示例类"""
        value = 42
        
        def get_value(cls):
            return cls.value
        
        get_value = class_method_decorator(get_value)
    
    print(f"   类方法调用: {ExampleClass.get_value()}")
    
    # 4. 动态添加属性和方法
    print("\n4. 动态添加属性和方法:")
    
    class DynamicClassExample:
        """动态类示例"""
        pass
    
    # 动态添加属性
    DynamicClassExample.new_attribute = "动态添加的属性"
    
    # 动态添加实例方法
    def dynamic_method(self):
        return f"动态方法调用，属性值: {self.new_attribute}"
    
    DynamicClassExample.dynamic_method = dynamic_method
    
    # 动态添加类方法
    def dynamic_class_method(cls):
        return f"动态类方法，属性值: {cls.new_attribute}"
    
    DynamicClassExample.dynamic_class_method = classmethod(dynamic_class_method)
    
    obj = DynamicClassExample()
    print(f"   动态属性: {DynamicClassExample.new_attribute}")
    print(f"   动态实例方法: {obj.dynamic_method()}")
    print(f"   动态类方法: {DynamicClassExample.dynamic_class_method()}")


def main():
    """主函数"""
    print("=" * 60)
    print("装饰器与元类难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. 基本装饰器（函数装饰器、带参数装饰器）")
    print("2. 类装饰器（计时、重试功能）")
    print("3. 属性装饰器（@property, setter方法）")
    print("4. 类方法与静态方法装饰器")
    print("5. 元类基础与自定义元类")
    print("6. 元类应用（单例模式）")
    print("7. 元编程技术")
    print("=" * 60)
    
    # 运行各个演示
    demo_basic_decorators()
    demo_class_decorators()
    demo_property_method_decorators()
    demo_metaclasses()
    demo_metaprogramming()
    
    print("\n" + "=" * 60)
    print("演示完成!")
    print("=" * 60)


if __name__ == "__main__":
    main()