# -*- coding: utf-8 -*-
"""
第四阶段：元类与元编程难点实战演示
演示type类、__new__与__init__的区别、元类的实际应用等核心概念
"""

import functools
import inspect
from typing import Type, Dict, Any, List
from datetime import datetime


def demo_type_class():
    """演示type类与类的创建过程"""
    print("=" * 60)
    print("type类与类创建过程演示")
    print("=" * 60)
    
    print("1. type类的基本使用：")
    print(f"   int的类型: {type(int)}")
    print(f"   list的类型: {type(list)}")
    print(f"   dict的类型: {type(dict)}")
    print(f"   type的类型: {type(type)}")
    
    print("\n2. 使用type创建类：")
    
    # 定义类的属性和方法
    class_attrs = {
        'class_var': 100,
        'greet': lambda self, name: f"Hello, {name}! I'm {self.name}"
    }
    
    # 使用type动态创建类
    DynamicClass = type("DynamicClass",  # 类名
                      (object,),        # 父类元组
                      class_attrs)      # 类属性和方法
    
    # 使用创建的类
    obj = DynamicClass()
    obj.name = "Dynamic Object"
    print(f"   类名: {DynamicClass.__name__}")
    print(f"   父类: {DynamicClass.__bases__}")
    print(f"   类变量: {DynamicClass.class_var}")
    print(f"   实例方法调用: {obj.greet('Alice')}")
    
    print("\n3. type创建类的完整过程：")
    
    # 定义初始化方法
    def __init__(self, name):
        self.name = name
    
    # 定义另一个方法
    def say_age(self, age):
        return f"{self.name} is {age} years old"
    
    # 创建带有初始化方法的类
    Person = type("Person", 
                 (object,), 
                 {
                     '__init__': __init__, 
                     'say_age': say_age,
                     'species': 'Homo sapiens'
                 })
    
    person = Person("Bob")
    print(f"   实例: {person}")
    print(f"   实例属性: {person.name}")
    print(f"   类属性: {Person.species}")
    print(f"   方法调用: {person.say_age(30)}")


def demo_new_init_difference():
    """演示__new__与__init__的区别"""
    print("\n" + "=" * 60)
    print("__new__与__init__的区别演示")
    print("=" * 60)
    
    class NewInitDemo:
        """演示__new__与__init__的区别"""
        
        def __new__(cls, *args, **kwargs):
            """创建实例"""
            print(f"   __new__被调用: {cls}, args: {args}, kwargs: {kwargs}")
            # 调用父类的__new__创建实例
            instance = super().__new__(cls)
            # 在__new__中可以修改实例
            instance.new_attribute = "在__new__中添加的属性"
            return instance
        
        def __init__(self, name, value):
            """初始化实例"""
            print(f"   __init__被调用: {self}, name: {name}, value: {value}")
            self.name = name
            self.value = value
    
    print("1. 创建实例过程：")
    obj = NewInitDemo("test", 100)
    
    print("\n2. 实例的属性：")
    print(f"   name: {obj.name}")
    print(f"   value: {obj.value}")
    print(f"   new_attribute: {obj.new_attribute}")
    
    print("\n3. 单例模式使用__new__：")
    
    class Singleton:
        """使用__new__实现单例模式"""
        _instance = None
        
        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
        
        def __init__(self, name):
            self.name = name
    
    s1 = Singleton("First")
    s2 = Singleton("Second")
    
    print(f"   s1: {s1}, name: {s1.name}")
    print(f"   s2: {s2}, name: {s2.name}")
    print(f"   s1 is s2: {s1 is s2}")
    
    print("\n4. 不可变类使用__new__：")
    
    class ImmutablePoint:
        """不可变点类"""
        
        def __new__(cls, x, y):
            instance = super().__new__(cls)
            # 在__new__中设置属性
            instance._x = x
            instance._y = y
            return instance
        
        @property
        def x(self):
            return self._x
        
        @property
        def y(self):
            return self._y
    
    p = ImmutablePoint(10, 20)
    print(f"   点坐标: ({p.x}, {p.y})")
    
    try:
        p.x = 30
        print("   可以修改属性（错误！）")
    except AttributeError:
        print("   不能修改属性（正确！）")


def demo_custom_metaclasses():
    """演示自定义元类"""
    print("\n" + "=" * 60)
    print("自定义元类演示")
    print("=" * 60)
    
    class AutoRegisterMeta(type):
        """自动注册子类的元类"""
        
        def __init__(cls, name, bases, attrs):
            # 跳过基类
            if not hasattr(cls, '_registry'):
                cls._registry = []
            else:
                # 注册子类
                cls._registry.append(cls)
            super().__init__(name, bases, attrs)
    
    class BaseComponent(metaclass=AutoRegisterMeta):
        """基础组件类"""
        pass
    
    class Button(BaseComponent):
        """按钮组件"""
        def render(self):
            return "<button>Click</button>"
    
    class TextBox(BaseComponent):
        """文本框组件"""
        def render(self):
            return "<input type='text' />"
    
    class CheckBox(BaseComponent):
        """复选框组件"""
        def render(self):
            return "<input type='checkbox' />"
    
    print("1. 自动注册子类：")
    print(f"   已注册的组件类: {[cls.__name__ for cls in BaseComponent._registry]}")
    
    print("\n2. 统一接口调用：")
    for component_class in BaseComponent._registry:
        instance = component_class()
        print(f"   {component_class.__name__}: {instance.render()}")
    
    print("\n3. 验证装饰器的元类：")
    
    class ValidatedMeta(type):
        """验证属性类型的元类"""
        
        def __new__(cls, name, bases, attrs):
            # 检查是否有类型注解
            for attr_name, attr_value in attrs.items():
                if inspect.isfunction(attr_value) and attr_name != "__init__":
                    sig = inspect.signature(attr_value)
                    if sig.return_annotation is not inspect.Parameter.empty:
                        attrs[attr_name] = cls.wrap_function(attr_value, sig.return_annotation)
            return super().__new__(cls, name, bases, attrs)
        
        @staticmethod
        def wrap_function(func, return_type):
            """包装函数以验证返回类型"""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                if not isinstance(result, return_type):
                    raise TypeError(f"函数 {func.__name__} 应该返回 {return_type.__name__}，但返回了 {type(result).__name__}")
                return result
            return wrapper
    
    class Calculator(metaclass=ValidatedMeta):
        """计算器类"""
        
        def add(self, a: int, b: int) -> int:
            return a + b
        
        def multiply(self, a: int, b: int) -> int:
            return a * b
        
        def stringify(self, value: int) -> str:
            return str(value)
    
    calc = Calculator()
    print(f"   加法: {calc.add(5, 3)}")
    print(f"   乘法: {calc.multiply(5, 3)}")
    print(f"   字符串化: {calc.stringify(42)}")
    
    try:
        calc.add(5, "3")
        print("   类型错误未被捕获（错误！）")
    except TypeError as e:
        print(f"   类型错误被正确捕获: {e}")


