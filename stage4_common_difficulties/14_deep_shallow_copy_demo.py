# -*- coding: utf-8 -*-
"""
第四阶段：深浅拷贝难点实战演示
演示浅拷贝、深拷贝的区别与应用场景
"""

import copy
from typing import Dict, List, Any
import sys
import time


def demo_basic_copy():
    """演示基本的拷贝概念"""
    print("=" * 60)
    print("深浅拷贝基本概念演示")
    print("=" * 60)
    
    # 1. 赋值（非拷贝）
    print("1. 赋值操作（非拷贝）:")
    original = [1, 2, 3]
    alias = original
    
    print(f"   原始列表: {original}, id: {id(original)}")
    print(f"   别名列表: {alias}, id: {id(alias)}")
    print(f"   是同一个对象: {original is alias}")
    
    # 修改别名
    alias.append(4)
    print(f"   修改别名后:")
    print(f"     原始列表: {original}")
    print(f"     别名列表: {alias}")
    
    # 2. 浅拷贝
    print("\n2. 浅拷贝 (copy.copy()):")
    original = [1, 2, [3, 4]]
    shallow = copy.copy(original)
    
    print(f"   原始列表: {original}, id: {id(original)}")
    print(f"   浅拷贝: {shallow}, id: {id(shallow)}")
    print(f"   是同一个对象: {original is shallow}")
    print(f"   内部列表是同一个对象: {original[2] is shallow[2]}")
    
    # 修改外部元素
    shallow[0] = 10
    print(f"   修改浅拷贝的外部元素:")
    print(f"     原始列表: {original}")
    print(f"     浅拷贝: {shallow}")
    
    # 修改内部列表
    shallow[2].append(5)
    print(f"   修改浅拷贝的内部列表:")
    print(f"     原始列表: {original}")
    print(f"     浅拷贝: {shallow}")
    
    # 3. 深拷贝
    print("\n3. 深拷贝 (copy.deepcopy()):")
    original = [1, 2, [3, 4]]
    deep = copy.deepcopy(original)
    
    print(f"   原始列表: {original}, id: {id(original)}")
    print(f"   深拷贝: {deep}, id: {id(deep)}")
    print(f"   是同一个对象: {original is deep}")
    print(f"   内部列表是同一个对象: {original[2] is deep[2]}")
    
    # 修改外部元素
    deep[0] = 10
    print(f"   修改深拷贝的外部元素:")
    print(f"     原始列表: {original}")
    print(f"     深拷贝: {deep}")
    
    # 修改内部列表
    deep[2].append(5)
    print(f"   修改深拷贝的内部列表:")
    print(f"     原始列表: {original}")
    print(f"     深拷贝: {deep}")


def demo_copy_variations():
    """演示不同的拷贝方法"""
    print("\n" + "=" * 60)
    print("不同拷贝方法的比较")
    print("=" * 60)
    
    # 1. 列表拷贝方法
    print("1. 列表的拷贝方法:")
    original = [1, 2, [3, 4]]
    
    # 列表切片
    copy_slice = original[:]
    print(f"   列表切片: {copy_slice}, 内部列表相同: {original[2] is copy_slice[2]}")
    
    # list.copy()
    copy_method = original.copy()
    print(f"   list.copy(): {copy_method}, 内部列表相同: {original[2] is copy_method[2]}")
    
    # copy.copy()
    copy_copy = copy.copy(original)
    print(f"   copy.copy(): {copy_copy}, 内部列表相同: {original[2] is copy_copy[2]}")
    
    # copy.deepcopy()
    copy_deep = copy.deepcopy(original)
    print(f"   copy.deepcopy(): {copy_deep}, 内部列表相同: {original[2] is copy_deep[2]}")
    
    # 2. 字典拷贝方法
    print("\n2. 字典的拷贝方法:")
    original_dict = {"a": 1, "b": [2, 3]}
    
    # dict.copy()
    dict_copy = original_dict.copy()
    print(f"   dict.copy(): {dict_copy}, 内部列表相同: {original_dict['b'] is dict_copy['b']}")
    
    # copy.copy()
    copy_dict = copy.copy(original_dict)
    print(f"   copy.copy(): {copy_dict}, 内部列表相同: {original_dict['b'] is copy_dict['b']}")
    
    # 3. 元组的拷贝（不可变对象）
    print("\n3. 元组的拷贝（不可变对象）:")
    original_tuple = (1, 2, [3, 4])
    tuple_copy = copy.copy(original_tuple)
    tuple_deep = copy.deepcopy(original_tuple)
    
    print(f"   原始元组: {original_tuple}, id: {id(original_tuple)}")
    print(f"   浅拷贝: {tuple_copy}, id: {id(tuple_copy)}, 是同一个对象: {original_tuple is tuple_copy}")
    print(f"   深拷贝: {tuple_deep}, id: {id(tuple_deep)}, 是同一个对象: {original_tuple is tuple_deep}")
    print(f"   内部列表是否相同: {original_tuple[2] is tuple_copy[2]}, {original_tuple[2] is tuple_deep[2]}")


