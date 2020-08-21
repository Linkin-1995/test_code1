"""
    定义函数,查找列表中是否存在相同元素(不借助其他容器,自定义算法实现)
"""


def is_repeat(list_target):
    # 取数据
    for r in range(len(list_target) - 1):
        # 作比较
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True  # 中 -- 有相同项则返回True(退出函数)
    return False  # 比较过程后 -- 没有相同项则返回False


list01 = [170, 160, 180, 165]

print(is_repeat(list01))


或者
list01=[1,3,8,9,3,4,5]
def Determine_the_digital(list):
    for i in range(len(list)):
        if i in list[i+1:] or i in list[0:i]:
            return "True"
    return "False"
result=Determine_the_digital(list01)
print(result)
