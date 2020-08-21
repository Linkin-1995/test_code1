# 练习:
# 字符串： content = "我是京师监狱狱长金海。"
# 打印第一个字符、打印最后一个字符、打印中间字符
# 打印第三个字符、打印倒数第五个字符
# 命题：金海在字符串content中
# 命题：京师监狱不在字符串content中
content = "我是京师监狱狱长金海。"
print(content[0])
print(content[-1])
print(content[len(content) // 2])
print(content[2])
print(content[-5])
print("金海" in content)  # True
print("京师监狱" not in content)  # False
