"""
     MyRange3.0
     yield -> 生成器 generator
"""

"""
class generator: #生成器　= 可迭代对象 + 迭代器(主要)
    def __iter__(self): # 可迭代对象
        return self
    
    def __next__(self): # 迭代器
        准备数据
        返回数据

for item in generator():
    ...
"""


def my_range(end):
    number = 0
    while number < end:
        yield number
        number += 1


# 循环一次 计算一次 返回一次
# for number in my_range(5):  # 0 ~ 4
#     print(number)

m01 = my_range(9999999999)  # 创建生成器对象
iterator = m01.__iter__()
while True:
    try:
        number = iterator.__next__()
        print(number)
    except StopIteration:
        break
