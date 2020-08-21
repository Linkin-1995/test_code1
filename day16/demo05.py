"""

"""


class StudentIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        # 如果大于等于最大索引,则停止迭代(索引不在增加)
        if self.__index >= len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


class StudentController:
    def __init__(self):
        self.__list_students = []

    def add_student(self, stu):
        self.__list_students.append(stu)

    def __iter__(self):
        return StudentIterator(self.__list_students)


controller = StudentController()
controller.add_student("程以宁")
controller.add_student("高家富")
controller.add_student("李杰")

# 遍历自定义对象
# for name in controller:
#     print(name) #

iterator = controller.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)  # 程以宁
        # 3. 停止循环获取
    except StopIteration:
        break
