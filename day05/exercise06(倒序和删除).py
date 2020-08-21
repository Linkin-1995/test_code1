# 打印疫情地区列表所有元素(一行一个)
# 倒序打印新增人数列表(一行一个)
# 将现存人数列表大于100的元素设置为0


# 删除疫情地区列表中间元素
# 删除新增人数列表前两个元素
# 删除现存人数列表后两个元素
list_regions = ["北京", "香港", "上海"]
list_new_peoples = [1, 10, 0]
list_now_peoples = [324, 107, 24]

# 从头到尾读
for item in list_regions:
    print(item)
# 从尾到头读
for i in range(len(list_new_peoples)-1,-1,-1):
    print(list_new_peoples[i])
# 从头到尾改
# for item in list_now_peoples:
#     if item > 100:
#         item = 0 # 修改的是变量item,不是列表中元素.
for i in range(len(list_now_peoples)):
    if list_now_peoples[i] > 100:
        list_now_peoples[i] = 0 # 修改列表中元素


del list_regions[len(list_regions) // 2]
del list_new_peoples[: 2]
del list_now_peoples[-2:]
