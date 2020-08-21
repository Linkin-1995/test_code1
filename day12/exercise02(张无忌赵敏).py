"""
    使用面向对象思想,描述下列情景
        张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
    张无忌与赵敏属于数据不同 -- 使用对象区分
"""


# 如果需求如下,需要单独创建教/工作类
# 张无忌 教xxx
#       工作
#       ....
# 赵敏  工作
#       ....

class Person:
    def __init__(self, name):
        self.name = name

    def work(self, money):
        print("张无忌工作挣了%d元" % money)

    def teach(self, other, skill):
        print("%s教%s%s" % (self.name, other.name, skill))


zwj = Person("张无忌")
zm = Person("赵敏")
zwj.work(5000)
zm.work(10000)
zwj.teach(zm, "九阳神功")
zm.teach(zwj, "玉女心经")
