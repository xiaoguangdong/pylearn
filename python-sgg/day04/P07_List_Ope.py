"""
    该案例演示了列表常用的操作
"""
list1 = [100,200,600,300,400,600,500,600]
# list.insert(index,x)	在指定位置插入x
# list1.insert(4,800)
# list.append(x)	在列表末尾追加x
# list1.append(600)
# list1.extend(list2)	在列表1的末尾追加列表2的数据
# list2 = ["a","b","c","d","e"]
# list1.extend(list2)
# del list[index]	删除指定位置的数据或切片
# del list1[0]
# list.remove(x)	删除第一次出现的x
# list1.remove(200)
# list.pop([index])	删除指定位置的数据，默认为末尾数据
# list1.pop(-4)
# list.clear()	清空列表中元素
# list1.clear()
# list[index] = x	修改指定位置的数据
# list1[0] = 600
# list1[start:end] = list2	修改列表切片的数据
# list1[0:2] =["a","b"]
# sorted(list[,reverse=True])	返回排序后的新列表，可选降序
# list2 = sorted(list1,reverse=True)
# print(list2)
# list.sort([reverse=True])	对列表就地排序，可选降序
list1.sort()
# list.reverse()	反转列表中的元素
# list1.reverse()
# list.index(x[,start,[,end]])	返回x在列表中首次出现的位置，可指定起始和结束范围
# print(list1.index(600))
# list.count(x)	返回x的数量
# print(list1.count(600))
# len(list)	返回列表元素个数
#print(len(list1))
# max(list)	返回列表中最大值
# min(list)	返回列表中最小值
# sum(list)	返回列表中所有元素和
# list.copy()	拷贝列表
# list2 = list1.copy()
# list2[0] = 900
# print(id(list1), id(list2))
# list(x)	将序列转换为列表
# print(list2)
# print(list1)
