"""
    列表
"""
list_names = ["杨鹏雨", "刘启玄", "张强"]
# 遍历
# -- for 变量 in 列表:
#       变量存储的是列表中记录的元素
#    适用性：从头到尾读取元素
for item in list_names:
    print(item)
# -- for 变量 in range(开始，结束，间隔):
#       变量存储的是整数(索引)
#       列表名[变量]才是列表中的元素

# len(list_names) - 1 : 从最大索引开始(总数-1)
# -1 : 到-1结束(实际不包含-1,只能取到0)
# -1 : 倒序
for i in range(len(list_names) - 1, -1, -1):  # 2 1 0
    print(list_names[i])

# 删除
# -- 根据元素  列表名.remove(元素)
list_names.remove("刘启玄")
# -- 根据定位  del 列表名[索引或者切片]
del list_names[1]
del list_names[-2:]
