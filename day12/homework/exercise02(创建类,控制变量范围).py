"""
    创建技能类(技能名称,攻击比率,消耗法力,持续时间)
                      0 - 2  0 - 80  0 - 120
           保证数据范围

    属性:将对实例变量的操作,改为对方法的操作.
              (为了逻辑判断)
"""


class Skill:
    def __init__(self, name="", atk_rate=0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration

    # 1. 创建属性对象 2. 绑定下面函数 property(读取函数)
    # 3. 将属性对象地址交给函数名称关联
    # atk_rate = property(读取函数)
    @property
    def atk_rate(self):
        return self.__atk_rate

    # 1. 调用属性的setter方法 2.绑定下面函数 atk_rate.setter(写入方法)
    # 3. 将属性对象地址交给函数名称关联
    # atk_rate = atk_rate.setter(写入方法)
    @atk_rate.setter
    def atk_rate(self, value):
        if 0 <= value <= 2:
            self.__atk_rate = value
        else:
            raise Exception("攻击比率不在范围内")

    @property
    def cost_sp(self):
        return self.__cost_sp

    @cost_sp.setter
    def cost_sp(self, value):
        if value < 0:
            self.__cost_sp = 0
        elif value > 80:
            self.__cost_sp = 80
        else:
            self.__cost_sp = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0 <= value <= 120:
            self.__duration = value
        else:
            raise Exception("持续时间不在范围内")


s01 = Skill("乾坤大挪移", 1, -10)
s01.atk_rate = 1
print(s01.atk_rate)
print(s01.cost_sp)
