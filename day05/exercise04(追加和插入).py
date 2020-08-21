"""
    练习1:
        创建疫情地区列表
        创建新增人数列表
        创建现有人数列表
        要求：存储３个元素
    练习2:
        为以上三个列表追加第四个元素
        为以上三个列表在第二个位置上插入甘肃信息
"""
# 列表名 = [元素1...]
list_regions = ["北京", "香港", "上海"]
list_new_peoples = [1, 10, 0]
list_now_peoples = [324, 107, 24]

# 列表名.append(元素1)
list_regions.append("四川")
list_new_peoples.append(0)
list_now_peoples.append(12)

# 列表名.insert(索引,元素)
list_regions.insert(1,"甘肃")
list_new_peoples.insert(1,0)
list_now_peoples.insert(1,11)

