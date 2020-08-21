# 练习：
# 根据月日,计算是这一年的第几天.
# 公式：前几个月天数 + 当月天数
# 例如：5月10日
# 计算：31  29  31  30 + 10

month = int(input("请输入月份："))
day = int(input("请输入天："))
# 使用元组存储每月天数
days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 5
# days_of_month[0]
# days_of_month[1]
# days_of_month[2]
# days_of_month[3]
# total_days = 0
# # 累加前几个月的天数
# for i in range(month - 1):
#     total_days += days_of_month[i] 
total_days = sum(days_of_month[:month - 1])
# 累加当月的天数
total_days += day
print("%d月%d日是这一年的第%d天" % (month, day, total_days))
