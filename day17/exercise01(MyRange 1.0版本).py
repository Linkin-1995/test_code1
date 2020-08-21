"""
     MyRange1.0
     自定义MyRange类,实现下列效果
"""


class MyRangeIterator:
    def __init__(self, stop):
        self.__number = -1
        self.__stop = stop

    def __next__(self):
        if self.__number >= self.__stop - 1:
            raise StopIteration()
        self.__number += 1
        return self.__number


class MyRange:
    def __init__(self, end):
        self.__end = end

    def __iter__(self):
        return MyRangeIterator(self.__end)


# 循环一次 计算一次 返回一次
for number in MyRange(5):  # 0 ~ 4
    print(number)

# m01 = MyRange(5)
# iterator = m01.__iter__()
# while True:
#     try:
#         number = iterator.__next__()
#         print(number)
#     except StopIteration:
#         break

for number in MyRange(9999999999999999999):  # 0 ~ 4
    print(number)
