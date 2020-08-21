"""
    跳转语句
    练习:exercise07
"""
# # 需求：累加1-100之间所有的数字
# sum_value = 0
# for number in range(1, 101):
#     sum_value += number
# print(sum_value)

# 需求：累加1-100之间能被3整除的数字
# sum_value = 0
# for number in range(1, 101):
#     # 思想：满足条件 累加
#     if number % 3 == 0:
#         sum_value += number
# print(sum_value)

# 1  2  3  4  5 ....
sum_value = 0
for number in range(1, 101):
    # 思想：不满足条件 跳过  否则 累加
    if number % 3 != 0:
        continue  # 跳过本次循环,继续下次循环
        # break # 跳出循环
    sum_value += number
print(sum_value)
