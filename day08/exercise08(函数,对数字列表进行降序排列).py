"""
    参照day07/demo07.py
    定义函数,对数字列表进行降序排列.
    体会：
        # 1. 传入可变数据
        # 2. 修改可变数据
        # 3. 不用通过返回值,函数外也能得到修改后的结果
"""


# list01 = [43, 2, 45, 65, 76, 8, 9]
# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] < list01[c]:
#             list01[r], list01[c] = list01[c], list01[r]
# print(list01)

# 传入列表地址,函数内修改元素,所以不用通过返回值,函数外也可以得到排序后的结果
def descending_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]


list01 = [43, 2, 45, 65, 76, 8, 9]
descending_order(list01)
print(list01)
