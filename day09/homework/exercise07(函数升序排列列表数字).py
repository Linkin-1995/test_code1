"""
    定义函数,对列表进行生序排列
    list01 = [170, 160, 180, 165]
"""
def ascending_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                # 修改可变对象
                list_target[r], list_target[c] = list_target[c], list_target[r]

# 传入可变对象
list01 = [170, 160, 180, 165]
ascending_order(list01)
print(list01)# [160, 165, 170, 180]

# print(ascending_order(list01))# None
