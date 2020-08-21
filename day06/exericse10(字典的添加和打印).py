# 练习1：
# 创建字典存储北京疫情信息(地区/新增/现有)
# 创建字典存储香港疫情信息(地区/新增/现有)
# 创建字典存储上海疫情信息(地区/新增/现有)
dict_bj_infos = {"region": "北京", "new": 0, "now": 320}
dict_hk_infos = {"region": "香港", "new": 17, "now": 121}
dict_sh_infos = {"region": "上海", "new": 2, "now": 23}

# 练习2：
# 为以上3个字典添加si亡人数
dict_bj_infos["death"] = 9
dict_hk_infos["death"] = 7
dict_sh_infos["death"] = 7

# 练习3：
# 以固定格式,打印字典信息.
# 格式：xx地区新增xx人,现有xx人,死亡xx人.
print("%s地区新增%d人,现有%d人,死亡%d人." % (dict_bj_infos["region"], dict_bj_infos["new"], dict_bj_infos["new"], dict_bj_infos["death"]))
print("%s地区新增%d人,现有%d人,死亡%d人." % (dict_hk_infos["region"], dict_hk_infos["new"], dict_hk_infos["new"], dict_hk_infos["death"]))
print("%s地区新增%d人,现有%d人,死亡%d人." % (dict_sh_infos["region"], dict_sh_infos["new"], dict_sh_infos["new"], dict_sh_infos["death"]))
