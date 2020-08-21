# 练习:参照day03/exercise06
# 定义函数,根据心理年龄与实际年龄,计算智商等级。
# ma = int(input("请输入心理年龄："))
# ca = int(input("请输入实际年龄："))
# iq = ma / ca * 100
# # 连续区间只需要判断单边(不用判断两端)
# if iq >= 140:
#     print("天才")
# elif iq >= 120:
#     print("超常")
# elif iq >= 110:
#     print("聪慧")
# elif iq >= 90:
#     print("正常")
# elif iq >= 80:
#     print("迟钝")
# else:
#     print("低能")

# def get_iq_level(ma, ca):
#     iq = ma / ca * 100
#     if iq >= 140:
#         return "天才"
#     elif iq >= 120: # 如果前面return,那么当前代码不能执行.所以elif 可以改为if
#         return "超常"
#     elif iq >= 110:
#         return "聪慧"
#     elif iq >= 90:
#         return "正常"
#     elif iq >= 80:
#         return "迟钝"
#     else:
#         return "低能"

def get_iq_level(ma, ca):
    iq = ma / ca * 100
    if iq >= 140:  # 如果满足条件,返回结果,退出函数
        return "天才"
    if iq >= 120:
        return "超常"
    if iq >= 110:
        return "聪慧"
    if iq >= 90:
        return "正常"
    if iq >= 80:
        return "迟钝"
    return "低能"  # 如果以上条件都不满足,执行本行


level = get_iq_level(25, 20)
print(level)
