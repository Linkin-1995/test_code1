"""
    1. 在终端中录入一个整数，
        如果是奇数为变量state赋值"奇数", 否则赋值"偶数"。
    2. 在终端中录入一个年份，
        如果是闰年为变量day赋值29, 否则赋值28。
        闰年：年份能被4整除但是不能被100整除
             年份能被400整除
"""
# if int(input("请输入整数：")) % 2 != 0:
#     state = "奇数"
# else:
#     state = "偶数"

# if int(input("请输入整数：")) % 2:
#     state = "奇数"
# else:
#     state = "偶数"

# state = "奇数" if int(input("请输入整数：")) % 2 else "偶数"


year = int(input("请输入闰年："))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     day = 29
# else:
#     day = 28
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(day)
