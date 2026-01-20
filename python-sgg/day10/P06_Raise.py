"""
    该案例演示了raise抛出异常
"""
def add(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x + y
    else:
        # 抛出异常
        raise TypeError("参数类型错误")


try:
    # 可能发生异常的代码
    print(add(1, 2.0))
except:
    # 对异常处理的代码
    print("发生异常了")

print("end")