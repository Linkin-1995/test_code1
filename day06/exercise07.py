# 以容器（统一管理数据）的思想修改下列代码

month = int(input("请输入月份："))
# if 1 <= month <= 12:
#     if month == 2:
#         print("28天")
#     # elif month == 4 or month == 6 or month == 9 or month == 11:
#     elif month in (4, 6, 9, 11):
#         print("30天")
#     else:  # 1 3 5 7 8 10 12
#         print("31天")
# else:
#     print("月份有误")

# 使用元组存储每月天数
days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(days_of_month[month - 1])