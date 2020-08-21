"""
    列表推导式
        语法：[对变量的操作 for 变量 in 容器 if 条件]
        适用性：根据其他容器构建列表
    练习:exercise06

"""
# 需求：将list01中大于5的数字,存入另外一个列表中list02
list01 = [3, 4, 5, 6, 7, 8, 9]
# list02 = []
# for item in list01:
#     if item > 5:
#         list02.append(item)
# print(list02)
list02 = [item for item in list01 if item > 5]
print(list02)

# 需求：将list01中所有元素增加10之后存入list03
# list03 = []
# for item in list01:
#     list03.append( item + 10 )
# print(list03)
list03 = [item + 10 for item in list01]
