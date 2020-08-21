#  练习:在终端中录入一个整数, 打印每位相加和。
number = input("请输入一个整数：")
result = 0  # 在循环前创建用于存储累加和的变量
for item in number:
    # "1234" --> "1" --> 1
    result += int(item) # 在循环中进行累加
print("累加和是:" + str(result))#  在循环后查看结果
