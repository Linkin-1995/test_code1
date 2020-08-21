"""
    读取疫情地区列表中间元素
    读取新增人数列表前两个元素
    读取现存人数列表后两个元素

    修改疫情地区列表最后一个元素 "sh"
    修改新增人数列表前两个元素　设置为0
    修改现存人数列表后两个元素  100, 20
"""
list_regions = ["北京", "香港", "上海"]
list_new_peoples = [1, 10, 0]
list_now_peoples = [324, 107, 24]

# 列表名[整数]
print(list_regions[len(list_regions) // 2])
# 列表名[:结束索引]
print(list_new_peoples[:2])
# 列表名[开始索引:]
print(list_new_peoples[-2:])

list_regions[-1] = "sh"
list_new_peoples[:2] = [0,0]
list_now_peoples[-2:] = [100,20]
print(list_now_peoples)
