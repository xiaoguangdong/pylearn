# -*- coding: utf-8 -*-
"""
第四阶段：可变与不可变对象难点实战演示
演示列表/元组区别、字典键限制、函数参数传递、深浅拷贝等核心难点
"""

import copy
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
import sys


def demo_basic_differences():
    """演示可变与不可变对象的基本区别"""
    print("=" * 60)
    print("可变与不可变对象基本区别")
    print("=" * 60)
    
    # 不可变对象示例
    print("1. 不可变对象:")
    a = 10
    b = "hello"
    c = (1, 2, 3)
    
    print(f"   整数: id(a) = {id(a)}")
    a += 1
    print(f"   修改后: id(a) = {id(a)} (id已改变!)")
    
    print(f"\n   字符串: id(b) = {id(b)}")
    b += " world"
    print(f"   修改后: id(b) = {id(b)} (id已改变!)")
    
    print(f"\n   元组: id(c) = {id(c)}")
    try:
        c[0] = 99  # 会抛出异常
    except TypeError as e:
        print(f"   修改元组元素会抛出: {type(e).__name__}: {e}")
    
    # 可变对象示例
    print("\n2. 可变对象:")
    d = [1, 2, 3]
    e = {"a": 1}
    f = {1, 2, 3}
    
    print(f"   列表: id(d) = {id(d)}")
    d.append(4)
    print(f"   添加元素后: id(d) = {id(d)} (id未改变!)")
    print(f"   列表内容: {d}")
    
    print(f"\n   字典: id(e) = {id(e)}")
    e["b"] = 2
    print(f"   添加键值对后: id(e) = {id(e)} (id未改变!)")
    print(f"   字典内容: {e}")


def demo_dict_key_limitation():
    """演示字典键的限制（必须为不可变类型）"""
    print("\n" + "=" * 60)
    print("字典键的限制演示")
    print("=" * 60)
    
    # 有效键示例
    print("1. 有效的字典键（不可变类型）:")
    valid_dict = {
        123: "整数键",          # 整数 - 不可变 ✓
        "name": "字符串键",     # 字符串 - 不可变 ✓
        (1, 2, 3): "元组键",    # 元组 - 不可变 ✓
        frozenset([1, 2]): "冻结集合键",  # frozenset - 不可变 ✓
        True: "布尔键",         # 布尔 - 不可变 ✓
        None: "None键",        # None - 不可变 ✓
    }
    
    for key, value in valid_dict.items():
        print(f"   {repr(key)}: {value} (类型: {type(key).__name__})")
    
    # 无效键示例
    print("\n2. 无效的字典键（可变类型）:")
    
    try:
        invalid_dict = {[1, 2]: "列表键"}  # 列表 - 可变 ✗
    except TypeError as e:
        print(f"   列表作为键: {type(e).__name__}: {e}")
    
    try:
        invalid_dict = {{1, 2}: "集合键"}  # 集合 - 可变 ✗
    except TypeError as e:
        print(f"   集合作为键: {type(e).__name__}: {e}")
    
    try:
        invalid_dict = {{"a": 1}: "字典键"}  # 字典 - 可变 ✗
    except TypeError as e:
        print(f"   字典作为键: {type(e).__name__}: {e}")
    
    # 实际应用场景
    print("\n3. 实际应用场景 - 缓存系统:")
    
    def expensive_computation(x: int, y: int, config: dict) -> int:
        """模拟昂贵计算"""
        # 使用元组作为字典键来缓存结果
        key = (x, y, frozenset(config.items()))
        return key
    
    config1 = {"mode": "fast", "precision": "high"}
    config2 = {"precision": "high", "mode": "fast"}  # 相同内容，不同顺序
    
    key1 = expensive_computation(10, 20, config1)
    key2 = expensive_computation(10, 20, config2)
    
    print(f"   config1的键: {key1}")
    print(f"   config2的键: {key2}")
    print(f"   键是否相等: {key1 == key2}")
    print(f"   frozenset确保顺序不影响相等性")


