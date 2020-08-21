"""
    古代的秤，一斤十六两。
    在终端中获取两，计算几斤零几两。
"""
weight = int(input("请输入重量(两)："))
jin = weight // 16
liang = weight % 16
print(str(jin) + "斤零" + str(liang) + "两")
