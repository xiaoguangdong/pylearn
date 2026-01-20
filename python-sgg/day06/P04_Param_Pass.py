"""
    该案例演示了函数参数的传递
"""
"""
def change_int(a):
    print(f"在函数内部修改值之前的地址:{id(a)}")
    a = 20
    print(f"在函数内部修改值之后的地址:{id(a)}")


b = 10
change_int(b)
print(f"在函数外部修改值之后的地址:{id(b)}")


def change_list(list1):
    print(f"在函数内部修改列表之前的地址:{id(list1)},列表中的元素:{list1}")
    list1[2] = 500
    print(f"在函数内部修改列表之后的地址:{id(list1)},列表中的元素:{list1}")


my_list = [1, 2, 3, 4, 5]

print(f"在函数外部修改列表之前的地址:{id(my_list)},列表中的元素:{my_list}")
change_list(my_list)
print(f"在函数外部修改列表之后的地址:{id(my_list)},列表中的元素:{my_list}")
"""
def multi(m_list):
    print("函数内m_list id:", id(m_list))
    # m_list *= 3
    m_list = m_list * 3
    print("函数内扩充后m_list id:", id(m_list))

list1 = [1,2,3]
print("list1 id:", id(list1))
multi(list1)