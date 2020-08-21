# 练习1：在终端中录入一个内容,循环打印每个文字的编码值。
# 练习2：循环录入编码值,打印文字.直到输入空字符串,停止。
# https://unicode-table.com/cn/#4F26

# for item in input("请输入内容："):
#     print(ord(item))

while True:
    code_value = input("请输入编码值：")
    if code_value == "":
        break
    print(chr(int(code_value)))
