"""
    需求1:
        定义函数,在手机列表中,获取所有手机的品牌
        # "华为1"  "华为2"  "苹果1" .....
        定义函数,在手机列表中,获取所有手机的品牌与颜色
    步骤:
        1. 根据需求实现功能
        2. "封装":将所有变化点定义为函数,通用代码定义函数
        3. "继承":用参数隔离变化
        4. "多态":调用通用函数,传递变化点(lambda).

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

"""
def select01():
    for item in list_phones:
        yield item.brand


def select02():
    for item in list_phones:
        yield item.brand, item.color


def handle01(item):
    return item.brand


def handle02(item):
    return item.brand, item.color


def select(handle):
    for item in list_phones:
        # yield item.brand, item.color
        # yield handle02(item)
        yield handle(item)


for item in select(handle02):
    print(item)

# for item in IterableHelper.select(list_phones,handle02):
#     print(item) 
"""

# lambda 参数是 list_phones中每个元素
# lambda 函数体是对列列表每个元素处理逻辑
for item in IterableHelper.select(list_phones,lambda item: (item.brand, item.color)):
    print(item)