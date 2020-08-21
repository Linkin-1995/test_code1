"""
    继承 - 数据
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1. 子类没有构造函数,将使用父类构造函数
# class Student(Person):
#     pass
#
# s01 = Student("悟空",25)
# print(s01.__dict__)

# 2. 子类有构造函数,将覆盖父类构造函数(好像它不存在)
#    此时:子类必须通过super()函数调用父类构造函数.
class Student(Person):
    # 子类构造函数参数:父类构造函数参数,子类构造函数参数
    def __init__(self,name,age,score):
        self.score = score
        # 通过super()函数调用父类构造函数.
        super().__init__(name,age)
        # self.name = name
        # self.age = age

s01 = Student("悟空",25,100) # 执行子类构造函数
print(s01.__dict__)






