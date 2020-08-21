"""
    函数间互相调用
"""

# ---------------函数------------------
def multiple_attack(count):
    for __ in range(count):
        single_attack()

def single_attack():
    print("摆拳")
    print("临门一脚")
    print("勾拳")

# ---------------入口------------------
multiple_attack(2)
