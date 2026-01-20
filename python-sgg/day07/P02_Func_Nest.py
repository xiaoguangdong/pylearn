"""
    该案例演示了函数的嵌套
"""
def func_a():
    print('func_a执行前')
    print('func_a执行中')
    print('func_a执行后')

def func_b():
    print('func_b执行前')
    func_a()
    print('func_b执行后')

func_b()
