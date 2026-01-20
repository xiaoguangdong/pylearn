"""
    该案例演示了字符串常用的函数
"""
"""
str.replace(old,new[,max])	把将字符串中的old替换成new,如果指定max，则替换不超过max次
str1 = "hello world"
str2 = str1.replace("o","z",1)
print(str2)
"""

#str.split([x][,n])	按x分隔字符串，默认按任何空白字符串分隔并在结果中丢弃空字符串。可指定最大分隔次数

str1 = "a,b,c,d,e,f"
# print(type(str1.split(",")))
list1 = str1.split(",",3)
print(list1)


"""
x.join(seq)	以x作为分隔符，将序列中所有的字符串合并为一个新的字符串

list1 = ["a","b","c","d","e","f"] # a-b-c-d-e-f
# 列表中的元素类型 必须是str
# list1 = [1,2,3,4,5]
str1 = "-".join(list1)
print(str1)
"""

"""
str.find(x[,start][,end])	返回字符串中第一个x的索引值，不存在则返回-1，可指定字符串开始结束范围
str1 = "fdasjfdkasfadsjjsa"
print(str1.find("a",3,8))
"""
"""
str.index(x[,start][,end])	返回字符串中第一个x的索引值，不存在则报错，可指定字符串开始结束范围
"""
str1 = "fdasjfdkasfadsjjsa"
# print(str1.index("a"))
print(str1.index("asj"))
