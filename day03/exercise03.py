# 练习：满足条件嫁给你,否则去学习
# 1. 年龄大于25 并且 身高小于170
# 2. 职位是高管 或者 年薪大于500000
# 3. 身高大于180 并且 财产大于10000000 或者 颜值大于95

if int(input("请输入年龄：")) > 25 and float(input("请输入身高：")) < 170:
    print("嫁给你")
else:
    print("去学习")

if input("请输入职位：") == "高管" or float(input("请输入年薪：")) > 500000 :
    print("嫁给你")
else:
    print("去学习")

if float(input("请输入身高：")) > 180 and float(input("请输入财产：")) > 10000000 or int(input("请输入颜值：")) > 95:
    print("嫁给你")
else:
    print("去学习")