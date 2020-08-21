"""
    变化点：增加飞机、火车、自行车....
    缺点：违反了面向对象设计原则 -- 开闭原则
          -- 允许增加新功能,但是不能修改客户端代码.
"""
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,position,a):
        print(self.name + "去"+position)
        if type(a) == Car:
            a.run()
        elif type(a) == Airplane:
            a.fly()

class Car:
    def run(self):
        print("汽车在行驶")

class Airplane:
    def fly(self):
        print("飞机在飞行")

lz = Person("老张")
car = Car()
air = Airplane()
lz.go_to("东北",car)
lz.go_to("东北",air)
