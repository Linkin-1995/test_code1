"""
    现实事物  --抽象-->  类  --具体-->   对象
                      (模板)

    类:对现实事物抽象后的产物
    对象:类别中具体的实例
"""
# 创建类
class Wife:
    """
        抽象的老婆概念
    """
    # 数据:姓名/财产/颜值....
    def __init__(self, name, money, face_score=90):
        self.name = name
        self.money = money
        self.face_score = face_score

    # 行为:工作...
    def work(self):
        print(self.name + "工作挣钱")


# 创建老婆对象(调用构造函数__init__函数)
jn = Wife("建宁", 1000000, 95)
# 点表示的,是一种包含的关系
jn.work()