def demo_metaprogramming_applications():
    """演示元编程的实际应用"""
    print("\n" + "=" * 60)
    print("元编程实际应用演示")
    print("=" * 60)
    
    print("1. 实现ORM映射：")
    
    class ModelMeta(type):
        """ORM模型元类"""
        
        def __new__(cls, name, bases, attrs):
            if name == "Model":
                return super().__new__(cls, name, bases, attrs)
            
            # 收集字段信息
            fields = {}
            for attr_name, attr_value in attrs.items():
                if isinstance(attr_value, str):
                    fields[attr_name] = attr_value
            
            # 添加字段信息到类
            attrs['__fields__'] = fields
            attrs['__table__'] = name.lower()
            
            return super().__new__(cls, name, bases, attrs)
    
    class Model(metaclass=ModelMeta):
        """ORM模型基类"""
        
        def __init__(self, **kwargs):
            for field, _ in self.__fields__.items():
                if field in kwargs:
                    setattr(self, field, kwargs[field])
        
        def save(self):
            """保存到数据库"""
            fields = ', '.join(self.__fields__.keys())
            values = ', '.join([f"'{getattr(self, field, '')}'" for field in self.__fields__])
            sql = f"INSERT INTO {self.__table__} ({fields}) VALUES ({values})"
            print(f"   执行SQL: {sql}")
    
    class User(Model):
        """用户模型"""
        name = "VARCHAR(255)"
        email = "VARCHAR(255)"
        age = "INT"
    
    class Product(Model):
        """产品模型"""
        name = "VARCHAR(255)"
        price = "DECIMAL(10,2)"
        stock = "INT"
    
    # 创建并保存模型
    user = User(name="Alice", email="alice@example.com", age=30)
    user.save()
    
    product = Product(name="Laptop", price=999.99, stock=10)
    product.save()
    
    print("\n2. 实现配置类：")
    
    class ConfigMeta(type):
        """配置类元类"""
        
        def __getattr__(cls, name):
            if name in cls.__annotations__:
                return None
            raise AttributeError(f"类 {cls.__name__} 没有属性 {name}")
        
        def __setattr__(cls, name, value):
            if name in cls.__annotations__:
                expected_type = cls.__annotations__[name]
                if isinstance(value, expected_type):
                    super().__setattr__(name, value)
                else:
                    raise TypeError(f"属性 {name} 应该是 {expected_type.__name__} 类型")
            else:
                super().__setattr__(name, value)
    
    class AppConfig(metaclass=ConfigMeta):
        """应用配置类"""
        DEBUG: bool
        PORT: int
        HOST: str
        DATABASE_URL: str
    
    # 配置应用
    AppConfig.DEBUG = True
    AppConfig.PORT = 8080
    AppConfig.HOST = "localhost"
    AppConfig.DATABASE_URL = "sqlite:///app.db"
    
    print(f"   DEBUG: {AppConfig.DEBUG}")
    print(f"   PORT: {AppConfig.PORT}")
    print(f"   HOST: {AppConfig.HOST}")
    print(f"   DATABASE_URL: {AppConfig.DATABASE_URL}")
    
    try:
        AppConfig.PORT = "8080"  # 应该是整数
        print("   类型错误未被捕获（错误！）")
    except TypeError as e:
        print(f"   类型错误被正确捕获: {e}")


def main():
    """主函数"""
    print("=" * 60)
    print("元类与元编程难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. type类与类的创建过程")
    print("2. __new__与__init__的区别")
    print("3. 自定义元类的实现")
    print("4. 元编程的实际应用场景")
    print("=" * 60)
    
    # 运行各个演示
    demo_type_class()
    demo_new_init_difference()
    demo_custom_metaclasses()
    demo_metaprogramming_applications()
    
    print("\n" + "=" * 60)
    print("元类与元编程难点总结:")
    print("1. type是Python中所有类的元类，包括它自己")
    print("2. __new__负责创建实例，__init__负责初始化实例")
    print("3. 元类可以拦截类的创建过程，用于自动注册、验证等")
    print("4. 元编程用于编写能够修改其他程序的程序，如ORM、配置系统等")
    print("5. 合理使用元编程可以提高代码的复用性和灵活性")
    print("=" * 60)


if __name__ == "__main__":
    main()
