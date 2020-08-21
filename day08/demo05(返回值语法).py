"""
    返回值语法
        价值1:返回结果
        价值2: 退出函数(无视循环,都能退出)

        注意：
        return # return 后面没有数据,默认返回None
        函数没有返回值(没写return),也默认返回None
"""


# 价值1:返回结果
# 函数返回数据100
def func01():
    print("func01执行喽")
    return 100


data = func01()
print(data)  # 100


# 价值2: 退出函数(无视循环,都能退出)
def func02():
    print("func02执行喽")
    return 100
    print("func02又执行喽")


data = func02()
print(data)  # 100


# 注意：
# return # return 后面没有数据,默认返回None
# 函数没有返回值(没写return),也默认返回None　
def func03():
    print("func03执行喽")


data = func03()
print(data)  # None
