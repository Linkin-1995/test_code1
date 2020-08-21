"""
    练习1: 创建三个字典, 存储前三个地区疫情信息
           (地区, 新增, 现有, 累计, 治愈)
    练习2: 为以上三个字典, 添加si亡信息
    练习3: 删除第一个字典的新增人数,
    练习4: 将第二个字典的新增人数设置为0,
    练习5: 打印第三个字典信息:
        格式: xx新增xx, 现有xx, 累计xx, 治愈xx, si亡xx
    练习6: 将第三个字典中所有值为0的键打印出来
"""
dict_bj_infos = {"region": "北京", "new": 0, "now": 307, "total": 929, "cure": 613}
dict_hk_infos = {"region": "香港", "new": 14, "now": 131, "total": 1299, "cure": 1161}
dict_sh_infos = {"region": "上海", "new": 0, "now": 23, "total": 718, "cure": 688}

dict_bj_infos["death"] = 9
dict_hk_infos["death"] = 7
dict_sh_infos["death"] = 7

del dict_bj_infos["new"]

dict_hk_infos["new"] = 0

print("%s新增%d, 现有%d, 累计%d, 治愈%d, si亡%d" % (
    dict_sh_infos["region"], dict_sh_infos["new"],
    dict_sh_infos["now"], dict_sh_infos["total"],
    dict_sh_infos["cure"], dict_sh_infos["death"]))

for key, value in dict_sh_infos.items():
    if value == 0:
        print(key)
