"""
    该案例演示了生成器
"""
"""
#创建生成器对象--- 使用元组推导式
generator = (x for x in range(5))  # 创建生成器
print(generator)  # <generator object <genexpr> at 0x0000026C2066CB80>
for x in generator:
    print(x)
"""
"""
#创建生成器对象--- 使用函数创建
def fibo():
    a , b = 0,1
    while True:
        yield b
        a, b = b, a+b

f = fibo()
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
"""
"""
#创建生成器对象--- 使用函数创建  获取函数返回值
def fibo():
    a , b ,counter = 0 , 1 , 0
    while counter < 10:
        yield b
        a, b ,counter = b, a+b ,counter + 1
    return "done"

f = fibo()
try:
    while True:
        print(next(f))
except StopIteration as e:
    print(e)
"""

# 向生成器发送数值，作为yield表达式的结果
# 案例 : 通过send()发送一个任务id，使生成器交替执行两个任务
def gen():
    task_id = 0
    int_value = 0
    char_value = "A"
    while True:
        match task_id:
            case 0:
                #生成数字序列
                task_id = yield int_value
                int_value += 1
            case 1:
                # 生成字符序列
                task_id = yield char_value
                char_value = chr(ord(char_value) + 1)
            case _:
                yield  # 返回None

f = gen()
# print(next(f))
# print(f.send(1))
# print(f.send(1))
# print(f.send(0))
# print(f.send(0))
# print(f.send(1))
# print(f.send(1))
print(f.send(None))
print(f.send(1))
print(f.send(1))
