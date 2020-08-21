"""
    继承 - 方法
        财产:钱不用孩子挣,但是也能花.
        皇位:江山不用太子打,但是能坐.
        代码:子类不用写,但是能直接用.
    练习:exercise04
"""


# 多个类型,有行为上的共性,在概念上是一致的.
class Person:
    def say(self):
        print("说话")


class Student(Person):
    def study(self):
        print("学习")
        self.say()


class Teacher(Person):
    def teach(self):
        print("教学")
        self.say()


# 子类可以访问父子成员
s01 = Student()
s01.study()

# 父类只能访问父类成员
p01 = Person()
p01.say()

# python 类型间关系的判定
# 1. isinstance( 对象,类型    )
# 学生对象 是一种 学生类型
print(isinstance(s01, Student))  # True
# 学生对象 是一种 人类型
print(isinstance(s01, Person))  # True
# 人对象 是一种 学生类型
print(isinstance(p01, Student))  # False

# 2. issubclass( 类型,类型   )
# 学生类型 是一种 学生类型
print(issubclass(Student, Student))  # True
# 学生类型 是一种 人类型
print(issubclass(Student, Person))  # True
# 人类型 是一种 学生类型
print(issubclass(Person, Student))  # False

# 3. type(对象) == 类型
# 学生对象 是 学生类型
print(type(s01) == Student)  # True
# 学生对象 是 人类型
print(type(s01) == Person)  # False
# 人对象 是 学生类型
print(type(p01) == Student)  # False

"""
练习:
    创建子类：狗(跑)，鸟类(飞)
    创建父类：动物(吃)
    体会子类复用父类方法
    体会 isinstance 、issubclass 与 type 的作用
"""





