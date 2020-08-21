"""
    需求5:
        定义函数,判断手机列表中是否存在品牌是"三星2"的手机
        定义函数,判断手机列表中是否存在价格大于10000的手机
        结果是:bool类型

    需求6:
        定义函数,根据单价对手机列表进行升序排列
        定义函数,根据品牌长度对手机列表进行升序排列

    步骤:
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
def is_exists01():
    for phone in list_phones:
        if phone.brand == "三星2":
            return True
    return False

def is_exists02():
    for phone in list_phones:
        if phone.price > 10000:
            return True
    return False
"""

print(IterableHelper.is_exists(list_phones, lambda phone: phone.price > 10000))

"""
def order_by01():
    for r in range(len(list_phones)-1):
        for c in range(r+1,len(list_phones)):
            if list_phones[r].price >  list_phones[c].price:
                list_phones[r],list_phones[c] = list_phones[c],list_phones[r]
                
def order_by02():
    for r in range(len(list_phones)-1):
        for c in range(r+1,len(list_phones)):
            if len(list_phones[r].brand) >  len(list_phones[c].brand):
                list_phones[r],list_phones[c] = list_phones[c],list_phones[r]
"""
IterableHelper.order_by(list_phones, lambda p: p.price)
for item in list_phones:
    print(item.__dict__)
