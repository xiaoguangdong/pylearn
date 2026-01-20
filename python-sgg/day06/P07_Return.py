
"""
    该案例演示了函数的返回值
"""
"""
def func():
    pass
    return

def func2():
    for i in range(100):
        if i==5:
            # continue
            # break
            return
        print(i)
    print("for循环结束了")

print("函数调用前")
func2()
print("函数调用后")
"""
"""
def sum(num1, num2):
    res = num1 + num2
    # return res
    return

result = sum(1, 2)
print(result)
"""
def func(a,b,c):
    print(a,b,c)
    return a,b,c,[a,b,c]

res = func(1,2,3)
print(res)
print(type(res))
