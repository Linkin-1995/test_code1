"""
    步骤:
        1. 根据需求,实现功能
        2. 封装 - 分
        3. 继承 - 隔
        4. 多态 - 做
"""
dict01 = {
    1001: "张无忌",
    1002: "赵敏",
    1003: "周芷若"
}


# 1. 需求
# 定义函数,在字典中获取所有房间号小于1003的键值对(元组)
def find01():
    for key, value in dict01.items():
        if key < 1003:
            yield key, value


# 定义函数,在字典中获取姓名长度大于2个字的键值对(元组)
def find02():
    for key, value in dict01.items():
        if len(value) > 2:
            yield key, value

***************************************************************
def condition01(key, value):
    return key < 1003


def condition02(key, value):
    return len(value) > 2


def find(condition):
    for key, value in dict01.items():
        # if len(value) > 2:
        # if condition02(key, value):
        if condition(key, value):
            yield key, value


for item in find(condition01):
    print(item)
