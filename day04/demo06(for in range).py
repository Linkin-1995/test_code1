"""
    for 变量 in range():
        循环体
    练习:exercise06
"""
# 写法1：range(开始, 结束, 间隔)
#       不包含结束值
for number in range(0, 5, 1):  # 0 1 2 3 4
    print(number)

# 写法2：range(开始, 结束)
#       间隔默认为1
for number in range(0, 5):  # 0 1 2 3 4
    print(number)

# 写法3：range(结束)
#       开始默认为0
for number in range(5):  # 0 1 2 3 4
    print(number)
