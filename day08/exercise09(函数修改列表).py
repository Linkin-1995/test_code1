"""
    定义函数,将数字列表中所有偶数,设置为0.
    list01 = [4,55,6,78,66,22,89,90]
             [0,55,0,0,0,0,89,0]
"""

def set_even_to_zero(list_target):
    for i in range(len(list_target)):
        if list_target[i] % 2 == 0:
            list_target[i] = 0
##必须是list[i],不能是for item in list: 中的"item",因为item是不可变参数


list01 = [4, 55, 6, 78, 66, 22, 89, 90]
set_even_to_zero(list01)
print(list01)
