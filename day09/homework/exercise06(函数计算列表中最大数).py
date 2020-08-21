"""
    定义函数,获取列表中最大的数字
    list01 = [170, 160, 180, 165]
    max_value = list01[0]
    for i in range(1, len(list01)):
        if max_value < list01[i]:
            max_value = list01[i]
    print(max_value)
"""


def get_max(list_target):
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        if max_value < list_target[i]:
            max_value = list_target[i]
    return max_value


print(get_max([170, 160, 180, 165]))
