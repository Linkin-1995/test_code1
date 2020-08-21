"""
    因为在项目中处处需要使用通用函数find
    所以将通用函数统一存储在Common包的iterable_tools模块中
    最后在项目中导入模块,通过类名访问静态方法(通用函数)
"""

from common.iterable_tools import IterableHelper

list01 = [3, 443, 4, 54, 6]


def condition01(item):
    return item > 10


def condition02(item):
    return item < 5


# def find(condition):
#     for item in list01:
#         if condition(item):
#             yield item
#
# for item in find(condition01):
#     print(item)


for item in IterableHelper.find_all(list01, condition01):
    print(item)
