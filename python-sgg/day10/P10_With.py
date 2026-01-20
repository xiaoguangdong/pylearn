"""
    该案例演示了with关键字
"""
"""
try:
    file = open("test.txt", "w")
    file.write(a)
    file.close()
finally:
    print("文件是否关闭：", file.closed)  # 文件是否关闭： False
"""
"""
try:
    file = open("test.txt", "w")
    try:
        file.write(a)
    finally:
        file.close()
finally:
    print("文件是否关闭：", file.closed)  # 文件是否关闭： True
"""
# print(open("test.txt", "w"))
try:
    with open("test.txt", "w") as file:
        file.write(a)
finally:
    print("文件是否关闭：", file.closed)  # 文件是否关闭： True
