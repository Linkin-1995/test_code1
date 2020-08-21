"""
    函数式编程 - 语法
        理论支柱:函数可以赋值给变量，赋值后变量绑定函数
        应用:函数赋值给参数
"""


def func01():
    print("func01执行了")

# 将函数返回值赋值给变量(None)
# a = func01()
# 将函数地址赋值给变量
a = func01
# 通过变量调用函数
a()

def func02():
    print("func02执行了")


# b 可以理解为一个钩子
def func03(b):
    print("func03执行了")
    b() # 拉钩子(执行传入的函数)

# 价值:func03可以和其他函数结合(灵活)
func03(  func01  )
func03(  func02  )