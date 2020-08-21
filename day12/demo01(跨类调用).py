"""
    跨类调用
    练习:exercise01~03
"""
# 需求:
# A 调用 B
# class A:
#     def func01(self):
#         pass
# class B:
#     def func02(self):
#         pass

# 做法1:直接创建对象
"""
class A:
    def func01(self):
        b = B() # 每次创建新
        b.func02()

class B:
    def func02(self):
        pass

a = A()
a.func01()
"""

# 做法2:在构造函数中创建对象
"""
class A:
    def __init__(self):
        self.b = B() # 创建A对象时创建B对象

    def func01(self):
        self.b.func02()

class B:
    def func02(self):
        pass

a = A()
a.func01()
"""

# 做法3:在类外创建对象
class A:
    def func01(self, b):# 通过参数调用
        b.func02()

class B:
    def func02(self):
        pass

a = A()
b = B()
a.func01(b)
