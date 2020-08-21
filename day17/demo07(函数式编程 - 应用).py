"""
    函数式编程 - 应用
        "封装": 将变化点定义到函数中   [分]
        "继承": 用参数抽象变化        [隔]
               调用参数统一函数的定义
               通用函数与具体条件隔离开
        "多态": 彰显子类的个性        [做]
               制作变化点的功能
"""
list01 = [3, 443, 4, 54, 6]


# 适用性:多个函数,主体部分相同,核心逻辑不同.

# 1. 定义函数,获取所有大于10的整数
def find01():
    for item in list01:
        if item > 10:
            yield item


# 2. 定义函数,获取所有小于5的整数
def find02():
    for item in list01:
        if item < 5:
            yield item


# 变化的
# "子重写":(后)做法 满足 (先)用法
def condition01(item):
    return item > 10


def condition02(item):
    return item < 5


# 通用的
def find(condition):
    for item in list01:
        # if item < 5:
        # if condition02(item):
        # 1.调用"父"
        if condition(item):
            yield item


# "创建子":传递具体条件
for item in find(condition01):
    print(item)


def condition03(item):
    return item % 2
