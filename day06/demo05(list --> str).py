"""
    list --> str
	将多个字符串拼接为一个。
	字符串 = "连接符".join(列表)
    练习:exercise04

"""
# 需求：根据xx逻辑,拼接字符串.
# result = ""
# for number in range(10):  # 0~9
#     # 缺点：每次循环,创建新字符串,之前的字符串成为垃圾
#     result += str(number)
# print(result)

# 解决：用可变对象替代不可变对象
list_result = []
for number in range(10):  # 0~9
    # 在原有列表基础上增加
    list_result.append(str(number))
# 将列表中多个元素连接为一个字符串
str_result = "".join(list_result)
print(str_result)

