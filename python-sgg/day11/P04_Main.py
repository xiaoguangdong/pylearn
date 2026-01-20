"""
    该案例演示了带包模块的导入
"""
"""
# 全局导入
# import graphic.circle
# import graphic.circle as c
print(circle.area(10))
"""

"""
# 局部导入  从包中导入模块
from graphic import circle

print(circle.area(10))
"""
"""
# 局部导入  导入包下某个模块的成员
from graphic.circle import area
print(area(10))
"""

"""
# 局部导入  from 包 import *
from graphic import *
print(circle.area(10))
print(rectangle.area(10,20))
"""

# import graphic.circle
# c = graphic.circle.Circle(10)
# print(c.area())


import graphic

c = graphic.circle.Circle(10)
r = graphic.rectangle.Rectangle(10,20)
print(c.area())
print(r.area())