def demo_function_argument_passing():
    """演示函数参数传递中的可变对象陷阱"""
    print("\n" + "=" * 60)
    print("函数参数传递中的可变对象陷阱")
    print("=" * 60)
    
    # 陷阱1：意外修改传入的可变对象
    print("1. 陷阱：意外修改传入的可变对象")
    
    def process_data_wrong(data: List[int]) -> List[int]:
        """错误示例：修改了传入的列表"""
        data.append(99)  # 修改了原始数据！
        return [x * 2 for x in data]
    
    def process_data_correct(data: List[int]) -> List[int]:
        """正确示例：不修改原始数据"""
        data_copy = data.copy()
        data_copy.append(99)
        return [x * 2 for x in data_copy]
    
    original_data = [1, 2, 3]
    print(f"   原始数据: {original_data}")
    
    result_wrong = process_data_wrong(original_data)
    print(f"   错误函数处理后:")
    print(f"     返回值: {result_wrong}")
    print(f"     原始数据: {original_data} (被意外修改!)")
    
    original_data = [1, 2, 3]  # 重置
    result_correct = process_data_correct(original_data)
    print(f"\n   正确函数处理后:")
    print(f"     返回值: {result_correct}")
    print(f"     原始数据: {original_data} (保持原样)")
    
    # 陷阱2：默认参数的可变对象
    print("\n2. 陷阱：默认参数使用可变对象")
    
    def append_to_list_wrong(item, my_list=[]):  # 危险！
        my_list.append(item)
        return my_list
    
    def append_to_list_correct(item, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(item)
        return my_list
    
    print(f"   错误实现:")
    result1 = append_to_list_wrong(1)
    result2 = append_to_list_wrong(2)
    result3 = append_to_list_wrong(3)
    print(f"     第一次调用: {result1}")
    print(f"     第二次调用: {result2} (共享了同一个列表!)")
    print(f"     第三次调用: {result3} (共享了同一个列表!)")
    
    print(f"\n   正确实现:")
    result1 = append_to_list_correct(1)
    result2 = append_to_list_correct(2)
    result3 = append_to_list_correct(3)
    print(f"     第一次调用: {result1}")
    print(f"     第二次调用: {result2}")
    print(f"     第三次调用: {result3}")


def demo_shallow_deep_copy():
    """演示浅拷贝与深拷贝的区别"""
    print("\n" + "=" * 60)
    print("浅拷贝与深拷贝的区别")
    print("=" * 60)
    
    # 创建嵌套数据结构
    original_data = {
        "name": "原始数据",
        "numbers": [1, 2, 3],
        "config": {
            "mode": "fast",
            "settings": [True, False]
        }
    }
    
    print("1. 原始数据结构:")
    print(f"   {original_data}")
    
    # 浅拷贝
    shallow_copy = copy.copy(original_data)
    print(f"\n2. 浅拷贝 (copy.copy()):")
    print(f"   id(original) != id(shallow_copy): {id(original_data) != id(shallow_copy)}")
    print(f"   id(original['numbers']) == id(shallow_copy['numbers']): "
          f"{id(original_data['numbers']) == id(shallow_copy['numbers'])}")
    print(f"   id(original['config']) == id(shallow_copy['config']): "
          f"{id(original_data['config']) == id(shallow_copy['config'])}")
    
    # 修改浅拷贝的嵌套列表
    shallow_copy['numbers'].append(99)
    print(f"\n   修改浅拷贝的列表后:")
    print(f"   浅拷贝: {shallow_copy['numbers']}")
    print(f"   原始数据: {original_data['numbers']} (也被修改了!)")
    
    # 重置数据
    original_data['numbers'] = [1, 2, 3]
    
    # 深拷贝
    deep_copy = copy.deepcopy(original_data)
    print(f"\n3. 深拷贝 (copy.deepcopy()):")
    print(f"   id(original) != id(deep_copy): {id(original_data) != id(deep_copy)}")
    print(f"   id(original['numbers']) != id(deep_copy['numbers']): "
          f"{id(original_data['numbers']) != id(deep_copy['numbers'])}")
    print(f"   id(original['config']) != id(deep_copy['config']): "
          f"{id(original_data['config']) != id(deep_copy['config'])}")
    
    # 修改深拷贝的嵌套列表
    deep_copy['numbers'].append(99)
    print(f"\n   修改深拷贝的列表后:")
    print(f"   深拷贝: {deep_copy['numbers']}")
    print(f"   原始数据: {original_data['numbers']} (未被修改)")
    
    # 不同拷贝方式的性能比较
    print(f"\n4. 不同拷贝方式的比较:")
    
    # 列表切片
    lst = [1, 2, 3, [4, 5]]
    slice_copy = lst[:]  # 相当于浅拷贝
    print(f"   列表切片是浅拷贝: {id(lst[3]) == id(slice_copy[3])}")
    
    # dict.copy()
    dct = {"a": [1, 2], "b": {"c": 3}}
    dict_copy = dct.copy()  # 浅拷贝
    print(f"   dict.copy()是浅拷贝: {id(dct['a']) == id(dict_copy['a'])}")
    
    # list.copy() (Python 3.3+)
    lst_copy = lst.copy()  # 浅拷贝
    print(f"   list.copy()是浅拷贝: {id(lst[3]) == id(lst_copy[3])}")


def demo_practical_scenarios():
    """演示实际应用场景"""
    print("\n" + "=" * 60)
    print("实际应用场景演示")
    print("=" * 60)
    
    # 场景1：配置管理
    print("1. 配置管理（避免意外修改）:")
    
    DEFAULT_CONFIG = {
        "timeout": 30,
        "retries": 3,
        "servers": ["server1", "server2"]
    }
    
    def create_config(user_config: dict = None) -> dict:
        """创建配置，避免修改默认配置"""
        config = copy.deepcopy(DEFAULT_CONFIG)
        if user_config:
            config.update(user_config)
        return config
    
    # 用户配置
    user_config = {"timeout": 60, "servers": ["server3"]}
    
    config1 = create_config(user_config)
    config2 = create_config({"retries": 5})
    
    print(f"   默认配置: {DEFAULT_CONFIG}")
    print(f"   配置1: {config1}")
    print(f"   配置2: {config2}")
    
    # 修改配置1的servers
    config1["servers"].append("server4")
    print(f"\n   修改配置1后:")
    print(f"   配置1: {config1}")
    print(f"   默认配置: {DEFAULT_CONFIG} (未受影响)")
    print(f"   配置2: {config2} (未受影响)")
    
    # 场景2：缓存系统
    print("\n2. 缓存系统（使用不可变键）:")
    
    class ExpensiveOperationCache:
        def __init__(self):
            self._cache = {}
        
        def compute(self, x: int, y: int, options: dict) -> int:
            # 使用不可变键
            key = (x, y, frozenset(options.items()))
            
            if key in self._cache:
                print(f"   缓存命中: {key}")
                return self._cache[key]
            
            # 模拟昂贵计算
            result = x * y + len(options)
            self._cache[key] = result
            
            print(f"   计算并缓存: {key} -> {result}")
            return result
    
    cache = ExpensiveOperationCache()
    
    options1 = {"mode": "fast", "precision": "high"}
    options2 = {"precision": "high", "mode": "fast"}  # 相同内容，不同顺序
    
    print(f"   第一次计算: {cache.compute(10, 20, options1)}")
    print(f"   第二次计算（相同参数）: {cache.compute(10, 20, options1)}")
    print(f"   第三次计算（相同内容，不同顺序）: {cache.compute(10, 20, options2)}")
    
    # 场景3：线程安全的数据传递
    print("\n3. 线程安全的数据传递（使用不可变对象）:")
    
    import threading
    import time
    
    def process_data(data: tuple):  # 使用元组确保不可变
        print(f"   线程 {threading.current_thread().name} 处理: {data}")
        time.sleep(0.1)
        return sum(data)
    
    # 创建线程
    data_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    threads = []
    results = []
    
    for i, data in enumerate(data_tuples):
        thread = threading.Thread(
            target=lambda d=data: results.append(process_data(d)),
            name=f"Worker-{i}"
        )
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"   处理结果: {results}")


def main():
    """主函数"""
    print("=" * 60)
    print("可变与不可变对象难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. 可变与不可变对象的基本区别")
    print("2. 字典键的限制")
    print("3. 函数参数传递陷阱")
    print("4. 浅拷贝与深拷贝")
    print("5. 实际应用场景")
    print("=" * 60)
    
    # 运行各个演示
    demo_basic_differences()
    demo_dict_key_limitation()
    demo_function_argument_passing()
    demo_shallow_deep_copy()
    demo_practical_scenarios()
    
    print("\n" + "=" * 60)
    print("难点总结:")
    print("1. 不可变对象：int, str, tuple, frozenset, bytes")
    print("2. 可变对象：list, dict, set, 自定义对象")
    print("3. 字典键必须是不可变对象")
    print("4. 函数参数传递是引用传递，注意可变对象的修改")
    print("5. 默认参数不要使用可变对象")
    print("6. 浅拷贝只复制一层，深拷贝递归复制")
    print("=" * 60)


if __name__ == "__main__":
    main()