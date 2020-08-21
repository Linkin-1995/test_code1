"""
    dict_hobbies = {
        "qtx": ["看书", "编码", "旅游"],
        "lzmly": ["刷抖音", "看电影"],
        "于谦": ["抽烟", "喝酒", "烫头"]
    }
    1) 打印"于谦"的第二个爱好
    2) 打印qtx所有爱好(一行一个)
    3) 打印所有人的所有爱好(一行一个)
"""
dict_hobbies = {
    "qtx": ["看书", "编码", "旅游"],
    "lzmly": ["刷抖音", "看电影"],
    "于谦": ["抽烟", "喝酒", "烫头"]
}
# 打印"于谦"的第二个爱好
print(dict_hobbies["于谦"][1])
# 打印qtx所有爱好(一行一个)
for hobbie in dict_hobbies["qtx"]:
    print(hobbie)
# 打印所有人的所有爱好(一行一个)
for hobbies in dict_hobbies.values():
    for hobbie in hobbies:
        print(hobbie)
