"""
    学生信息管理系统
"""


class StudentModel:
    """
        数据模型：封装数据
    """

    def __init__(self, name="", age=0, score=0.0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 学生编号(全球唯一标示符)
        self.sid = sid

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise Exception("成绩有误")


class StudentView:
    """
        界面视图：负责处理界面逻辑(input/print)
    """

    def __init__(self):
        # 对象.实例变量 = 类名()
        self.controller = StudentController()

    def display_menu(self):
        print("1) 获取学生信息")
        print("2) 显示学生信息")
        print("3) 删除学生信息")
        print("4) 修改学生信息")

    def select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            # 对象.实例方法()
            self.input_student()

    def input_student(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))
        stu = StudentModel(name, age, score)
        # 对象.实例变量.实例方法(参数)
        self.controller.add_student(stu)


class StudentController:
    """
        逻辑控制器：负责处理业务逻辑(存储/查询)
    """

    def __init__(self):
        self.list_students = []
        self.start_sid = 1001

    def add_student(self, stu_target):
        # 设置学生的编号(自增长)
        stu_target.sid = self.start_sid
        self.start_sid += 1
        self.list_students.append(stu_target)


view = StudentView()
while True:
    view.display_menu()
    view.select_menu()
