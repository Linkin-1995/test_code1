"""
    参照day11/homework/exercise02
    定义函数,在全局变量list_phones中,
        查找单价小于6000的所有手机

    定义函数,在全局变量list_phones中,
        查找蓝色手机(单个)

    重点体会：函数返回多个结果使用　- yield
            函数返回单个结果使用　- return
"""



class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

# 1
list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

def find01():
    # for i in range(len(list_phones)):
    #     if list_phones[i].price < 6000:
    for phone in list_phones:
        if phone.price < 6000:
            yield phone

for item in find01():
    print(item.__dict__)


def find02():
    for phone in list_phones:
        if phone.color == "蓝色":
            return phone

phone = find02()
print(phone.__dict__)

