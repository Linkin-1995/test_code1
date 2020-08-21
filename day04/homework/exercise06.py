"""
    在终端中获取两个数字，交换后再输出来。
"""
number01 = input("请输入第一个数字：")
number02 = input("请输入第二个数字：")
number01, number02 = number02, number01
print("第一个数字是：" + number01)
print("第二个数字是：" + number02)
