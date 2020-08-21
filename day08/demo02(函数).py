"""
    函数 - 功能
        入门　- 做法与用法分离
        制作
            def 函数名称():
                函数体

        使用
            函数名()
"""
# 做法 + 用法  -->  缺点:做法变化,需要修改多次.
"""
print("临门一脚")
print("摆拳")
print("勾拳")

# ..... 
print("临门一脚")
print("摆拳")
print("勾拳")
"""

# 做法　一次
def attack():
    print("摆拳")
    print("临门一脚")
    print("勾拳")

# 用法　多次
attack()
attack()
attack()
attack()
attack()
attack()