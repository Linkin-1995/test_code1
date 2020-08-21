# 练习:参照day02/exercise08
# 定义函数,根据重量(斤),计算几斤零几两.

# weight = int(input("请输入重量(两)："))
# jin = weight // 16
# liang = weight % 16
# print(str(jin) + "斤零" + str(liang) + "两")

def get_weight_of_jin_liang(weight):
    """

    :param weight:
    :return:
    """
    jin = weight // 16
    liang = weight % 16
    # 元组 (jin, liang)
    return jin, liang

weight = get_weight_of_jin_liang(100)
# print(weight)# (6, 4)
print("%d斤零%d两" % (weight[0], weight[1]))
print(f"{weight[0]}斤零{weight[1]}两")
