"""
    内置生成器
        enumerate 遍历可迭代对象同时获取索引
"""
list01 = [4, 14, 5, 6, 78, 9]
# for i in range(len(list01)):
#     if list01[i] > 10:
#         list01[i] = 10

# 元组(索引,元素)
# for item in enumerate(list01):
#     print(item)

for i, item in enumerate(list01):
    if item > 10:
        list01[i] = 10
print(list01)
