"""
    while 循环 - 死循环
        语法：
            while True:
                循环体
                if 退出条件:
                    break
        作用：
            延长程序的生命周期
        练习:exercise01
"""

# 死循环
while True:
    sex = input("请输入性别：")
    if sex == "男":
        print("您好,先生")
    elif sex == "女":
        print("您好,女士")
    else:
        print("性别未知")

    if input("请输入q键退出：") == "q":
        break # 跳出循环

