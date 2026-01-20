"""
    该案例演示了闭包
"""
def Outer(a,b):
    def inner(x):
        return a * x +b
    return inner

inn = Outer(1,2)
# print(inn(2))
for cell in inn.__closure__:
    print(cell.cell_contents)