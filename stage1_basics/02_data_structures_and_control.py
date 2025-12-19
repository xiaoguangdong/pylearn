# -*- coding: utf-8 -*-
"""
第一阶段：数据结构与流程控制
演示列表、元组、字典、集合以及条件语句和循环
"""


def demo_lists_and_tuples():
    """演示列表和元组"""
    print("=" * 50)
    print("列表和元组演示")
    print("=" * 50)
    
    # 列表（可变）
    fruits = [["苹果", "香蕉", "橙子"], ["草莓", "葡萄", "蓝莓"]]
    print(f"列表: {fruits}")
    fruits.append(["西瓜", "桃子", "梨子"])  # 添加元素
    print(f"添加元素后: {fruits}")
    fruits[0] = ["草莓","橘子","柚子"]  # 修改元素
    print(f"修改元素后: {fruits}")
    
    # 元组（不可变）
    coordinates = (10, 20)
    print(f"\n元组: {coordinates}")
    print(f"元组中的第一个元素: {coordinates[0]}")
    # coordinates[0] = 30  # 这会报错，元组不可变
    
    # 列表切片
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\n列表切片:")
    print(f"前三个: {numbers[:3]}")
    print(f"后三个: {numbers[-3:]}")
    print(f"中间部分: {numbers[2:7]}")
    
    print()


def demo_dictionaries_and_sets():
    """演示字典和集合"""
    print("=" * 50)
    print("字典和集合演示")
    print("=" * 50)
    
    # 字典（键值对）
    student = {
        "姓名": "李四",
        "年龄": 22,
        "专业": "计算机科学"
    }
    print(f"字典: {student}")
    print(f"姓名: {student['姓名']}")
    student["成绩"] = 95  # 添加新键值对
    print(f"添加成绩后: {student}")
    
    # 集合（无序、不重复）
    unique_numbers = {1, 2, 3, 4, 5, 3, 2}  # 重复元素会被自动去除
    print(f"\n集合: {unique_numbers}")
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(f"集合1: {set1}")
    print(f"集合2: {set2}")
    print(f"交集: {set1 & set2}")
    print(f"并集: {set1 | set2}")
    print(f"差集: {set1 - set2}")
    
    print()


def demo_conditionals():
    """演示条件语句"""
    print("=" * 50)
    print("条件语句演示")
    print("=" * 50)
    
    score = 85
    
    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    
    print(f"分数: {score}, 等级: {grade}")
    
    # 三元表达式
    result = "通过" if score >= 60 else "不通过"
    print(f"结果: {result}")
    
    print()


def demo_loops():
    """演示循环"""
    print("=" * 50)
    print("循环演示")
    print("=" * 50)
    
    # for循环
    print("for循环遍历列表:")
    colors = ["红色", "绿色", "蓝色"]
    for color in colors:
        print(f"  - {color}")
    
    # for循环遍历字典
    print("\nfor循环遍历字典:")
    person = {"姓名": "王五", "年龄": 25, "城市": "北京"}
    for key, value in person.items():
        print(f"  {key}: {value}")
    
    # while循环
    print("\nwhile循环:")
    count = 0
    while count < 5:
        print(f"  计数: {count}")
        count += 1
    
    # break和continue
    print("\nbreak和continue演示:")
    for i in range(10):
        if i == 3:
            continue  # 跳过3
        if i == 7:
            break  # 在7处停止
        print(f"  {i}")
    
    print()


def demo_comprehensions():
    """演示列表推导式和字典推导式"""
    print("=" * 50)
    print("列表推导式和字典推导式演示")
    print("=" * 50)
    
    # 列表推导式
    squares = [x ** 2 for x in range(1, 6)]
    print(f"平方数列表: {squares}")
    
    # 带条件的列表推导式
    even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
    print(f"偶数的平方: {even_squares}")
    
    # 字典推导式
    square_dict = {x: x ** 2 for x in range(1, 6)}
    print(f"平方数字典: {square_dict}")
    
    # 集合推导式
    unique_lengths = {len(word) for word in ["hello", "world", "python", "code"]}
    print(f"单词长度集合: {unique_lengths}")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_lists_and_tuples()
    demo_dictionaries_and_sets()
    demo_conditionals()
    demo_loops()
    demo_comprehensions()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

