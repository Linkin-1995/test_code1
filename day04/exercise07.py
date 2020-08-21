# 累加10 -- 60之间,个位不是3/5/8的整数和。
# 提示：个位是3/5/8就跳过
sum_value = 0
for number in range(10, 61):
    unit = number % 10
    if unit == 3 or unit == 5 or unit == 8:
        continue
    sum_value += number
print("累加和是:" + str(sum_value))
