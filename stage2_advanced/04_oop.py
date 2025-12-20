# -*- coding: utf-8 -*-
"""
第二阶段：面向对象编程
演示类与对象、继承与多态、特殊方法和属性装饰器
"""


class Animal:
    """动物基类"""
    
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
    
    def __str__(self):
        """字符串表示"""
        return f"{self.name}({self.age}岁)"
    
    def __repr__(self):
        """对象表示"""
        return f"Animal(name='{self.name}', age={self.age})"
    
    def make_sound(self):
        """发出声音"""
        return "动物发出声音"
    
    def get_info(self):
        """获取信息"""
        return f"这是一只{self.age}岁的{self.name}"


class Dog(Animal):
    """狗类 - 继承自Animal"""
    
    def __init__(self, name, age, breed):
        """初始化方法"""
        super().__init__(name, age)  # 调用父类初始化
        self.breed = breed
    
    def make_sound(self):
        """重写父类方法 - 多态"""
        return "汪汪汪！"
    
    def get_info(self):
        """重写父类方法"""
        return f"这是一只{self.age}岁的{self.breed}品种的狗，名叫{self.name}"


class Cat(Animal):
    """猫类 - 继承自Animal"""
    
    def __init__(self, name, age, color):
        """初始化方法"""
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        """重写父类方法 - 多态"""
        return "喵喵喵！"
    
    def get_info(self):
        """重写父类方法"""
        return f"这是一只{self.color}色的{self.age}岁的猫，名叫{self.name}"


class Student:
    """学生类 - 演示属性装饰器"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._score = 0
    
    @property
    def name(self):
        """姓名属性（只读）"""
        return self._name
    
    @property
    def age(self):
        """年龄属性"""
        return self._age
    
    @age.setter
    def age(self, value):
        """年龄设置器"""
        if value < 0 or value > 150:
            raise ValueError("年龄必须在0-150之间")
        self._age = value
    
    @property
    def score(self):
        """分数属性"""
        return self._score
    
    @score.setter
    def score(self, value):
        """分数设置器"""
        if value < 0 or value > 100:
            raise ValueError("分数必须在0-100之间")
        self._score = value
    
    @property
    def grade(self):
        """等级属性（计算属性）"""
        if self._score >= 90:
            return "优秀"
        elif self._score >= 80:
            return "良好"
        elif self._score >= 60:
            return "及格"
        else:
            return "不及格"
    
    def __str__(self):
        return f"Student(name='{self._name}', age={self._age}, score={self._score}, grade='{self.grade}')"


def demo_classes_and_objects():
    """演示类与对象"""
    print("=" * 50)
    print("类与对象演示")
    print("=" * 50)
    
    # 创建对象
    animal = Animal("通用动物", 5)
    print(f"创建对象: {animal}")
    print(f"对象信息: {animal.get_info()}")
    print(f"发出声音: {animal.make_sound()}")
    
    print()


def demo_inheritance_and_polymorphism():
    """演示继承与多态"""
    print("=" * 50)
    print("继承与多态演示")
    print("=" * 50)
    
    # 创建子类对象
    dog = Dog("旺财", 3, "金毛")
    cat = Cat("小花", 2, "橘色")
    
    print(f"狗: {dog}")
    print(f"狗的信息: {dog.get_info()}")
    print(f"狗的声音: {dog.make_sound()}")
    
    print(f"\n猫: {cat}")
    print(f"猫的信息: {cat.get_info()}")
    print(f"猫的声音: {cat.make_sound()}")
    
    # 多态演示 - 同一个接口，不同的实现
    print("\n多态演示:")
    animals = [dog, cat]
    for animal in animals:
        print(f"  {animal.name}: {animal.make_sound()}")
    x
    print()


def demo_special_methods():
    """演示特殊方法"""
    print("=" * 50)
    print("特殊方法演示")
    print("=" * 50)
    
    dog1 = Dog("旺财", 3, "金毛")
    dog2 = Dog("来福", 2, "哈士奇")
    
    # __str__ 方法
    print(f"__str__: {str(dog1)}")
    
    # __repr__ 方法
    print(f"__repr__: {repr(dog1)}")
    
    # 可以添加更多特殊方法
    class Point:
        """点类 - 演示更多特殊方法"""
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            """加法运算符重载"""
            return Point(self.x + other.x, self.y + other.y)
        
        def __eq__(self, other):
            """相等运算符重载"""
            return self.x == other.x and self.y == other.y
        
        def __str__(self):
            return f"Point({self.x}, {self.y})"
    
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = p1 + p2
    print(f"\n点运算:")
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p1 + p2 = {p3}")
    print(f"p1 == p2: {p1 == p2}")
    
    print()


def demo_property_decorator():
    """演示属性装饰器"""
    print("=" * 50)
    print("属性装饰器演示")
    print("=" * 50)
    
    student = Student("张三", 20)
    print(f"初始状态: {student}")
    
    # 使用属性设置器
    student.age = 21
    student.score = 85
    print(f"修改后: {student}")
    
    # 访问计算属性
    print(f"等级: {student.grade}")
    
    # 尝试设置无效值
    try:
        student.age = 200
    except ValueError as e:
        print(f"错误: {e}")
    
    try:
        student.score = 150
    except ValueError as e:
        print(f"错误: {e}")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_classes_and_objects()
    demo_inheritance_and_polymorphism()
    demo_special_methods()
    demo_property_decorator()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

