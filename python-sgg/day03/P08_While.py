"""
    该案例演示了while循环
    需求：第1周有2只兔子，此后每周兔子的数量都增加上周数量的2倍，且期间没有兔子死亡，求第10周共有多少只兔子：
"""
# week = 1
# rabbit = 2
# while week < 10:
#     rabbit = rabbit + rabbit * 2
#     week += 1
# print(rabbit)


# 打印进度条
# import time
# num = 1
# while num <= 100:
#     print("\r" + "=" * num,end="")
#     num += 1
#     time.sleep(0.5)


rabbit = 2
week = 1
while week < 10:
    rabbit = rabbit + rabbit * 2
    week += 1
    if week == 5:
        break
else:
    print(f"第{week}周有{rabbit}只兔子")

