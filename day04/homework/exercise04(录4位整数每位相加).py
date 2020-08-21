"""
    在终端中录入一个4位整数, 打印每位相加和
    例如：1234 -->  1 + 2+ 3 + 4
         结果是：10
"""
number = int(input("请输入4位整数："))
# 计算个位
result = number % 10
# 累加十位
result += number // 10 % 10
# 累加百位
result += number // 100 % 10
# 累加千位
result += number // 1000
print(result)
