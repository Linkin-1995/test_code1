"""
    参照day06/exercise08
       day03/exercise09
    定义函数,根据年月日计算是这一年的第几天
    要求:增加年份的判断
"""


# year = int(input("请输入闰年："))
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# print(day)
#
# month = int(input("请输入月份："))
# day = int(input("请输入天："))
# days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_days = sum(days_of_month[:month - 1])
# total_days += day
# print("%d月%d日是这一年的第%d天" % (month, day, total_days))

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_total_days(year,month, day):
    day_of_month02 = 29 if is_leap_year(year) else 28
    days_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_days = sum(days_of_month[:month - 1])
    total_days += day
    return total_days

print(get_total_days(2020, 2, 5))