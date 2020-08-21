"""
    创建狗类
        数据：品种、爱称、年龄、体重
        行为：吃、叫
    实例化两个对象并调用其方法
    画出内存图
    体会:不同狗对象,具有不同的数据.
"""


class Dog:
    def __init__(self, variety, name, age, weight):
        self.variety = variety
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(self.name + "吃东西")

    def yell(self):
        print(self.name + "大声喊叫")


d01 = Dog("拉布拉多", "米咻", 5, 70)
d01.eat()
d01.yell()

d02 = Dog("拉布拉多", "黑米", 4, 60)
d02.eat()
d02.yell()
