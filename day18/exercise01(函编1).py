"""
    lambda 应用  - 作为函数的实参
        定义函数,只为传参,需要使用lambda代替普通函数.
        普通函数(lambda 参数:函数体)
"""
from common.iterable_tools import IterableHelper


class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color


list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

# 将查找条件定义在函数中
# item.color == "白色"

# def condition01(item):
#     return item.color == "白色"

# for item in IterableHelper.find_all(list_phones,condition01):

# 调用通用函数
for item in IterableHelper.find_all(list_phones, lambda item: item.color == "白色"):
    print(item.__dict__)

# def condition02(item):
#     return item.brand == "苹果2"
#
# result = IterableHelper.find_single(list_phones, condition02)
# print(result.__dict__)

result = IterableHelper.find_single(list_phones, lambda item: item.brand == "苹果2")
print(result.__dict__)
