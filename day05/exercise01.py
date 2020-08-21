# 练习：
# 1.在终端中获取一个整数，在一行打印星号*
# 2.在终端中获取一个整数，作为边长，打印矩形。
# print("*%s*" % (" " * (number - 2)))
number = int(input("请输入整数："))  # 5
# 打印头
# print("*" * number)
# 打印中间
# for __ in range(number - 2):
#     # *   *
#     print("*" + " " * (number - 2) + "*")
# 打印尾
# print("*" * number)

for item in range(number):  # 0 1 2 3 4
    if item == 0 or item == number - 1:
        print("*" * number)  # 打印头尾
    else:
        print("*" + " " * (number - 2) + "*")  # 打印中间
