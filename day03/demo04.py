"""
    逻辑运算符
        判断命题之间的关系
        与and:
            并且      所有条件都得满足
        或or
            或者     满足一个条件就行
        非not
            取反
        短路逻辑：一但结果确定，后面的语句将不再执行。
            价值：尽量将耗时的判断,放在后面完成.
    练习:exercise02
"""
# 来自于丈母娘的灵魂质问：
# 命题： 有钱  又  有房
# 有钱 and 有房
# print(float(input("请输入你的财产：")) > 100000 and input("请输入你是否有房产：") == "有")
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# 命题： 有钱  或  有房
# 有钱 or 有房
print(float(input("请输入你的财产：")) > 100000 or input("请输入你是否有房产：") == "有")
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

print(not True) # False
print(not False) # True