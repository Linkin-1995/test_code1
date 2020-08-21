"""
    练习:
    创建手机类
        数据：品牌、价格、颜色
        行为：通话
    实例化两个对象并调用其方法
    体会:抽象/具体
    练习:画出下列代码内存图
"""


# 类命名:所有单词大写,不要使用下划线隔开
class MobilePhone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
        self.a = 100

    def call(self):
        print(self.brand + "手机打电话")

p01 = MobilePhone("苹果", 9999, "白色")
p01.call()
print(p01.__dict__)

p02 = MobilePhone("华为", 5000, "绿色")
p02.call()
