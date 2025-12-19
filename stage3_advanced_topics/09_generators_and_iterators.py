# -*- coding: utf-8 -*-
"""
第三阶段：生成器与迭代器
演示迭代器协议、生成器函数和生成器表达式
"""


def demo_iterator_protocol():
    """演示迭代器协议"""
    print("=" * 50)
    print("迭代器协议演示")
    print("=" * 50)
    
    # 自定义迭代器类
    class NumberRange:
        """数字范围迭代器"""
        
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.current = start
        
        def __iter__(self):
            """返回迭代器对象"""
            return self
        
        def __next__(self):
            """返回下一个值"""
            if self.current >= self.end:
                raise StopIteration
            value = self.current
            self.current += 1
            return value
    
    # 使用自定义迭代器
    print("自定义迭代器:")
    num_range = NumberRange(1, 5)
    for num in num_range:
        print(f"  {num}")
    
    print()
    
    # 使用iter()和next()
    print("使用iter()和next():")
    num_range2 = NumberRange(5, 8)
    iterator = iter(num_range2)
    print(f"  next(iterator): {next(iterator)}")
    print(f"  next(iterator): {next(iterator)}")
    print(f"  next(iterator): {next(iterator)}")
    
    print()
    
    # 内置可迭代对象
    print("内置可迭代对象:")
    my_list = [1, 2, 3]
    my_dict = {"a": 1, "b": 2, "c": 3}
    
    list_iter = iter(my_list)
    print(f"  列表迭代器: {list(list_iter)}")
    
    dict_iter = iter(my_dict)
    print(f"  字典键迭代器: {list(dict_iter)}")
    
    print()


def demo_generator_function():
    """演示生成器函数（yield）"""
    print("=" * 50)
    print("生成器函数演示")
    print("=" * 50)
    
    # 简单的生成器函数
    def countdown(n):
        """倒计时生成器"""
        print(f"  开始倒计时从 {n}")
        while n > 0:
            yield n
            n -= 1
        print("  倒计时结束！")
    
    print("倒计时生成器:")
    for num in countdown(5):
        print(f"  {num}")
    
    print()
    
    # 斐波那契数列生成器
    def fibonacci_generator(n):
        """斐波那契数列生成器"""
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    
    print("斐波那契数列生成器:")
    fib_gen = fibonacci_generator(10)
    for num in fib_gen:
        print(f"  {num}", end=" ")
    print("\n")
    
    # 无限生成器
    def infinite_counter():
        """无限计数器"""
        count = 0
        while True:
            yield count
            count += 1
    
    print("无限生成器（取前5个）:")
    counter = infinite_counter()
    for i in range(5):
        print(f"  {next(counter)}")
    
    print()
    
    # 生成器表达式 vs 列表推导式
    print("生成器表达式 vs 列表推导式:")
    # 列表推导式（立即计算）
    squares_list = [x**2 for x in range(5)]
    print(f"  列表推导式: {squares_list}, 类型: {type(squares_list)}")
    
    # 生成器表达式（惰性计算）
    squares_gen = (x**2 for x in range(5))
    print(f"  生成器表达式: {squares_gen}, 类型: {type(squares_gen)}")
    print(f"  生成器值: {list(squares_gen)}")
    
    print()


def demo_generator_advanced():
    """演示生成器高级用法"""
    print("=" * 50)
    print("生成器高级用法演示")
    print("=" * 50)
    
    # 使用send()向生成器发送值
    def echo_generator():
        """回显生成器"""
        while True:
            value = yield
            print(f"  收到值: {value}")
            yield value * 2
    
    print("使用send()向生成器发送值:")
    gen = echo_generator()
    next(gen)  # 启动生成器
    result = gen.send(10)
    print(f"  结果: {result}\n")
    
    # 使用yield from（委托生成器）
    def number_generator(start, end):
        """数字生成器"""
        for i in range(start, end):
            yield i
    
    def multi_range_generator():
        """多范围生成器"""
        yield from number_generator(1, 4)
        yield from number_generator(10, 13)
        yield from number_generator(20, 23)
    
    print("使用yield from:")
    for num in multi_range_generator():
        print(f"  {num}")
    
    print()
    
    # 生成器用于读取大文件
    def read_large_file(filename):
        """逐行读取大文件"""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    yield line.strip()
        except FileNotFoundError:
            print(f"  文件 {filename} 不存在")
    
    # 创建测试文件
    test_file = "large_file_demo.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        for i in range(5):
            f.write(f"这是第 {i+1} 行\n")
    
    print("逐行读取文件:")
    for line in read_large_file(test_file):
        print(f"  {line}")
    
    # 清理
    import os
    os.remove(test_file)
    
    print()


def demo_generator_expressions():
    """演示生成器表达式"""
    print("=" * 50)
    print("生成器表达式演示")
    print("=" * 50)
    
    # 基本生成器表达式
    gen1 = (x * 2 for x in range(5))
    print(f"基本生成器表达式: {list(gen1)}")
    
    # 带条件的生成器表达式
    gen2 = (x**2 for x in range(10) if x % 2 == 0)
    print(f"偶数的平方: {list(gen2)}")
    
    # 嵌套生成器表达式
    gen3 = ((x, y) for x in range(3) for y in range(3))
    print(f"嵌套生成器表达式: {list(gen3)}")
    
    # 生成器表达式的优势（内存效率）
    print("\n内存效率对比:")
    print("  列表推导式会立即创建所有元素，占用内存")
    print("  生成器表达式按需生成，节省内存")
    
    # 示例：处理大量数据
    large_list = list(range(1000000))  # 100万个元素
    large_gen = (x * 2 for x in range(1000000))  # 生成器，不占用内存
    
    print(f"  列表大小（前10个）: {large_list[:10]}")
    print(f"  生成器（前10个）: {[next(large_gen) for _ in range(10)]}")
    
    print()


def demo_practical_examples():
    """演示实际应用示例"""
    print("=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    # 1. 数据管道处理
    def data_pipeline(data):
        """数据处理管道"""
        # 过滤
        filtered = (x for x in data if x > 0)
        # 转换
        transformed = (x * 2 for x in filtered)
        # 聚合
        return sum(transformed)
    
    data = [-2, -1, 0, 1, 2, 3, 4, 5]
    result = data_pipeline(data)
    print(f"数据处理管道结果: {result}")
    
    # 2. 无限序列生成
    def prime_generator():
        """质数生成器"""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        num = 2
        while True:
            if is_prime(num):
                yield num
            num += 1
    
    print("\n前10个质数:")
    prime_gen = prime_generator()
    primes = [next(prime_gen) for _ in range(10)]
    print(f"  {primes}")
    
    # 3. 分块处理
    def chunk_generator(data, chunk_size):
        """分块生成器"""
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]
    
    print("\n分块处理:")
    data_list = list(range(10))
    for chunk in chunk_generator(data_list, 3):
        print(f"  块: {chunk}")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_iterator_protocol()
    demo_generator_function()
    demo_generator_advanced()
    demo_generator_expressions()
    demo_practical_examples()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

