"""
    练习:参照day04/homework/exercise03案例,
    定义函数,计算折扣。
    account_type = input("请输入账户类型：")
    money = float(input("请输入消费金额："))
    if account_type == "vip":
        if money < 500:
            print("享受85折扣")
        else:
            print("享受8折扣")
    else:
        if money > 800:
            print("享受9折扣")
        else:
            print("原价购买")
"""

# 注意:返回的折扣应该是数字(比例)
def calculate_discount(account_type, money):
    if account_type == "vip":
        return 0.85 if money < 500 else 0.8
    return 0.9 if money > 800 else 1


print(calculate_discount("vip", 800))
