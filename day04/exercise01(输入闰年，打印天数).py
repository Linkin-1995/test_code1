# 练习:反复执行下列代码,输入y键继续。day03/exercise09
# year = int(input("请输入闰年："))
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# print(day)

while True:
    year = int(input("请输入闰年："))
    day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    print(day)
    # 输入的不是y键则退出
    if input("请输入y键继续：") != "y":
        break
