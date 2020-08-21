"""
    复习 - 函数参数
        实际参数:与形参进行对应
            位置实参:按顺序
                序列实参:拆
            关键字实参:按名字
                字典实参:拆

        形式参数:约束实参传递方式
            默认形参:可选
"""


# 语法:
# 默认形参:def 函数名(形参名1=默认值,形参名2=默认值):
# 适用性:允许实参不传递信息式
def func01(p1=0, p2=0, p3=0):
    pass


# 位置实参 :函数名(数据1,数据2,数据3)
# 价值:最常用的为形参传递数据方式
# 适用性:传递全部数据
func01(1, 2, 3)

# 关键字实参 :函数名(形参名1=数据1,形参名2=数据2)
# 价值:指定名称传递(屏蔽其他参数)
# 适用性:传递部分数据
func01(p3=3)

# 序列实参 :函数名(*序列)
# 价值:将实参构建过程交给容器统一管理(在其他地方创建)
# 适用性:形参过于复杂,需要使用容器统一管理
list01 = [1, 2, 3]
func01(*list01)

# 序列实参 :函数名(*序列)
# 价值与适用性同上
dict01 = {"p1": 1, "p3": 3, "p2": 2}
func01(**dict01)