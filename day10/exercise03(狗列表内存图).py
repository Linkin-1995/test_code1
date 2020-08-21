"""
    实例变量 - 练习
        1. 画出列表list_dogs内存图
        2. 画出调用find_dog_by_name函数内存图
"""


class Dog:
    def __init__(self, variety, name, age, weight):
        self.variety = variety
        self.name = name
        self.age = age
        self.weight = weight


d01 = Dog("拉布拉多", "米咻", 5, 70)
list_dogs = [
    d01,
    Dog("拉布拉多", "黑米", 4, 60),
    Dog("黑背", "哮天犬", 4, 30),
    Dog("藏獒", "小黑", 4, 80),
]


# 做法:在狗列表中根据名称查找狗对象的功能
def find_dog_by_name(name):
    for dog in list_dogs:
        if dog.name == name:
            return dog


result = find_dog_by_name("黑米")
print(result.name)


# 练习1:创建函数,在狗列表中查找品种是"黑背"的狗对象(如果有多个也查找第一个)
def find_dog_by_variety(variety):
    for dog in list_dogs:
        if dog.variety == variety:
            return dog


result = find_dog_by_variety("黑背")
print(result.name)


# 练习2:创建函数,在狗列表中查找所有体重大于10的狗对象
def find_dog_gt_weight(weight):
    list_result = []
    for dog in list_dogs:
        if dog.weight > weight:
            list_result.append(dog)
    return list_result


result = find_dog_gt_weight(10)
# [<__main__.Dog object at 0x7faddc1e8320>, <__main__.Dog object at 0x7faddc1e8358>, <__main__.Dog object at 0x7faddc1e8390>, <__main__.Dog object at 0x7faddc1e83c8>]
# print(result) # 打印狗列表,显示所有狗的地址
for item in result:
    print(item.weight)
