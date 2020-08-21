"""
    需求3:
        定义函数,计算手机列表中白色手机的数量
        定义函数,计算手机列表中价格大于7000的数量

    需求4:
        定义函数,计算手机列表中最贵的手机
        定义函数,计算手机列表中名字最长的手机
        温馨提示:根据任意条件查找最大值

    步骤:
        1. 根据需求实现功能
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
    Phone("HUAWEI2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

"""
def get_count01():
    count = 0
    for phone in list_phones:
        if phone.color == "白色":
            count += 1
    return count

def get_count02():
    count = 0
    for phone in list_phones:
        if phone.price > 7000:
            count += 1
    return count
"""

print(IterableHelper.get_count(list_phones, lambda p: p.color == "白色"))

#  [先用] -- 做通用函数时,调用 max_value.price 的函数
#  [后做] -- 用通用函数时,做lambda代替 max_value.price 的函数
"""
def get_max01():
    max_value = list_phones[0]
    for i in range(1, len(list_phones)):
        if max_value.price < list_phones[i].price:
            max_value = list_phones[i]
    return max_value

def get_max02():
    max_value = list_phones[0]
    for i in range(1, len(list_phones)):
        if len(max_value.brand) < len(list_phones[i].brand):
            max_value = list_phones[i]
    return max_value
"""
re = IterableHelper.get_max(list_phones,lambda element:element.price)
re = IterableHelper.get_max(list_phones,lambda element:len(element.brand))
print(re.__dict__)