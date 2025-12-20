# -*- coding: utf-8 -*-
"""
第四阶段：生成器与迭代器难点实战演示
演示yield关键字、生成器表达式、迭代器协议等核心概念
"""

from typing import Iterator, Generator, Iterable, List
import sys
import time


def demo_iterator_protocol():
    """演示迭代器协议"""
    print("=" * 60)
    print("迭代器协议演示")
    print("=" * 60)
    
    # 1. 可迭代对象与迭代器的区别
    print("1. 可迭代对象与迭代器的区别:")
    
    # 列表是可迭代对象
    numbers = [1, 2, 3, 4, 5]
    print(f"   列表 numbers: {numbers}")
    print(f"   是否是可迭代对象: {hasattr(numbers, '__iter__')}")
    print(f"   是否是迭代器: {hasattr(numbers, '__next__')}")
    
    # 创建迭代器
    numbers_iter = iter(numbers)
    print(f"   创建迭代器 numbers_iter")
    print(f"   是否是可迭代对象: {hasattr(numbers_iter, '__iter__')}")
    print(f"   是否是迭代器: {hasattr(numbers_iter, '__next__')}")
    
    # 使用next()获取元素
    print(f"\n2. 使用next()获取元素:")
    print(f"   第一次 next(): {next(numbers_iter)}")
    print(f"   第二次 next(): {next(numbers_iter)}")
    print(f"   第三次 next(): {next(numbers_iter)}")
    
    # 迭代完所有元素
    print(f"\n3. 迭代完所有元素:")
    numbers_iter = iter(numbers)
    for num in numbers_iter:
        print(f"   {num}")
    
    # 迭代器耗尽
    print(f"\n4. 迭代器耗尽后的行为:")
    try:
        next(numbers_iter)
    except StopIteration:
        print(f"   抛出 StopIteration 异常")


def demo_custom_iterator():
    """演示自定义迭代器"""
    print("\n" + "=" * 60)
    print("自定义迭代器演示")
    print("=" * 60)
    
    class MyRange:
        """模拟range()函数的自定义迭代器"""
        
        def __init__(self, start: int, end: int, step: int = 1):
            """初始化"""
            self.start = start
            self.end = end
            self.step = step
            self.current = start
        
        def __iter__(self):
            """返回迭代器对象（self）"""
            return self
        
        def __next__(self):
            """返回下一个元素，没有元素时抛出StopIteration"""
            if (self.step > 0 and self.current >= self.end) or \
               (self.step < 0 and self.current <= self.end):
                raise StopIteration
            
            value = self.current
            self.current += self.step
            return value
    
    # 使用自定义迭代器
    print("1. 使用自定义MyRange迭代器:")
    print(f"   range(0, 10, 2): {list(range(0, 10, 2))}")
    print(f"   MyRange(0, 10, 2): {list(MyRange(0, 10, 2))}")
    
    # 反向迭代
    print(f"   MyRange(10, 0, -2): {list(MyRange(10, 0, -2))}")
    
    # 手动迭代
    print(f"\n2. 手动迭代MyRange:")
    my_range = MyRange(0, 5)
    my_iter = iter(my_range)
    
    while True:
        try:
            value = next(my_iter)
            print(f"   {value}")
        except StopIteration:
            break


