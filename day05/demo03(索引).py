"""
    索引：定位单个元素
        容器名称[整数]
    练习：exercise02
"""
message = "我是花果山水帘洞齐天大圣孙悟空"
print(message[1])  # 定位第二个元素
print(message[-2])  # 定位倒数第二个
# 定位中间元素(总数 // 2)
# len(message) ---> 15
index = len(message) // 2  # 15 // 2 --> 7
print(message[index])
print(message[len(message) // 2])
