"""
    需求2:
        定义函数,删除手机列表中所有蓝色手机
        定义函数,删除手机列表中所有单价大于7000的手机

    步骤:
        1. 根据需求实现功能
            参考:day09/homework/exercise09

        5. 将通用代码定义到IterableHelper类中
        6. 用lambda代替变化点
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


def delete_all01():
    for i in range(len(list_phones) - 1, -1, -1):
        if list_phones[i].color == "蓝色":
            del list_phones[i]

def delete_all02():
    for i in range(len(list_phones) - 1, -1, -1):
        if list_phones[i].price < 7000:
            del list_phones[i]

# def condtion01(phone):
#     return phone.color == "蓝色"

IterableHelper.delete_all(list_phones,lambda phone:phone.color == "蓝色")
for item in list_phones:
    print(item.__dict__)