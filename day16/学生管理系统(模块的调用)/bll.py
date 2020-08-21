class StudentController:
    """
        逻辑控制器：负责处理业务逻辑(存储/查询)
    """

    def __init__(self):
        self.__list_students = []
        # 重命名：shift+f6
        self.__start_sid = 1001

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu_target):
        # 设置学生的编号(自增长)
        stu_target.sid = self.__start_sid
        self.__start_sid += 1
        self.__list_students.append(stu_target)

    def remove_student(self, sid):
        """
            移除学生
        :param sid:int类型的学生编号
        :return:是否移除成功
        """
        for stu in self.__list_students:
            if stu.sid == sid:
                self.__list_students.remove(stu)
                return True  # 删除成功

        return False  # 删除失败

    def modify(self, stu_target):
        for stu in self.__list_students:
            if stu.sid == stu_target.sid:
                # stu = stu_target # 错误:改栈帧变量
                # 正确：改学生信息
                stu.name = stu_target.name
                stu.age = stu_target.age
                stu.score = stu_target.score
                return True
        return False

        # 错误：改列表变量
        # for i in range(len(self.__list_students)):
        #     if self.__list_students[i].sid == stu_target.sid:
        #         self.__list_students[i] = stu_target