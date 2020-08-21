# 练习：定义数值累乘的函数
# 1,2,3,4
# 4,54,5,56,67,78,89
def multiplicative(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(multiplicative(1, 2, 3, 4))
print(multiplicative(4, 54, 5, 56, 67, 78, 89))
