"""
    该案例演示了作用域
    主要有4中作用域
        局部 Local -> 嵌套 (Enclosing) ->全局 Global ->内建 Built-in
        LEGB
"""
a = 100
def outer():
    b = 200
    def inner():
        c = 300
        print("先从局部作用域查找:",c)
        print("再从嵌套作用域查找:",b)
        print("再从全局作用域查找:",a)
        print("最后从内建作用域查找:",len([1,2,3]))
    return inner

f = outer()
f()