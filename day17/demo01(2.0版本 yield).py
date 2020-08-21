"""
    迭代器 --> yield
    练习1:将迭代器版本的图形管理器day16/exercise03
        改为yield版本实现

    练习2:将MyRange1.0版本exercise01
        改为yield版本实现
"""

class StudentController:
    def __init__(self):
        self.__list_students = []

    def add_student(self, stu):
        self.__list_students.append(stu)

    # def __iter__(self):
    #     # 生成迭代器代码的大致规则:
    #     # 1. 将yield之前的代码放在__next__方法体中
    #     # 2. 将yield之后的数据作为__next__方法返回值
    #     print("准备")
    #     yield self.__list_students[0]
    #
    #     print("准备")
    #     yield self.__list_students[1]
    #
    #     print("准备")
    #     yield self.__list_students[2]

    def __iter__(self):
        for item in self.__list_students:
            print("准备数据")
            yield item

controller = StudentController()
controller.add_student("程以宁")
controller.add_student("高家富")
controller.add_student("李杰")

# 遍历自定义对象
for name in controller:
    print(name) #

# iterator = controller.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
