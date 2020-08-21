"""
    模块(文件)
        程序结构清晰
        利于多人开发

    快捷键：
        正确写出需要导入的成员
        alt + 回车 --> import this name

    练习：将day15/infos_system.py拆分为4个模块
        将StudentModel类定义在model.py中
        将StudentController类定义在bll.py中
            业务business 逻辑logic 层layer
        将StudentView类定义在usl.py中
            用户user 显示show 层layer
        将入口代码定义在main.py中
"""
# 标记当前文件夹为根目录
# 在当前文件夹中右键 --> Mark Director as --> Sources Root

# ------------导入语句--------------
# 方式1
# 语法：import 文件名
# 使用：文件名.成员
# 本质：使用变量关联模块地址
# 适用性：面向过程的成员(全局变量、函数)
import module01

# ------------当前模块代码--------------
#
# print(module01.g01)
module01.func01()
# m01 =module01. MyClass(10)
# print(m01.data)

# 方式2
# 语法：from 文件名 import 成员名
# 使用：通过成员名调用
# 本质：将成员导入到当前模块作用域中
# 小心：多个模块中有相同成员会冲突(覆盖)
# 适用性：面向对象的成员(类)


# from module01 import g01
# from module01 import func01
# print(g01)
# func01()

# print(g01)
# func01()

from module01 import *

def func01():
    print("demo01 -- func01")

func01()
