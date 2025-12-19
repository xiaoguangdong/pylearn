# -*- coding: utf-8 -*-
"""
第二阶段：异常处理与调试
演示try-except-finally、自定义异常和调试技巧
"""


def demo_basic_exception():
    """演示基本的异常处理"""
    print("=" * 50)
    print("基本异常处理演示")
    print("=" * 50)
    
    # try-except
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("捕获到除零错误")
    
    # 捕获多个异常
    try:
        value = int("abc")
        result = 10 / value
    except ValueError:
        print("捕获到值错误：无法将字符串转换为整数")
    except ZeroDivisionError:
        print("捕获到除零错误")
    
    # 捕获所有异常
    try:
        undefined_variable
    except Exception as e:
        print(f"捕获到异常: {type(e).__name__}: {e}")
    
    print()


def demo_exception_else_finally():
    """演示try-except-else-finally"""
    print("=" * 50)
    print("try-except-else-finally演示")
    print("=" * 50)
    
    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("  错误：除数不能为零")
            return None
        else:
            print(f"  计算成功：{a} / {b} = {result}")
            return result
        finally:
            print("  无论是否发生异常，finally块都会执行")
    
    print("正常情况:")
    divide(10, 2)
    
    print("\n异常情况:")
    divide(10, 0)
    
    print()


def demo_custom_exception():
    """演示自定义异常"""
    print("=" * 50)
    print("自定义异常演示")
    print("=" * 50)
    
    # 自定义异常类
    class InsufficientFundsError(Exception):
        """余额不足异常"""
        
        def __init__(self, balance, amount):
            self.balance = balance
            self.amount = amount
            self.message = f"余额不足！当前余额：{balance}，需要：{amount}"
            super().__init__(self.message)
    
    class InvalidAmountError(Exception):
        """无效金额异常"""
        
        def __init__(self, amount):
            self.amount = amount
            self.message = f"无效金额：{amount}，金额必须大于0"
            super().__init__(self.message)
    
    # 使用自定义异常
    class BankAccount:
        def __init__(self, balance=0):
            self.balance = balance
        
        def withdraw(self, amount):
            if amount <= 0:
                raise InvalidAmountError(amount)
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            return self.balance
    
    account = BankAccount(100)
    
    # 正常取款
    try:
        new_balance = account.withdraw(50)
        print(f"取款成功，余额：{new_balance}")
    except (InsufficientFundsError, InvalidAmountError) as e:
        print(f"取款失败：{e}")
    
    # 余额不足
    try:
        account.withdraw(100)
    except InsufficientFundsError as e:
        print(f"取款失败：{e}")
    
    # 无效金额
    try:
        account.withdraw(-10)
    except InvalidAmountError as e:
        print(f"取款失败：{e}")
    
    print()


def demo_debugging_techniques():
    """演示调试技巧"""
    print("=" * 50)
    print("调试技巧演示")
    print("=" * 50)
    
    # 1. print调试
    def calculate_total(prices):
        total = 0
        print(f"调试：开始计算，prices = {prices}")
        for i, price in enumerate(prices):
            print(f"调试：处理第{i+1}个价格 {price}")
            total += price
            print(f"调试：当前总计 = {total}")
        print(f"调试：最终总计 = {total}")
        return total
    
    result = calculate_total([10, 20, 30])
    print(f"结果：{result}\n")
    
    # 2. 使用断言
    def divide(a, b):
        assert b != 0, "除数不能为零"
        return a / b
    
    try:
        result = divide(10, 2)
        print(f"断言通过，结果：{result}")
        # divide(10, 0)  # 这会触发断言错误
    except AssertionError as e:
        print(f"断言失败：{e}")
    
    print()
    
    # 3. pdb调试（演示，实际使用时需要设置断点）
    print("pdb调试提示：")
    print("  在代码中添加: import pdb; pdb.set_trace()")
    print("  或者使用: breakpoint() (Python 3.7+)")
    print("  常用命令:")
    print("    n - 下一行")
    print("    s - 进入函数")
    print("    c - 继续执行")
    print("    p 变量名 - 打印变量")
    print("    l - 显示代码")
    print("    q - 退出")
    
    # 示例：使用breakpoint（注释掉，避免实际中断）
    # def example_function(x, y):
    #     breakpoint()  # 设置断点
    #     result = x + y
    #     return result
    
    print()


def demo_exception_chaining():
    """演示异常链"""
    print("=" * 50)
    print("异常链演示")
    print("=" * 50)
    
    def process_data(data):
        try:
            return int(data)
        except ValueError as e:
            raise TypeError(f"无法处理数据: {data}") from e
    
    try:
        result = process_data("abc")
    except TypeError as e:
        print(f"捕获到类型错误: {e}")
        print(f"原始异常: {e.__cause__}")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_basic_exception()
    demo_exception_else_finally()
    demo_custom_exception()
    demo_debugging_techniques()
    demo_exception_chaining()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