def demo_generator_basics():
    """演示生成器基础"""
    print("\n" + "=" * 60)
    print("生成器基础演示")
    print("=" * 60)
    
    # 1. 生成器函数
    print("1. 生成器函数:")
    
    def my_generator(n: int) -> Generator[int, None, None]:
        """简单的生成器函数"""
        print(f"   开始生成 0 到 {n-1}")
        for i in range(n):
            print(f"   yield {i}")
            yield i
        print(f"   生成完成")
    
    # 创建生成器
    gen = my_generator(3)
    print(f"   生成器: {gen}")
    print(f"   是否是迭代器: {hasattr(gen, '__next__')}")
    
    # 迭代生成器
    print(f"\n2. 迭代生成器:")
    for i in gen:
        print(f"   获取到: {i}")
    
    # 2. 生成器表达式
    print("\n3. 生成器表达式:")
    
    # 列表推导式
    list_comp = [x * x for x in range(5)]
    print(f"   列表推导式: {list_comp}, 类型: {type(list_comp)}")
    
    # 生成器表达式
    gen_exp = (x * x for x in range(5))
    print(f"   生成器表达式: {gen_exp}, 类型: {type(gen_exp)}")
    print(f"   转换为列表: {list(gen_exp)}")
    
    # 3. yield关键字的特性
    print("\n4. yield关键字的特性:")
    
    def generator_with_pauses(n: int) -> Generator[int, None, None]:
        """演示yield的暂停特性"""
        for i in range(n):
            print(f"   生成器暂停: {i}")
            value = yield i
            print(f"   生成器恢复，收到值: {value}")
    
    gen = generator_with_pauses(3)
    print(f"   第一次 next(): {next(gen)}")
    print(f"   send(None): {gen.send(None)}")
    print(f"   send('hello'): {gen.send('hello')}")


def demo_generator_advanced():
    """演示生成器高级特性"""
    print("\n" + "=" * 60)
    print("生成器高级特性演示")
    print("=" * 60)
    
    # 1. 生成器的关闭
    print("1. 生成器的关闭:")
    
    def infinite_generator() -> Generator[int, None, None]:
        """无限生成器"""
        i = 0
        while True:
            try:
                yield i
                i += 1
            except GeneratorExit:
                print(f"   生成器被关闭")
                raise
    
    gen = infinite_generator()
    print(f"   next(): {next(gen)}")
    print(f"   next(): {next(gen)}")
    gen.close()
    
    # 2. 生成器异常处理
    print("\n2. 生成器异常处理:")
    
    def generator_with_error() -> Generator[int, None, None]:
        """演示生成器中的异常"""
        yield 1
        yield 2
        raise ValueError("生成器内部错误")
        yield 3
    
    gen = generator_with_error()
    try:
        print(f"   next(): {next(gen)}")
        print(f"   next(): {next(gen)}")
        print(f"   next(): {next(gen)}")
    except ValueError as e:
        print(f"   捕获到异常: {e}")
    
    # 3. 生成器的委托（yield from）
    print("\n3. 生成器的委托 (yield from):")
    
    def generator1() -> Generator[int, None, None]:
        """第一个生成器"""
        yield 1
        yield 2
    
    def generator2() -> Generator[int, None, None]:
        """第二个生成器"""
        yield 3
        yield 4
    
    def combined_generator() -> Generator[int, None, None]:
        """组合两个生成器"""
        yield from generator1()
        yield from generator2()
    
    print(f"   组合生成器的结果: {list(combined_generator())}")


