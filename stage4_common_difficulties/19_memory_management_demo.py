# -*- coding: utf-8 -*-
"""
第四阶段：内存管理与垃圾回收难点实战演示
演示引用计数机制、循环引用与标记清除、分代回收策略等核心概念
"""

import sys
import gc
import weakref
import time
from typing import List, Dict, Any


def demo_reference_count():
    """演示引用计数机制"""
    print("=" * 60)
    print("引用计数机制演示")
    print("=" * 60)
    
    print("1. 基本引用计数：")
    
    # 创建一个对象并查看引用计数
    obj = object()
    print(f"   对象: {obj}")
    print(f"   初始引用计数: {sys.getrefcount(obj) - 1}")  # 减去getrefcount自身的引用
    
    # 添加引用
    ref1 = obj
    print(f"   添加引用后: {sys.getrefcount(obj) - 1}")
    
    ref2 = ref1
    print(f"   再次添加引用: {sys.getrefcount(obj) - 1}")
    
    # 减少引用
    del ref1
    print(f"   删除一个引用: {sys.getrefcount(obj) - 1}")
    
    ref2 = None
    print(f"   清除另一个引用: {sys.getrefcount(obj) - 1}")
    
    print("\n2. 引用计数与容器：")
    
    # 创建对象
    a = [1, 2, 3]
    b = {'key': 'value'}
    
    print(f"   列表a的引用计数: {sys.getrefcount(a) - 1}")
    print(f"   字典b的引用计数: {sys.getrefcount(b) - 1}")
    
    # 互相引用
    a.append(b)
    b['list_ref'] = a
    
    print(f"   互相引用后列表a计数: {sys.getrefcount(a) - 1}")
    print(f"   互相引用后字典b计数: {sys.getrefcount(b) - 1}")
    
    # 删除引用
    del a
    del b
    print(f"   删除变量后，引用计数为0，对象等待回收")
    
    print("\n3. 弱引用：")
    
    class MyClass:
        def __del__(self):
            print("   MyClass对象被销毁")
    
    # 创建对象
    obj = MyClass()
    print(f"   对象创建后引用计数: {sys.getrefcount(obj) - 1}")
    
    # 创建弱引用
    weak_ref = weakref.ref(obj)
    print(f"   弱引用不会增加计数: {sys.getrefcount(obj) - 1}")
    print(f"   通过弱引用获取对象: {weak_ref()}")
    
    # 删除强引用
    del obj
    print(f"   删除强引用后，弱引用指向: {weak_ref()}")
    
    # 弱引用字典
    print("\n   弱引用字典：")
    weak_dict = weakref.WeakKeyDictionary()
    obj1 = MyClass()
    obj2 = MyClass()
    
    weak_dict[obj1] = "Value 1"
    weak_dict[obj2] = "Value 2"
    
    print(f"   弱引用字典内容: {list(weak_dict.items())}")
    
    del obj1
    print(f"   删除obj1后字典内容: {list(weak_dict.items())}")


