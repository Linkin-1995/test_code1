"""
    创建图形管理器
        1. 记录多种图形（圆形、矩形....）
        2. 提供计算总面积的方法.
    满足：
        开闭原则、依赖倒置
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.
    写出具体体现：
        封装：GraphicManager、Circle、Rectanle
        继承：创建Graphic、隔离GraphicManager与Circle、Rectanle
        多态：GraphicManager调用Graphic,
             Circle、Rectanle重写get_area方法、
             创建Circle、Rectanle对象
        开闭原则：
            增加具体类型(三角形),图形GraphicManager不变
        依赖倒置
            GraphicManager使用Graphic,不使用Circle、Rectanle
        组合复用
            GraphicManager通过变量调用图形,而不是继承。
"""


class GraphicManager:
    def __init__(self):
        self.list_graphics = []

    def add_graphic(self, graphic):
        self.list_graphics.append(graphic)

    def calculate_total_area(self):
        total_area = 0
        for item in self.list_graphics:
            # 1. 编写代码时调用父
            total_area += item.get_area()
        return total_area


class Graphic:
    def get_area(self):
        pass


# -------------------

class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    # 2. 编写代码时子重写
    def get_area(self):
        return 3.14 * self.r


class Rectanle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w

# 测试
manager = GraphicManager()
# 3. 运行时创建子
manager.add_graphic(Circle(5))
manager.add_graphic(Rectanle(5, 6))
print(manager.calculate_total_area())
