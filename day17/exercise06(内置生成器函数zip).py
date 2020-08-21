# 矩阵转置
map = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# 1. 从map中获取4个(行)元素,交给zip处理
for item in zip(map[0],map[1],map[2],map[3]):
    print(item)
# 2. 如果map行列数量未知
for item in zip(*map): # 拆
    print(item)
# 3. 结果应该还是列表嵌套列表
# list_map = []
# for item in zip(*map): # 拆
#     list_map.append(list(item))
list_map = [list(item) for item in zip(*map)]
print(list_map)
