# 练习：
# 说出下列代码表达的命题
# 	print(666 == "666")
# 	print(input("你爱我吗? ") == "爱")
# 	print(float(input("请输入你的身高：")) > 170)
# 根据命题写出代码
# 	输入的是正数
# 	输入的是月份
# 	输入的不是偶数

# # 命题：整数666 等于 字符串666
# print(666 == "666") # False
# # 命题：你爱我
# print(input("你爱我吗? ") == "爱")
# # 命题：你的身高大于170
# print(float(input("请输入你的身高：")) > 170)


print(float(input("请输入数字：")) > 0)
print(1 <= int(input("请输入月份：")) <= 12)
# 输入的是偶数
print(int(input("请输入数字：")) % 2 == 0)
# 输入的不是偶数
print(int(input("请输入数字：")) % 2 != 0)