"""
     MyRange2.0
"""


class MyRange:
    def __init__(self, end):
        self.__end = end

    def __iter__(self):
        number = 0
        while number < self.__end:
            yield number
            number += 1


# 循环一次 计算一次 返回一次
for number in MyRange(5):  # 0 ~ 4
    print(number)

m01 = MyRange(5)
iterator = m01.__iter__()
while True:
    try:
        number = iterator.__next__()
        print(number)
    except StopIteration:
        break
