"""
    day11/homework/exercise02
    1. 比较两个手机对象是否相同
    2. 判断手机列表中是否存在某个手机对象
    3. 根据单价对手机列表进行排序
"""
class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def __eq__(self, other):
        if type(other) == Phone:
            return self.brand == other.brand
        elif type(other) == str:
            return self.brand == other

    def __lt__(self, other):
        return self.price  < other.price

list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

print(list_phones[0] == list_phones[1])
# Phone("华为1", 5999, "蓝色").__eq__("华为1")
print(Phone("华为1", 5999, "蓝色") == "华为1")

print("华为1" in list_phones)

list_phones.sort() # 内部会循环调用__lt__

print(list_phones)