def demo_practical_scenarios():
    """演示实际应用场景"""
    print("\n" + "=" * 60)
    print("实际应用场景演示")
    print("=" * 60)
    
    # 场景1：配置管理
    print("1. 配置管理场景:")
    
    DEFAULT_CONFIG = {
        "server": "localhost",
        "port": 8080,
        "timeout": 30,
        "retry": {
            "count": 3,
            "backoff": 0.5
        },
        "features": ["logging", "monitoring"]
    }
    
    def create_config(user_config=None):
        """创建配置，避免修改默认配置"""
        config = copy.deepcopy(DEFAULT_CONFIG)
        if user_config:
            config.update(user_config)
        return config
    
    # 创建用户配置
    user_config = {
        "port": 9090,
        "retry": {
            "count": 5
        },
        "features": ["logging"]
    }
    
    config1 = create_config(user_config)
    config2 = create_config()
    
    print(f"   默认配置特征: {DEFAULT_CONFIG['features']}")
    print(f"   配置1特征: {config1['features']}")
    print(f"   配置2特征: {config2['features']}")
    
    # 修改配置1的特征
    config1["features"].append("security")
    print(f"   修改配置1特征后:")
    print(f"     默认配置: {DEFAULT_CONFIG['features']}")
    print(f"     配置1: {config1['features']}")
    print(f"     配置2: {config2['features']}")
    
    # 场景2：数据处理
    print("\n2. 数据处理场景:")
    
    def process_data(data):
        """处理数据，不修改原始数据"""
        # 创建深拷贝，避免影响原始数据
        processed = copy.deepcopy(data)
        
        # 处理数据
        for item in processed:
            if "price" in item:
                item["price"] *= 1.1  # 提价10%
                item["original_price"] = item["price"] / 1.1
        
        return processed
    
    # 原始数据
    products = [
        {"name": "A", "price": 100, "tags": ["electronics"]},
        {"name": "B", "price": 200, "tags": ["clothing"]}
    ]
    
    processed = process_data(products)
    print(f"   原始数据: {products}")
    print(f"   处理后: {processed}")
    print(f"   原始数据未被修改: {products[0]['price'] == 100}")
    
    # 场景3：缓存系统
    print("\n3. 缓存系统场景:")
    
    cache = {}
    
    def get_cached_data(key, data_gen_func):
        """获取缓存数据，如果不存在则生成"""
        if key not in cache:
            # 生成数据并深拷贝后缓存
            data = data_gen_func()
            cache[key] = copy.deepcopy(data)
        return copy.deepcopy(cache[key])
    
    # 生成数据的函数
    def generate_data():
        return {"timestamp": time.time(), "values": [1, 2, 3]}
    
    # 第一次获取
    data1 = get_cached_data("data1", generate_data)
    time.sleep(0.5)
    
    # 第二次获取（应该使用缓存）
    data2 = get_cached_data("data1", generate_data)
    
    print(f"   两次获取的数据相同: {data1 == data2}")
    print(f"   时间戳相同（说明使用了缓存）: {data1['timestamp'] == data2['timestamp']}")
    
    # 修改获取的数据
    data1["values"].append(4)
    print(f"   修改后的数据1: {data1}")
    print(f"   缓存中的数据不变: {cache['data1']}")


def demo_performance_considerations():
    """演示拷贝性能考量"""
    print("\n" + "=" * 60)
    print("拷贝性能考量")
    print("=" * 60)
    
    # 创建不同复杂度的数据结构
    simple_data = list(range(100))
    nested_data = [list(range(100)) for _ in range(100)]
    deep_nested_data = [[[1 for _ in range(10)] for _ in range(10)] for _ in range(10)]
    
    # 测试浅拷贝性能
    print("1. 浅拷贝性能:")
    
    start = time.time()
    for _ in range(1000):
        copy.copy(simple_data)
    print(f"   简单数据: {time.time() - start:.6f}秒")
    
    start = time.time()
    for _ in range(1000):
        copy.copy(nested_data)
    print(f"   嵌套数据: {time.time() - start:.6f}秒")
    
    # 测试深拷贝性能
    print("\n2. 深拷贝性能:")
    
    start = time.time()
    for _ in range(1000):
        copy.deepcopy(simple_data)
    print(f"   简单数据: {time.time() - start:.6f}秒")
    
    start = time.time()
    for _ in range(1000):
        copy.deepcopy(nested_data)
    print(f"   嵌套数据: {time.time() - start:.6f}秒")
    
    start = time.time()
    for _ in range(100):
        copy.deepcopy(deep_nested_data)
    print(f"   深度嵌套数据: {time.time() - start:.6f}秒")
    
    # 内存占用比较
    print("\n3. 内存占用:")
    
    def get_size(obj, seen=None):
        """递归计算对象的内存大小"""
        if seen is None:
            seen = set()
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        seen.add(obj_id)
        size = sys.getsizeof(obj)
        
        if isinstance(obj, dict):
            size += sum(get_size(k, seen) + get_size(v, seen) for k, v in obj.items())
        elif hasattr(obj, '__dict__'):
            size += get_size(obj.__dict__, seen)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            size += sum(get_size(item, seen) for item in obj)
        
        return size
    
    nested_dict = {f"key_{i}": {f"inner_{j}": j for j in range(10)} for i in range(10)}
    shallow_nested = copy.copy(nested_dict)
    deep_nested = copy.deepcopy(nested_dict)
    
    print(f"   原始对象: {get_size(nested_dict):,} 字节")
    print(f"   浅拷贝: {get_size(shallow_nested):,} 字节")
    print(f"   深拷贝: {get_size(deep_nested):,} 字节")


