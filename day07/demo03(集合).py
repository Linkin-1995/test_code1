"""
   集合set　-　基础操作
        作用：去重复
"""
# 1. 创建
# -- 集合名 = {元素1, 元素2, 元素3}
# set01 = {} # 是字典,不是集合
set01 = {101, 102, 103}
# -- 集合名 = set(其他容器)
list01 = ["a", "b", "b", "b", "c"]
set02 = set(list01)
print(set02)

# 2. 添加  集合名.add(元素)
set01.add(104)
set01.add(104)
print(set01) # {104, 101, 102, 103}

# 3. 定位(没有)

# 4. 删除
# 集合名.remove(元素)
# 集合名.discard(元素)
# set01.remove(108) #　如果没有则报错
set01.discard(108)#　如果没有不会报错

# 5. 遍历
# -- for 变量 in 集合名:
for item in set01:
    print(item)




