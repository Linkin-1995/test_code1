# 练习：
# 年龄大于25 并且 身高小于170
# 职位是高管 或者 年薪大于500000
# 身高大于180 并且 财产大于10000000 或者 颜值大于95
# 体会：短路逻辑

# print(int(input("请输入年龄：")) > 25 and float(input("请输入身高：")) < 170)
# print(input("请输入职位：") == "高管" or float(input("请输入年薪：")) > 500000)
print(float(input("请输入身高：")) > 180 and float(input("请输入财产：")) > 10000000 or int(input("请输入颜值：")) > 95)

重点！！！
input要被and或者or链接起来  否则不执行短路逻辑
