"""
    练习1:在列表中获取所有整数,并计算它的平方.
    练习2:在列表中获取所有大于10的小数.
    要求：使用列表推导式，生成器表达式完成.
    通过调试，体会差异.
"""
list01 = [4, "a", 54.5, True, 7, 89, 1.8]

# 练习1:
list02 = [item ** 2 for item in list01
          if type(item) == int]

generator02 = (item ** 2 for item in list01
               if type(item) == int)

print(list02)  # 有数据
# print(generator02)# 没数据
for item in generator02:
    print(item)

# 练习:
list03 = [item for item in list01
          if type(item) == float and item > 10]

generator03 = (item for item in list01
               if type(item) == float and item > 10)


print(list03)
for item in generator03:
    print(item)
