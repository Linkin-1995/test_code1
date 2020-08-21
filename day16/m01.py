"""
    m01 模块
"""
print("我是谁？",__name__)


def func01():
    """
        func01函数
    """
    print("func01")

# 以单下划线开头 - 隐藏成员
# 只适用于from xx import *
def _func02():
    print("func02")