def demo_cyclic_references():
    """演示循环引用与标记清除"""
    print("\n" + "=" * 60)
    print("循环引用与标记清除演示")
    print("=" * 60)
    
    # 禁用自动垃圾回收
    gc.disable()
    print("1. 循环引用示例：")
    
    class Node:
        def __init__(self, name):
            self.name = name
            self.next = None
            self.prev = None
        
        def __del__(self):
            print(f"   Node {self.name} 被销毁")
    
    # 创建循环引用
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    
    # 创建双向链表
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    
    # 创建循环
    node3.next = node1
    node1.prev = node3
    
    print(f"   创建循环引用后，节点数量: {gc.get_count()}")
    
    # 删除所有外部引用
    del node1
    del node2
    del node3
    
    print(f"   删除外部引用后，节点数量: {gc.get_count()}")
    print(f"   循环引用导致引用计数不为0")
    
    # 手动进行垃圾回收
    print("\n2. 标记清除算法：")
    print(f"   手动执行垃圾回收前: {gc.get_count()}")
    collected = gc.collect()
    print(f"   手动执行垃圾回收后: {gc.get_count()}")
    print(f"   收集的对象数量: {collected}")
    
    # 启用自动垃圾回收
    gc.enable()
    
    print("\n3. 循环引用中的弱引用解决方案：")
    
    class WeakNode:
        def __init__(self, name):
            self.name = name
            self.next = None
            self.prev = None
        
        def __del__(self):
            print(f"   WeakNode {self.name} 被销毁")
    
    # 创建节点
    w_node1 = WeakNode("W1")
    w_node2 = WeakNode("W2")
    w_node3 = WeakNode("W3")
    
    # 使用弱引用避免循环
    w_node1.next = w_node2
    w_node2.prev = weakref.ref(w_node1)
    w_node2.next = w_node3
    w_node3.prev = weakref.ref(w_node2)
    
    # 不形成循环
    # w_node3.next = None
    
    # 删除外部引用
    del w_node1
    del w_node2
    del w_node3
    
    # 手动回收
    gc.collect()


def demo_generational_collection():
    """演示分代回收策略"""
    print("\n" + "=" * 60)
    print("分代回收策略演示")
    print("=" * 60)
    
    print("1. 分代回收概述：")
    print(f"   分代数量: {gc.get_count()}")
    print(f"   分代阈值: {gc.get_threshold()}")
    
    # 创建大量短期对象
    print("\n2. 短期对象与年轻代：")
    print(f"   初始计数: {gc.get_count()}")
    
    for _ in range(1000):
        obj = object()
        # 不保留引用，对象会被立即回收
    
    print(f"   创建1000个对象后计数: {gc.get_count()}")
    
    # 手动触发回收
    collected = gc.collect()
    print(f"   手动回收后计数: {gc.get_count()}")
    print(f"   收集的对象数量: {collected}")
    
    # 创建一些长期存在的对象
    print("\n3. 长期对象与老年代：")
    long_lived = []
    
    for i in range(1000):
        obj = [i] * 10  # 列表对象
        if i % 100 == 0:
            long_lived.append(obj)  # 保留10%的对象
    
    print(f"   创建长期对象后计数: {gc.get_count()}")
    
    # 多次回收，观察对象如何晋升到老年
    for i in range(3):
        collected = gc.collect()
        print(f"   第{i+1}次回收后计数: {gc.get_count()}")
        print(f"   收集的对象数量: {collected}")
    
    # 检查对象是否还存在
    print(f"   长期对象数量: {len(long_lived)}")
    
    # 清理
    del long_lived
    gc.collect()


def demo_memory_optimization():
    """演示内存优化技巧"""
    print("\n" + "=" * 60)
    print("内存优化技巧演示")
    print("=" * 60)
    
    print("1. 对象大小比较：")
    
    # 计算不同类型对象的大小
    types = [
        (int, 42),
        (float, 3.14),
        (str, "hello"),
        (list, [1, 2, 3]),
        (dict, {'a': 1, 'b': 2}),
        (tuple, (1, 2, 3)),
        (set, {1, 2, 3})
    ]
    
    for type_name, obj in types:
        size = sys.getsizeof(obj)
        print(f"   {type_name.__name__}对象大小: {size} 字节")
    
    print("\n2. 避免不必要的副本：")
    
    # 大列表
    large_list = list(range(1000000))
    print(f"   大列表大小: {sys.getsizeof(large_list)} 字节")
    
    # 切片创建副本
    slice_copy = large_list[:]
    print(f"   切片副本大小: {sys.getsizeof(slice_copy)} 字节")
    
    # 引用不创建副本
    ref = large_list
    print(f"   引用大小: {sys.getsizeof(ref)} 字节")
    
    # 清除
    del large_list, slice_copy, ref
    
    print("\n3. 生成器与内存节省：")
    
    # 列表推导式
    list_comp = [x * x for x in range(1000000)]
    print(f"   列表推导式大小: {sys.getsizeof(list_comp)} 字节")
    
    # 生成器表达式
    gen_exp = (x * x for x in range(1000000))
    print(f"   生成器表达式大小: {sys.getsizeof(gen_exp)} 字节")
    
    # 清除
    del list_comp, gen_exp
    
    print("\n4. 字符串优化：")
    
    # 字符串拼接
    print("   字符串拼接方式比较：")
    
    # 使用+号拼接
    start_time = time.time()
    s = ""
    for i in range(10000):
        s += str(i)
    end_time = time.time()
    print(f"   使用+号拼接时间: {end_time - start_time:.6f} 秒")
    
    # 使用join拼接
    start_time = time.time()
    parts = []
    for i in range(10000):
        parts.append(str(i))
    s = "".join(parts)
    end_time = time.time()
    print(f"   使用join拼接时间: {end_time - start_time:.6f} 秒")


