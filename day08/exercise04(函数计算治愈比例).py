"""
    参照day02/exercise06
    定义函数,计算治愈比例.
"""

# number_of_confirmed = int(input("请输入确诊人数："))
# number_of_cure = int(input("请输入治愈人数："))
# cure_ratio = number_of_cure / number_of_confirmed * 100
# # 治愈比例为96.7741935483871%
# print("治愈比例为" + str(cure_ratio) + "%")

def calculate_cure_ratio(number_of_confirmed, number_of_cure):
    cure_ratio = number_of_cure / number_of_confirmed * 100
    return cure_ratio


cure_ratio = calculate_cure_ratio(100, 96)
# print("治愈比例为%d%%"%cure_ratio)
print(f"治愈比例为{cure_ratio}%")
