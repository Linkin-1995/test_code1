"""
    列表内存图
        读取
    练习:exercise01
"""
data01 = ["a", "b"]
data02 = data01
data03 = data01[0]
data04 = data01[:]

data01[0] = "A"
print(data04[0])  # a

data02[1] = "B"
print(data01[1])  # B
