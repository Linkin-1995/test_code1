"""
    列表list
    练习：exercise05 
"""
# 定位
list_names = ["杨鹏雨", "刘启玄", "张强"]
# -- 索引：定位单个元素
name = list_names[1]  # 读取第二个元素
list_names[1] = "老刘"  # 修改第二个元素

# -- 切片：定位多个元素
# -- 通过切片读取列表,会创建新列表
print(list_names[: 2])  # 读取前二个元素
# -- 通过切片修改列表,会遍历右侧容器,依次赋值给左侧定位的区域
list_names[: 2] = ["小雨", "小刘"]  # 修改前二个元素
print(list_names)
