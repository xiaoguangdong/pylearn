"""
    该案例演示了断言机制
"""
def int_add(x, y):
    # if not (isinstance(x, int) and isinstance(y, int)):
    #     raise 异常类型
    assert isinstance(x, int) and isinstance(y, int), "参数类型错误"
    return x + y

# print(int_add(1, 2))  # 3
print(int_add("1", "2"))  # AssertionError: 参数类型错误
