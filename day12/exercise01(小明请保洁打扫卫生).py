"""
    使用面向对象思想,描述下列情景
        小明请保洁打扫卫生
    要求:使用3中调用方式,体会差异.
    参照day11/exercise07
"""


# 1. 为什么创建类?  -- 有行为需要承担,具有独立变化点
#     小明 --> 请/预约/通知
#     保洁 --> 打扫

# 写法1:小明每次通知新保洁打扫卫生
# class Client:
#     def __init__(self,name):
#         self.name = name
#
#     def notify(self):
#         print("通知保洁")
#         c = Cleaner()
#         c.cleaning()
#
# class Cleaner:
#     def cleaning(self):
#         print("打扫卫生")
#
# xm = Client("小明")
# xm.notify()


# 写法2:小明每次通知自己的保洁打扫卫生
# class Client:
#     def __init__(self,name):
#         self.name = name
#         self.cleaner = Cleaner()
#
#     def notify(self):
#         print("通知保洁")
#         self.cleaner.cleaning()
#
# class Cleaner:
#     def cleaning(self):
#         print("打扫卫生")
#
# xm = Client("小明")
# xm.notify()

# 写法3:小明通过参数调用保洁
class Client:
    def __init__(self, name):
        self.name = name

    def notify(self, cleaner):#小明与保洁的关系最为灵活
        print("通知保洁")
        cleaner.cleaning()


class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)
