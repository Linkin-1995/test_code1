# 练习：
# 累加0 1 2 3 4 5 6 7 8
# 累加3 4 5 6 7 8 9 10
# 累加2 4 6 8 10 12
# 累加8 7 6 5 4 3
# 累加-1 -2 -3 -4 -5 -6
sum_value = 0
for number in range(9):
    sum_value += number
print(sum_value)

sum_value = 0
for number in range(3, 11):
    sum_value += number
print(sum_value)

sum_value = 0
for number in range(2, 13, 2):
    sum_value += number
print(sum_value)

sum_value = 0
# 备注：希望包含3,所以终止值是2
for number in range(8, 2, -1):
    sum_value += number
print(sum_value)

sum_value = 0
for number in range(-1, -7, -1):
    sum_value += number
print(sum_value)
