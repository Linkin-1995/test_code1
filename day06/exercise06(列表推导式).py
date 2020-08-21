#    练习：
# 使用列表推导式生成1--50之间能被3或者5整除的数字
# 使用列表推导式生成5 -- 100之间的数字平方
# list_result01 = []
# for number in range(1,51):
#     if number % 3 == 0 or number % 5 == 0:
#         list_result01.append(number)
list_result01 = [number for number in range(1, 51) if number % 3 == 0 or number % 5 == 0]
print(list_result01)

list_result02 = [item ** 2 for item in range(5, 101)]
print(list_result02)
