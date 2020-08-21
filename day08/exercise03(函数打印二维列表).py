# 练习:
# list01 = [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
# ]
# 1	 2	3	4
# 5	 6	7	8
# 9	 10	11	12

def print_two_dimensional_list(list_target):
    """
        打印二维列表
    :param list_target:
    :return:
    """
    for line in list_target:
        for item in line:
            print(item, end="\t")
        print()


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print_two_dimensional_list(list01)