def demo_gc_module():
    """演示gc模块的使用"""
    print("\n" + "=" * 60)
    print("gc模块使用演示")
    print("=" * 60)
    
    print("1. gc模块基本功能：")
    
    # 检查垃圾回收是否启用
    print(f"   垃圾回收启用状态: {gc.isenabled()}")
    
    # 获取回收统计
    print(f"   回收统计: {gc.get_stats()}")
    
    # 创建循环引用
    class Cyclic:
        def __init__(self):
            self.other = None
    
    obj1 = Cyclic()
    obj2 = Cyclic()
    obj1.other = obj2
    obj2.other = obj1
    
    # 删除外部引用
    del obj1, obj2
    
    # 手动回收
    print(f"\n2. 手动垃圾回收：")
    print(f"   回收前垃圾对象数量: {len(gc.garbage)}")
    
    collected = gc.collect()
    print(f"   收集的对象数量: {collected}")
    print(f"   回收后垃圾对象数量: {len(gc.garbage)}")
    
    # 设置调试标志
    print(f"\n3. 调试模式：")
    
    # 注意：调试标志会产生大量输出，这里仅作演示
    # gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE)
    
    # 重置调试标志
    gc.set_debug(0)
    
    # 注册垃圾回收回调
    print(f"\n4. 垃圾回收回调：")
    
    def gc_callback(phase, info):
        if phase == "start":
            print(f"   垃圾回收开始: {info}")
        elif phase == "stop":
            print(f"   垃圾回收结束: {info}")
    
    # 注意：在某些Python版本中可能不可用
    try:
        gc.callbacks.append(gc_callback)
        # 触发垃圾回收
        gc.collect()
        # 移除回调
        gc.callbacks.remove(gc_callback)
    except AttributeError:
        print("   gc.callbacks在当前Python版本中不可用")


def main():
    """主函数"""
    print("=" * 60)
    print("内存管理与垃圾回收难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. 引用计数机制")
    print("2. 循环引用与标记清除")
    print("3. 分代回收策略")
    print("4. 内存优化技巧")
    print("5. gc模块的使用")
    print("=" * 60)
    
    # 运行各个演示
    demo_reference_count()
    demo_cyclic_references()
    demo_generational_collection()
    demo_memory_optimization()
    demo_gc_module()
    
    print("\n" + "=" * 60)
    print("内存管理与垃圾回收难点总结:")
    print("1. 引用计数是主要的内存管理方式，简单高效")
    print("2. 循环引用无法通过引用计数解决，需要标记清除算法")
    print("3. 分代回收策略基于'对象越老越难回收'的假设")
    print("4. 合理使用弱引用可以避免循环引用")
    print("5. 生成器、字符串join等技术可以优化内存使用")
    print("6. gc模块提供了手动控制垃圾回收的功能")
    print("=" * 60)


if __name__ == "__main__":
    main()
