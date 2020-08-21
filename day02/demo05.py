"""
    del
        删除变量
        引用计数
    练习:exercise04

"""
name01 = "悟空"
name02 = name01
name03 = "八戒"
# 删除变量
del name03,name01

# + 拼接后产生新数据
name04 = name02 + "唐僧"
del name02
print(name04) # "悟空唐僧"


