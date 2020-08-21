"""
需求:
    定义函数,在手机列表中查找品牌是"华为2"的手机对象(1个)
    定义函数,在手机列表中查找单价是4999的手机对象(1个)
步骤:
    1. 根据需求,实现功能
    2. 封装 - 分
    3. 继承 - 隔
    4. 多态 - 做
"""
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

# 完整的
def find01():
    for phone in list_phones:
        if phone.brand == "华为2":
            return phone

def find02():
    for phone in list_phones:
        if phone.price == 4999:
            return phone
**************************************************************************
# 变化的 ....
def condition01(phone):
    return phone.brand == "华为2"

def condition02(phone):
    return phone.price == 4999

# 不变的
def find(condition):
    for phone in list_phones:
        # if phone.price == 4999:
        # if condition02(phone):
        if condition(phone):
            return phone

# 不变的 + 变化的 = 完整
phone = find(condition02)
print(phone.__dict__)