def demo_practical_scenarios():
    """演示实际应用场景"""
    print("\n" + "=" * 60)
    print("实际应用场景演示")
    print("=" * 60)
    
    # 场景1：内存高效的数据处理
    print("1. 内存高效的数据处理:")
    
    def process_large_file(file_path: str, chunk_size: int = 1000) -> Generator[List[str], None, None]:
        """处理大文件，按块读取"""
        with open(file_path, 'r', encoding='utf-8') as f:
            while True:
                chunk = []
                for _ in range(chunk_size):
                    line = f.readline()
                    if not line:
                        break
                    chunk.append(line.strip())
                if not chunk:
                    break
                yield chunk
    
    # 模拟大文件
    print(f"   模拟读取大文件，每次读取2行")
    
    # 场景2：无限序列生成
    print("\n2. 无限序列生成:")
    
    def fibonacci() -> Generator[int, None, None]:
        """生成斐波那契序列"""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    fib = fibonacci()
    print(f"   斐波那契数列前10项: {[next(fib) for _ in range(10)]}")
    
    # 场景3：管道式数据处理
    print("\n3. 管道式数据处理:")
    
    def source() -> Generator[int, None, None]:
        """数据源"""
        for i in range(10):
            yield i
    
    def filter_even(numbers: Generator[int, None, None]) -> Generator[int, None, None]:
        """过滤偶数"""
        for num in numbers:
            if num % 2 == 0:
                yield num
    
    def multiply_by_2(numbers: Generator[int, None, None]) -> Generator[int, None, None]:
        """乘以2"""
        for num in numbers:
            yield num * 2
    
    # 数据管道
    pipeline = multiply_by_2(filter_even(source()))
    print(f"   管道处理结果: {list(pipeline)}")
    
    # 场景4：协程通信
    print("\n4. 协程通信:")
    
    def consumer() -> Generator[str, str, None]:
        """消费者协程"""
        while True:
            data = yield
            if data is None:
                break
            print(f"   消费者收到: {data}")
    
    def producer(c: Generator[str, str, None], items: List[str]) -> None:
        """生产者"""
        next(c)  # 启动协程
        try:
            for item in items:
                c.send(item)
            c.send(None)  # 关闭协程
        except StopIteration:
            pass  # 协程正常结束，忽略StopIteration异常
    
    items = ["item1", "item2", "item3"]
    c = consumer()
    producer(c, items)


def demo_memory_efficiency():
    """演示生成器的内存效率"""
    print("\n" + "=" * 60)
    print("内存效率演示")
    print("=" * 60)
    
    # 计算内存占用
    def get_memory_usage(obj) -> int:
        """获取对象的内存占用"""
        return sys.getsizeof(obj)
    
    # 比较列表和生成器的内存占用
    print("1. 比较列表和生成器的内存占用:")
    
    # 列表
    large_list = [x for x in range(1000000)]
    print(f"   列表（1,000,000个元素）: {get_memory_usage(large_list):,} 字节")
    
    # 生成器
    large_gen = (x for x in range(1000000))
    print(f"   生成器（1,000,000个元素）: {get_memory_usage(large_gen):,} 字节")
    print(f"   内存占用比例: {get_memory_usage(large_gen) / get_memory_usage(large_list):.6f}%")
    
    # 2. 比较处理大数据的时间
    print("\n2. 比较处理大数据的时间:")
    
    def time_operation(operation, name: str) -> None:
        """计时操作"""
        start = time.time()
        result = operation()
        end = time.time()
        print(f"   {name}: {end - start:.6f} 秒")
    
    # 列表处理
    def list_processing() -> int:
        """使用列表处理数据"""
        return sum([x * x for x in range(1000000)])
    
    # 生成器处理
    def generator_processing() -> int:
        """使用生成器处理数据"""
        return sum((x * x for x in range(1000000)))
    
    time_operation(list_processing, "列表推导式")
    time_operation(generator_processing, "生成器表达式")


def main():
    """主函数"""
    print("=" * 60)
    print("生成器与迭代器难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. 迭代器协议")
    print("2. 自定义迭代器")
    print("3. 生成器基础")
    print("4. 生成器高级特性")
    print("5. 实际应用场景")
    print("6. 内存效率比较")
    print("=" * 60)
    
    # 运行各个演示
    demo_iterator_protocol()
    demo_custom_iterator()
    demo_generator_basics()
    demo_generator_advanced()
    demo_practical_scenarios()
    demo_memory_efficiency()
    
    print("\n" + "=" * 60)
    print("难点总结:")
    print("1. 迭代器协议: __iter__() 返回迭代器，__next__() 返回下一个元素")
    print("2. 生成器是特殊的迭代器，使用yield关键字")
    print("3. 生成器表达式比列表推导式更节省内存")
    print("4. yield from 可以委托迭代到另一个生成器")
    print("5. 生成器适用于处理大数据、无限序列和管道式数据处理")
    print("=" * 60)


if __name__ == "__main__":
    main()