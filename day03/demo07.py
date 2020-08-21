"""
    if 真值表达式
    bool转换
        数据表示空(没值)结果为False
        bool(数据) 
"""
# 转换结果为False
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))  # None 表示空

if 10:  # bool(10)
    print("ok")
else:
    print("no")

content = input("请输入：")
# 如果没有输入内容
# if content != "":
if content:  # bool(content)
    print("您输入了:" + content)
else:
    print("您没有输入")
