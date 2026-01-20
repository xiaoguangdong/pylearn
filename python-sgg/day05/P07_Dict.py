"""
    该案例演示了字典基本操作
"""
"""
# 创建字典对象
dict1 = {}
dict2 = dict()
dict3 = {"a":"A","b":"B","c":"C"}
dict4 = dict(a="A",b="B",c="C")

dict5 = dict([("a","A"),("b","B"),("c","C")])

dict6 = {i:i*2 for i in range(5)}
print(dict1,type(dict1))
print(dict2,type(dict2))
print(dict3,type(dict3))
print(dict4,type(dict4))
print(dict5,type(dict5))
print(dict6,type(dict6))
"""
"""
# 访问字典元素
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
print(dict1["name"])
print(dict1["age"])
print(dict1["gender"])
# print(dict1["add"]) # 如果没有对应的key,会报错

print(dict1.get("name"))
print(dict1.get("age"))
print(dict1.get("gender"))
print(dict1.get("add")) # # 如果没有对应的key,返回None
print(dict1.get("add","beijing")) # # 如果没有对应的key,返回None
"""
"""
# 向字典中添加元素以及对元素进行修改
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
dict1["age"] = 20
dict1["add"] = "beijing"
print(dict1)

# 判断字典中是否包含key
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
print("name" in dict1)
# 不能对value进行判断
print("Alice" in dict1)
# 获取字典长度
print(len(dict1))
"""

dict1 = {"swk":"六小龄童","bj":"马德华","shs":"闫怀礼","ts":"迟重瑞"}
"""
# 遍历出字典的所有key
keys = dict1.keys()
print(keys)
for key in keys:
    print(key)

# 遍历出字典的所有value
values = dict1.values()
print(values)
print(type(values))
for val in values:
    print(val)
# 对k-v同时进行遍历--方式1
keys = dict1.keys()
for k in keys:
    print(f"{k}-------------------------{dict1.get(k)}")


# 对k-v同时进行遍历--方式2
items = dict1.items()
print(items)
print(type(items))
for item in items:
    print(item)
"""

# 删除字典元素
# del dict1["swk"]
# dict1.clear()
# del dict1
# print(dict1)

# dict.pop(key[,default])	获取key所对应的value，同时删除该键值对，可设置默认值
# print(dict1.pop("qtds"))

# dict.popitem()	取出字典中的最后插入的键值对，字典为空则报错
# print(dict1.popitem())
# print(dict1)

# dict1.update(dict2)	将dict2中的键值对更新到dict1中
dict2 = {"nz":"nezha"}
dict1.update(dict2)
print(dict1)


# dict.setdefault(key[,default])	获取字典中key对应value，可设置默认值。若key不存在于字典中，将会添加key并将value设为默认值

# dict2.setdefault("zr","aaaa")
# print(dict2)

# dict.fromkeys(seq[,default])	以序列seq中元素做字典的key创建一个新字典，可设置value的默认值

dict5 = dict2.fromkeys(range(5))

print(dict2)
print(dict5)