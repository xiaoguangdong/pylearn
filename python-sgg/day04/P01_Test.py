
"""
    练习题讲解
"""
# 水仙花数   3位数= 百位^3 + 十位^3 + 个位^3
# num = 100
#
# while num < 1000:
#     a = num // 100
#     b = num // 10 % 10
#     c = num % 10
#     if num == a ** 3 + b ** 3 + c ** 3:
#         print(num)
#     num += 1

# 输入当前时间，得到时间的下一秒
hh = int(input("请输入小时(0~23):"))
mm = int(input("请输入小时(0~59):"))
ss = int(input("请输入小时(0~59):"))

print(f"当前输入的时间为:{hh}:{mm}:{ss}")
# 秒 +1 得到下一秒
ss += 1
if ss == 60:
    ss = 0
    mm += 1
    if mm == 60:
        mm = 0
        hh += 1
        if hh == 24:
            hh = 0

print(f"下一秒的时间为:{hh}:{mm}:{ss}")




