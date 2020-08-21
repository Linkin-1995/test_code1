"""
    字典 -- 基础操作（完整版）
"""
# 创建
# 1. 创建
# -- 字典名称 = {键1: 值1,键2: 值2}
dict_wk_infos = {"name": "悟空", "sex": "男", "money": 500000}
# -- 字典名称 = dict(其他容器)
# 其他容器的格式要求：容器元素必须能够一分为二
#                 [(元素1,元素2),(元素3,元素4)]
# list01 = ["悟空",("猪","八戒"),["唐","三藏"]]
list01 = [("wk", "悟空"), ("bj", "猪八戒"), ("sf", "唐三藏")]
dict02 = dict(list01)  # {'wk': '悟空', 'bj': '猪八戒', 'sf': '唐三藏'}
print(dict02)

# 2. 添加  字典名称[键] = 值
# 字典中不存在当前键
if "age" not in dict_wk_infos:
    dict_wk_infos["age"] = 22

# 3. 定位  字典名称[键]
# 　字典中存在当前键
if "name" in dict_wk_infos:
    # -- 读取
    print(dict_wk_infos["name"])  # "悟空"
    # -- 修改
    dict_wk_infos["name"] = "孙悟空"

print(dict_wk_infos)

# 4. 删除
del dict_wk_infos["money"]
print(dict_wk_infos)

# 5. 遍历
# -- for 键 in 字典:
for key in dict_wk_infos:
    print(key)

# -- for 值 in 字典.values():
for value in dict_wk_infos.values():
    print(value)

# -- for 键,值 in 字典.items():
for key, value in dict_wk_infos.items():
    print(key)
    print(value)
