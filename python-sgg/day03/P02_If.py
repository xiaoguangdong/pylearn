"""
    该案例演示了单分支
    需求：商品价格50，若余额小于50则提示“余额不足，请充值”，最后打印“欢迎下次光临”
"""
from random import randint

# 随机生成1~100的整数 ，包括1和100
balance = randint(1, 100)
print(f"当前余额是：{balance}")
# 商品价格50
price = 50

# 注意：if分支后面的:冒号不要忘记
if balance < price:
    print("余额不足，请充值")

print("欢迎下次光临")
