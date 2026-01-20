"""
    该案例演示了自定义异常
"""
class MyException(Exception):
    def __init__(self, value):
        self.value = value


try:
    # 可能发生异常的代码
    raise MyException("这是我自己定义的异常")
except MyException as e:
    # 对异常处理的代码
    print(f"发生异常了{e}")