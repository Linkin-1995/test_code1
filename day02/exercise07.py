"""
    在终端中获取商品单价、购买的数量和支付金额。
    计算应该找回多少钱。
"""
price = float(input("请输入单价："))
count = float(input("请输入数量："))
money = float(input("请输入金额："))
change = money - price * count
print("应找回" + str(change) + "元")
