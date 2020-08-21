# 练习:体会print函数参数

# 星号元组形参  , 命名关键字形参
# 实参数量无限 ,  关键字实参
# def print(*values, sep = " ", end="\n")
print()
print("你好")
# 　还可以打印多个数据
print(1, 2, 3)  # 1 2 3
# 还可以指定分隔符
print(1, 2, 3, sep="-")  # 1-2-3
print(1, 2, 3, sep="-", end=" ")  # 1-2-3
# print(1, 2, 3,"-"," ")# 1-2-3