"""
    列表list
    练习：exercise04

"""
# 1. 创建
#  -- 列表名 = [元素1,元素2,元素3]
list_names = ["杨鹏雨","刘启玄","张强"]
# -- 列表名 = list(其他容器)
list01 = list("孙悟空") # str --> list

# 2. 添加
# -- 追加  列表名.append(元素)
list_names.append("李肇阳")
list_names.append("闫沛文")
# -- 插入  列表名.insert(索引,元素)
list_names.insert(0,"贺有朋")
list_names.insert(2,"闫思序")