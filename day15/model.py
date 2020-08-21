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