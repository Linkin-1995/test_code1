# 练习１：在终端中录入５次数字，然后打印累加和.
# 练习２：在终端中录入数字,如果录入空字符串则停止录入,
# 	最后打印累加和.

# sum_value = 0
# # 不希望在循环体中使用循环变量,所以命名为双下划线.
# for __ in range(5):  # 0 1 2 3 4
#     number = int(input("请输入数字："))
#     sum_value += number
# print("累加结果:" + str(sum_value))

sum_value = 0
while True:
    number = input("请输入数字：")
    if number == "":
        break
    sum_value += int(number)
print("累加结果:" + str(sum_value))
