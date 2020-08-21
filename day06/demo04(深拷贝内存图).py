"""
    列表内存图
        深拷贝
    练习:exercise03

"""
# 准备深拷贝工具
import copy

list01 = [
    "a",
    ["b", "c"]
]
# 深拷贝，备份全部数据(两份)
list02 = copy.deepcopy(list01)
list01[0] = "A"  # 修改第一层
list01[1][0] = "B"  # 修改第二层
print(list02)  # ['a', ['b', 'c']]
