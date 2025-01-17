# 练习:
# 请排列出2个色子可以组合的所有数字
# 每个色子数字1—6，可以使用range(1,7)表达
# list_result = []
# for x in range(1, 7):  # 1             2
#     for y in range(1, 7):  # 123456   123456
#         list_result.append((x, y))
# print(list_result)

list_result = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(list_result)

# 请排列出3个色子可以组合的所有数字
# 每个色子数字1—6，可以使用range(1,7)表达
# list_result = []
# for x in range(1, 7):  #             1                          2
#     for y in range(1, 7):  # 1              2     ...  6
#         for z in range(1, 7):  # 123456   123456     123456
#             list_result.append((x, y,z))
# print(list_result)

list_result = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
print(list_result)
