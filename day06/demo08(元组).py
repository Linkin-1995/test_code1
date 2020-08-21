"""
    元组 tuple
    面试： Python有哪些数据类型?
    答： 有两种
        第一种是不可变数据类型,采用按需分配的存储机制,例如 int  float  str...
                               (节省空间)
        另外一种是可变数据类型，采用预留空间的存储机制,例如 list
                              (操作方便)
    练习:exercise07~09

"""
# 1. 创建
# -- 元组名 = (元素1, 元素2, 元素3)
tuple01 = (10, 20, 30)
list02 = ["a", "b", "c"]
# -- 元组名 = tuple(其他容器)
tuple02 = tuple(list02)

# 2. 定位
# -- 索引 元组名[整数]
print(tuple01[0])  # 获取第一个元素
# -- 切片 元组名[开始:结束:间隔]
#    备注：创建新元组
print(tuple01[-2:])

# 3. 遍历
# 依次 获取 全部 元素
# -- for 变量 in 元组名:
for item in list02:
    print(item)
# -- for 变量 in range():
for i in range(len(list02) - 1, -1, -1):
    print(list02[i])

# 4.特殊：
# -- 小括号可以省略
tuple03 = "a", "b"
# -- 拆包    变量1,变量2  =  容器
data01, data02 = (10, 20)
data01, data02 = "ab"
data01, data02 = [10, 20]
print(data01)
print(data02)
# -- 如果元组中只有一个元素,必须添加逗号
tuple04 = (10,)
print(type(tuple04))
