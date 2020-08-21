"""
    累加100 -- 999之间,百位不是4/6/9的整数和。
"""
sum_value = 0
for number in range(100, 1000):
    unit = number // 100
    if unit == 4 or unit == 6 or unit == 9:
        continue  # 跳过continue后面代码( sum_value += number 语句)
    sum_value += number
# print("累加和是:" + str(sum_value))
print("累加和是:%d" % sum_value)
