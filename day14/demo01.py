"""
    面向对象 - 主体知识
        字面意思:考虑问题从对象的的角度出发
        步骤：
            1. 识别对象  找人
            2. 分配职责  干嘛
            3. 建立交互  协作

        特征：
            1. 封装：分 - 变化
            2. 继承：隔 - 变化
            3. 多态：做 - 变化(功能)

        原则：
            1. 开闭原则 - 目标
            2. 单一职责 - 对封装的补充
            3. 依赖倒置 - 引出继承
            4. 组合复用 - 继承是抽象变化,不是代码复用.
"""
# 多继承：
class A:
    def func01(self):
        print("A -- func01")

class B(A):
    def func01(self):
        print("B -- func01")
        # 因为是 D 类型对象，所以调用了C,而不是A
        super().func01()

class C(A):
    def func01(self):
        print("C -- func01")
        super().func01()

class D(B,C):
    def func01(self):
        print("D -- func01")
        # 调用继承列表第一个
        super().func01()

d = D()
d.func01()

# 同名方法解析顺序：调用同名方法的查找顺序
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())