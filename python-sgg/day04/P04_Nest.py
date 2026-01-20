"""
    该案例演示了循环的嵌套
    打印99乘法表
"""
# 外层循环控制打印的行数  一共9行
for i  in range(1,10):
    for j in range(1,i + 1):
        print(f"{j} * {i} = {i*j}",end="\t")
    print()
