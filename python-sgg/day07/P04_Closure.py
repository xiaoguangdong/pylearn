"""
    该案例演示了闭包
    需求：如何让A函数中定义的变量能够被B函数访问到
"""
"""
方式1：通过函数的嵌套调用，将A中的变量作为参数传递给B
def func_a():
    num = 10
    func_b(num)

def func_b(num):
    print(num)
"""
# 方式2
def func_a():
    num1 = 10
    def func_b():
        print(num1)
    return func_b

fb = func_a()
objs = fb.__closure__
print(objs)
for cell in objs:
    print(cell.cell_contents)
# fb()