def demo_common_pitfalls():
    """演示拷贝的常见陷阱"""
    print("\n" + "=" * 60)
    print("拷贝的常见陷阱")
    print("=" * 60)
    
    # 陷阱1：浅拷贝的深度不够
    print("1. 浅拷贝深度不够的陷阱:")
    data = {"users": [{"name": "Alice", "roles": ["admin", "user"]}]}
    shallow_copy = copy.copy(data)
    
    # 修改嵌套结构
    shallow_copy["users"][0]["roles"].append("manager")
    print(f"   原始数据: {data['users'][0]['roles']}")
    print(f"   浅拷贝: {shallow_copy['users'][0]['roles']}")
    print(f"   两者相同: {data['users'][0]['roles'] is shallow_copy['users'][0]['roles']}")
    
    # 陷阱2：不可变对象的拷贝
    print("\n2. 不可变对象的拷贝陷阱:")
    tuple_data = (1, 2, [3, 4])
    tuple_copy = copy.copy(tuple_data)
    
    print(f"   元组浅拷贝是同一个对象: {tuple_data is tuple_copy}")
    print(f"   但内部列表仍然可以修改: {tuple_data[2]}")
    
    tuple_data[2].append(5)
    print(f"   修改内部列表后: {tuple_copy[2]}")
    
    # 陷阱3：自定义对象的拷贝
    print("\n3. 自定义对象的拷贝陷阱:")
    
    class Person:
        """人员类"""
        def __init__(self, name, address):
            self.name = name
            self.address = address
        
        def __repr__(self):
            return f"Person({self.name}, {self.address})"
    
    class Address:
        """地址类"""
        def __init__(self, street, city):
            self.street = street
            self.city = city
        
        def __repr__(self):
            return f"Address({self.street}, {self.city})"
    
    address = Address("Main St", "New York")
    person = Person("Alice", address)
    
    # 浅拷贝
    person_shallow = copy.copy(person)
    print(f"   浅拷贝: {person_shallow}")
    print(f"   地址对象相同: {person.address is person_shallow.address}")
    
    # 修改地址
    person_shallow.address.city = "Boston"
    print(f"   修改浅拷贝的地址后:")
    print(f"     原始对象: {person}")
    print(f"     浅拷贝: {person_shallow}")
    
    # 深拷贝
    person_deep = copy.deepcopy(person)
    person_deep.address.city = "Chicago"
    print(f"   修改深拷贝的地址后:")
    print(f"     原始对象: {person}")
    print(f"     深拷贝: {person_deep}")


def main():
    """主函数"""
    print("=" * 60)
    print("深浅拷贝难点实战演示")
    print("=" * 60)
    print("本演示涵盖:")
    print("1. 浅拷贝与深拷贝的基本概念")
    print("2. 不同数据类型的拷贝方法")
    print("3. 实际应用场景")
    print("4. 性能考量")
    print("5. 常见陷阱")
    print("=" * 60)
    
    # 运行各个演示
    demo_basic_copy()
    demo_copy_variations()
    demo_practical_scenarios()
    demo_performance_considerations()
    demo_common_pitfalls()
    
    print("\n" + "=" * 60)
    print("难点总结:")
    print("1. 浅拷贝只复制一层，深拷贝递归复制所有层级")
    print("2. 不可变对象的拷贝通常返回原对象")
    print("3. 嵌套数据结构需要深拷贝以避免意外修改")
    print("4. 深拷贝性能开销较大，注意使用场景")
    print("5. 自定义对象需要考虑__copy__和__deepcopy__方法")
    print("=" * 60)


if __name__ == "__main__":
    main()