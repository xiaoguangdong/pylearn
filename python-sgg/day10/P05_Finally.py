"""
    该案例演示了finally
"""
"""
try:
    result = 3 / 1
except ZeroDivisionError as e:
    print(e)
else:
    print(result)
finally:
    print("finally")

print("End")


"""
try:
    result = 3 / 0
except NameError as e:
    print(e)
else:
    print(result)
finally:
    print("finally")

print("End")
