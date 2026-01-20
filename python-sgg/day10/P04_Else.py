"""
    该案例演示了else
"""
"""
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零！")
else:
    print(f"结果是: {result}")
"""
try:
    result = 10 / 0
    print(f"结果是: {result}")
except ZeroDivisionError:
    print("除数不能为零！")


