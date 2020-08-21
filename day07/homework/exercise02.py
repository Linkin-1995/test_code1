"""
    将列表中的数字累减
        list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    结果：806400
"""
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]

# 循环前 -- 第一个元素
result = list02[0]
# 循环 -- 从第二个元素开始到末尾
for i in range(1, len(list02)):
    result -= list02[i]
print(result)
