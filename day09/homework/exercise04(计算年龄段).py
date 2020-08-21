"""
    参照day04/homework_exercise02案例,
    定义函数,根据年龄,计算对应的人生阶段。
    age = int(input("请输入年龄："))
    if age < 0:
        print("年龄输入有误")
    elif age <= 6:
        print("童年")
    elif age <= 17:
        print("少年")
    elif age <= 40:
        print("青年")
    elif age <= 65:
        print("中年")
    else:
        print("老年")
"""


def get_stages_of_life(age):
    """
        获取人生阶段
    :param age: 年龄
    :return: 人生阶段
    """
    if age < 0:
        return None  # 函数没有结果
    if age <= 6:
        return "童年"
    if age <= 17:
        return "少年"
    if age <= 40:
        return "青年"
    if age <= 65:
        return "中年"
    return "老年"


print(get_stages_of_life(30))
