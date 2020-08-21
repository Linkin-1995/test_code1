"""
    字典推导式
        字典名称 = {键:值 for 变量 in 容器 if 条件}
    练习:exercise02
"""
# 复习:列表推导式
list01 = [4, 4, 5, 6, 7, 7, 8, 9]
# list_result = []
# for item in list01:
#     if item % 2:
#         list_result.append(item)
# print(list_result)
list_result = [item for item in list01 if item % 2]

# dict_result = {}
# for number in range(1, 11):  # １　～　１０
#     dict_result[number] = number ** 2
dict_result = {number: number ** 2 for number in range(1, 11)}
print(dict_result)

# dict_result = {}
# for number in range(1, 11):  # １　～　１０
#     if number % 2:
#         dict_result[number] = number ** 2
dict_result = {number: number ** 2 for number in range(1, 11) if number % 2}
print(dict_result)
