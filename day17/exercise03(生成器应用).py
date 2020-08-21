"""
    练习：
        list01 = [3,434,35,6,7]
        定义函数,将全局变量list01中所有奇数返回.
        1. 使用传统思想：
            创建新列表存储所有结果,再返回列表
        2. 使用生成器思想：
            使用yield返回奇数
"""
list01 = [3, 434, 35, 6, 7]


def find01():
    list_result = []
    for number in list01:
        if number % 2:
            list_result.append(number)
    return list_result

# 立即 积极
result = find01()
for item in result:
    print(item)


# ..................................

def find02():
    for number in list01:
        if number % 2:
            yield number

# 推算数据
# 延迟(惰性)操作
result = find02()
for item in result:
    print(item)
