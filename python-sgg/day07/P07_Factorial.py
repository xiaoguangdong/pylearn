"""
    该案例演示了函数的递归
    案例：求一个整数n的阶乘
    5! = 5 * 4 * 3 * 2 * 1
"""
"""
# 不用递归
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(5))
"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))