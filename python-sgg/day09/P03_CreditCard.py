"""
    该案例演示了使用封装信用卡类设计案例
"""
class CreditCard:
    def __init__(self,name):
        self.name = name
        self.__password = None
        self.__balance = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,password):
        if password != "888888":
            print("密码输入有误")
        else:
            print("密码输入正确")
            self.__password = password

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        if balance < 0:
            print("理性消费，信用卡爆了")
        else:
            print("消费成功")
            self.__balance = balance

c1 = CreditCard("mzl")
# print(c1.password)
c1.password = "666666"
c1.password = "888888"
c1.balance = -100

