# -*- coding: utf-8 -*-
"""
第一阶段：Python环境配置与基础语法
演示变量、数据类型、运算符和代码规范
"""


def demo_variables_and_types():
    """演示变量与数据类型"""
    print("=" * 50)
    print("变量与数据类型演示")
    print("=" * 50)
    
    # 整数类型
    age = 25
    print(f"整数类型: {age}, 类型: {type(age)}")
    
    # 浮点数类型
    price = 99.99
    print(f"浮点数类型: {price}, 类型: {type(price)}")
    
    # 字符串类型
    name = "Python学习者"
    print(f"字符串类型: {name}, 类型: {type(name)}")
    
    # 布尔类型
    is_student = True
    print(f"布尔类型: {is_student}, 类型: {type(is_student)}")
    
    # None类型
    data = None
    print(f"None类型: {data}, 类型: {type(data)}")
    
    print()


def demo_operators():
    """演示基本运算符与表达式"""
    print("=" * 50)
    print("基本运算符与表达式演示")
    print("=" * 50)
    
    a, b = 10, 3
    
    # 算术运算符
    print(f"加法: {a} + {b} = {a + b}")
    print(f"减法: {a} - {b} = {a - b}")
    print(f"乘法: {a} * {b} = {a * b}")
    print(f"除法: {a} / {b} = {a / b}")
    print(f"整除: {a} // {b} = {a // b}")
    print(f"取余: {a} % {b} = {a % b}")
    print(f"幂运算: {a} ** {b} = {a ** b}")
    
    # 比较运算符
    print(f"\n比较运算符:")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    
    # 逻辑运算符
    print(f"\n逻辑运算符:")
    print(f"True and False: {True and False}")
    print(f"True or False: {True or False}")
    print(f"not True: {not True}")
    
    print()


def demo_code_style():
    """演示代码规范"""
    print("=" * 50)
    print("代码规范演示")
    print("=" * 50)
    
    # PEP 8 命名规范
    # 变量名使用小写字母和下划线
    user_name = "张三"
    user_age = 20
    
    # 常量使用大写字母和下划线
    MAX_SIZE = 100
    MIN_SIZE = 1
    
    # 函数名使用小写字母和下划线
    def calculate_total(price, quantity):
        """计算总价"""
        return price * quantity
    
    print(f"用户名: {user_name}, 年龄: {user_age}")
    print(f"最大尺寸: {MAX_SIZE}, 最小尺寸: {MIN_SIZE}")
    print(f"总价: {calculate_total(10, 5)}")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_variables_and_types()
    demo_operators()
    demo_code_style()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

