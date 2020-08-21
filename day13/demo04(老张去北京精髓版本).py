"""
    变化点：增加飞机、火车、自行车....

    三大特征：
        封装：创建人类,汽车类,飞机类         [分]
        继承：创建交通工具隔离火车、飞机等变化 [隔]
        多态：人调用交通工具,　　　　　　　　　[做]　　　
        　　　火车、飞机重写运输方法,
        　　　创建火车飞机对象
    练习：
        情景：手雷爆炸，可能伤害敌人或者玩家的生命。
        变化：还可能伤害房子、树、鸭子....
        要求：增加新事物，不影响手雷.
        体会：开闭原则
        写出：封装继承多态具体体现
            画出架构设计图


"""
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,position,vehicle):
        print(self.name + "去"+position)
        # 1. 编码时　调用父 transport 方法
        #　　　运行时 执行子
        vehicle.transport()

class Vehicle:
    def transport(self):
        pass

# -----------以上代码是框架--以下代码是实现-----------------
class Car(Vehicle):
    # 2. 子重写
    def transport(self):
        print("汽车在行驶")

class Airplane(Vehicle):
    def transport(self):
        print("飞机在飞行")


# -----------测试-------------
lz = Person("老张")
car = Car()
air = Airplane()
# 3. 创建子
lz.go_to("东北",car)
lz.go_to("东北",air)
