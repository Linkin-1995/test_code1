"""
    在终端中循环录入5个人的年龄,
    最后打印平均年龄(总年龄除以人数)
"""
sum_of_ages = 0
count_of_person = 5
for __ in range(count_of_person):  # 0 1 2 3 4
    age = int(input("请输入年龄："))
    sum_of_ages += age
# print("平均年龄是:" + str(sum_of_ages / count_of_person) + "岁")
print("平均年龄是:%d岁" % (sum_of_ages / count_of_person))
