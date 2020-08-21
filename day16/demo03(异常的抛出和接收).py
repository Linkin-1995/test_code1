"""
    主动抛出异常：
        目的：快速传递错误消息
        做法：
            1. 抛出方:
                raise　XXXX(错误消息)
            2. 接收方:
                try:
                     ....
                except XXXX as e:
                     ....
    练习:创建敌人类,保障攻击力在0--100之间
        如果超过范围在终端中重新录入
"""


class Wife:
    def __init__(self, age):
        self.age = age  # 2.

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):  # 3.
        if 22 <= value <= 30:
            self.__age = value
        else:
            # 主动抛出异常
            raise Exception("我不要", "if 22 <= value <= 30", 1001)


# 接收
while True:
    try:
        age = int(input("请输入年龄："))
        w01 = Wife(age)  # 1.
        print(w01.age)
        break
    except Exception as e:
        print(e.args[0])
        print(e.args[1])
        print(e.args[2])

print("后续逻辑")
