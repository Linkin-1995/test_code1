"""
    在终端中录入一个疫情确诊人数,再录入一个治愈人数,
    打印治愈比例
    格式：治愈比例为xx%
"""
number_of_confirmed = int(input("请输入确诊人数："))
number_of_cure = int(input("请输入治愈人数："))
cure_ratio = number_of_cure / number_of_confirmed * 100
# 治愈比例为96.7741935483871%
print("治愈比例为" + str(cure_ratio) + "%")
