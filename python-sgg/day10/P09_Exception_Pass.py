"""
    该案例演示了异常的传递
"""
"""
try:
    try:
        try:
            print(1 / 0)
        except NameError as e:
            print("第三层", e)
    except TypeError as e:
        print("第二层", e)
except Exception as e:
    print("第一层", type(e), e)
"""

def m1():
    m2()

def m2():
    m3()

def m3():
    print(1/0)

m1()