"""
    该案例演示了global和nonlocal关键字
"""
"""
# 通过 += 操作赋值，会报错，认为局部变量还未定义
var1 = 10
def func():
    var1 += 10 ==> var1 = var1 + 10
    print(var1)
func()
"""
"""
var1 = 10
def func():
    var1 = 20
    print(f"局部作用域中的var1={var1}")
func()
print(f"全局作用域中的var1={var1}")
"""
"""
var1 = 10
def func():
    # 声明：当前在局部作用域中使用全局的变量 var1
    global var1
    var1 = 20
    print(f"局部作用域中的var1={var1,id(var1)}")
func()
print(f"全局作用域中的var1={var1,id(var1)}")
"""
"""
list1 = [1,2,3]
def func():
    list1[0] = 100
    # list1 = [3,4,5]
    print(f"局部作用域中的list1={list1, id(list1)}")

func()
print(f"全局作用域中的list1={list1, id(list1)}")
"""

def outer():
    var1 = 10
    def inner():
        nonlocal var1
        var1 = 20
        print(f"局部作用域中的var1={var1, id(var1)}")
    inner()
    print(f"嵌套作用域中的var1={var1, id(var1)}")
outer()


