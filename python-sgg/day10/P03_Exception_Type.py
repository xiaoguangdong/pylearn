"""
    该案例演示了异常类型
"""
try:
    result = 3 / 0
    print("发生异常了")
except NameError as e:
    print(e)
except (RuntimeError, TypeError) as e:
    print(e)
except:
    print("Unexpected error")
print("End")
