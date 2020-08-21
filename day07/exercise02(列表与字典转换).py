# 练习1：将两个列表，合并为一个字典
# 		姓名列表["张无忌","赵敏","周芷若"]
# 		房间列表[101,102,103]
# 练习2：颠倒练习1字典键值
list_names = ["张无忌", "赵敏", "周芷若"]
list_rooms = [101, 102, 103]
#1.
# dict_result = {}
# for i in range(len(list_names)):  # 0  1  2
#     dict_result[list_rooms[i]] = list_names[i]
dict_result01 = {list_rooms[i]: list_names[i] for i in range(len(list_names))}
print(dict_result01)

#2.
dict_result02 = {v: k for k, v in dict_result01.items()}
print(dict_result02)


#字典变列表
dict={'wk': '悟空', 'bj': '猪八戒', 'sf': '唐三藏'}
list=[]
for key,value in dict.items():
    list.append((key,value))
print(list)
[('wk', '悟空'), ('bj', '猪八戒'), ('sf', '唐三藏')]









