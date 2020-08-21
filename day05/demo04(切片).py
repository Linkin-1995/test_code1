"""
    切片：定位多个元素
        容器名称[开始:结束:间隔]

        # 产生整数
        # for number in range(开始,结束,间隔)
    练习：exercise03

"""
message = "我是花果山水帘洞齐天大圣孙悟空"

# 写法1:  容器名称[开始:结束:间隔]
#        注意：不包含结束
print(message[0:5:1])  # 我是花果山

# 写法2:  容器名称[开始:结束]
#        注意：间隔默认为1
print(message[0:5])  # 我是花果山

# 写法3:  容器名称[:结束]
#        注意：开始默认为头
print(message[:5])  # 我是花果山

# 写法4:  容器名称[:]
#        注意：结束默认为尾
print(message[2:])  #

# 索引超过范围会报错
# print(message[999]) # IndexError
# 切片可以超过范围
print(message[:999])

# 练一练
message = "我是花果山水帘洞齐天大圣孙悟空"
# 花果山
print(message[2:5])
# 是花果山水帘洞齐天大圣孙悟
print(message[1:-2])
# 山果花
print(message[4: 1:-1])
# 悟孙圣大天齐洞帘水山果花是
print(message[-2: 0:-1])
# 我花山帘齐大孙空
print(message[::2])
# 空悟孙圣大天齐洞帘水山果花是我
print(message[::-1])# 从尾到头获取全部
# 空
print(message[2:5:-1])
# 空
print(message[4: 1])