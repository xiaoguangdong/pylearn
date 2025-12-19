# -*- coding: utf-8 -*-
"""
第一阶段：函数与模块
演示函数定义、参数传递、Lambda表达式和模块使用
"""


def demo_function_basics():
    """演示函数定义与调用"""
    print("=" * 50)
    print("函数定义与调用演示")
    print("=" * 50)
    
    def greet(name):
        """简单的问候函数"""
        return f"你好, {name}!"
    
    def add(a, b):
        """加法函数"""
        return a + b
    
    print(greet("Python学习者"))
    print(f"3 + 5 = {add(3, 5)}")
    
    print()


def demo_parameters():
    """演示参数传递"""
    print("=" * 50)
    print("参数传递演示")
    print("=" * 50)
    
    # 位置参数
    def greet(name, age):
        return f"{name}今年{age}岁"
    
    print(f"位置参数: {greet('张三', 25)}")
    
    # 关键字参数
    print(f"关键字参数: {greet(age=30, name='李四')}")
    
    # 默认参数
    def introduce(name, city="北京"):
        return f"{name}来自{city}"
    
    print(f"默认参数: {introduce('王五')}")
    print(f"覆盖默认参数: {introduce('赵六', '上海')}")
    
    # *args - 可变位置参数
    def sum_all(*args):
        return sum(args)
    
    print(f"*args示例: sum_all(1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")
    
    # **kwargs - 可变关键字参数
    def print_info(**kwargs):
        print(f"kwargs: type(kwargs) is {type(kwargs)}")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    
    print("**kwargs示例:")
    print_info(姓名="张三", 年龄=25, 职业="程序员")
    
    # 组合使用
    def flexible_func(required, *args, default="默认值", **kwargs):
        print(f"  必需参数: {required}")
        print(f"  *args: {args}")
        print(f"  默认参数: {default}")
        print(f"  **kwargs: {kwargs}")
    
    print("\n组合参数示例:")
    flexible_func("必需", 1, 2, 3, default="自定义", key1="value1", key2="value2")
    
    print()


def demo_lambda():
    """演示Lambda表达式"""
    print("=" * 50)
    print("Lambda表达式演示")
    print("=" * 50)
    
    # 简单的lambda函数
    square = lambda x: x ** 2
    print(f"square(5) = {square(5)}")
    
    # lambda与map结合
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"map(lambda x: x**2, {numbers}) = {squared}")
    
    # lambda与filter结合
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter(lambda x: x%2==0, {numbers}) = {even_numbers}")
    
    # lambda与sorted结合
    students = [("张三", 85), ("李四", 92), ("王五", 78)]
    sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
    print(f"按分数排序: {sorted_by_score}")
    
    print()


def demo_builtin_functions():
    """演示常用内置函数"""
    print("=" * 50)
    print("常用内置函数演示")
    print("=" * 50)
    
    # len() - 获取长度
    print(f"len('Python') = {len('Python')}")
    print(f"len([1, 2, 3, 4, 5]) = {len([1, 2, 3, 4, 5])}")
    
    # range() - 生成数字序列
    print(f"range(5) = {list(range(5))}")
    print(f"range(2, 10, 2) = {list(range(2, 10, 2))}")
    
    # enumerate() - 枚举
    print("\nenumerate()示例:")
    for index, value in enumerate(["a", "b", "c"]):
        print(f"  索引{index}: {value}")
    
    # zip() - 组合多个序列
    print("\nzip()示例:")
    names = ["张三", "李四", "王五"]
    ages = [25, 30, 28]
    for name, age in zip(names, ages):
        print(f"  {name}: {age}岁")
    
    # max(), min(), sum()
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nmax({numbers}) = {max(numbers)}")
    print(f"min({numbers}) = {min(numbers)}")
    print(f"sum({numbers}) = {sum(numbers)}")
    
    # isinstance() - 类型检查
    print(f"\nisinstance(5, int) = {isinstance(5, int)}")
    print(f"isinstance('hello', str) = {isinstance('hello', str)}")
    
    print()


def demo_unpacking():
    """演示参数解包：* 和 ** 在函数调用时的用法"""
    print("=" * 50)
    print("参数解包演示（* 和 ** 在函数调用时）")
    print("=" * 50)
    
    # 定义一个需要多个参数的函数
    def greet(name, age, city):
        return f"{name}，{age}岁，来自{city}"
    
    # 方式1：直接传递参数
    print("方式1 - 直接传递参数:")
    print(f"  {greet('张三', 25, '北京')}")
    
    # 方式2：使用 * 解包元组/列表作为位置参数
    print("\n方式2 - 使用 * 解包元组作为位置参数:")
    person_info = ('李四', 30, '上海')
    print(f"  person_info = {person_info}")
    print(f"  greet(*person_info) = {greet(*person_info)}")
    
    # 也可以解包列表
    person_list = ['王五', 28, '广州']
    print(f"\n  解包列表: greet(*{person_list}) = {greet(*person_list)}")
    
    # 方式3：使用 ** 解包字典作为关键字参数
    print("\n方式3 - 使用 ** 解包字典作为关键字参数:")
    person_dict = {'name': '赵六', 'age': 32, 'city': '深圳'}
    print(f"  person_dict = {person_dict}")
    print(f"  greet(**person_dict) = {greet(**person_dict)}")
    
    # 方式4：混合使用
    print("\n方式4 - 混合使用 * 和 **:")
    def flexible_greet(name, age, city="未知", **extra_info):
        result = f"{name}，{age}岁，来自{city}"
        if extra_info:
            info_str = ', '.join([f"{k}={v}" for k, v in extra_info.items()])
            result += f"，其他信息：{info_str}"
        return result
    
    # 使用元组和字典解包
    base_info = ('孙七', 27)
    extra_dict = {'city': '杭州', '职业': '程序员', '爱好': '编程'}
    print(f"  base_info = {base_info}")
    print(f"  extra_dict = {extra_dict}")
    print(f"  结果: {flexible_greet(*base_info, **extra_dict)}")
    
    # 重要说明
    print("\n" + "=" * 50)
    print("重要说明：")
    print("=" * 50)
    print("1. 函数定义时：")
    print("   - *args: 接收多个位置参数，打包成元组(tuple)")
    print("   - **kwargs: 接收多个关键字参数，打包成字典(dict)")
    print("\n2. 函数调用时：")
    print("   - *tuple: 将元组/列表解包成位置参数")
    print("   - **dict: 将字典解包成关键字参数")
    print("\n3. 示例对比：")
    print("   # 定义函数")
    print("   def func(*args, **kwargs):")
    print("       print(f'args类型: {type(args)}')  # <class 'tuple'>")
    print("       print(f'kwargs类型: {type(kwargs)}')  # <class 'dict'>")
    print("   ")
    print("   # 调用函数")
    print("   my_tuple = (1, 2, 3)")
    print("   my_dict = {'a': 1, 'b': 2}")
    print("   func(*my_tuple, **my_dict)  # 解包传入")
    
    print()


# 演示模块导入
def demo_module_import():
    """演示模块导入"""
    print("=" * 50)
    print("模块导入演示")
    print("=" * 50)
    
    # 导入标准库模块
    import math
    print(f"math.pi = {math.pi}")
    print(f"math.sqrt(16) = {math.sqrt(16)}")
    
    # 导入特定函数
    from datetime import datetime
    now = datetime.now()
    print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 导入并重命名
    import random as rnd
    print(f"随机数: {rnd.randint(1, 100)}")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_function_basics()
    demo_parameters()
    demo_unpacking()  # 新增：参数解包演示
    demo_lambda()
    demo_builtin_functions()
    demo_module_import()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

