"""
    需求：
        创建函数,打印列表所有元素(一行一个)
"""
# list01 = [1,2,3,4]
# for item in list01:
#     print(item)
#
# list02 = [5,65,76,8,90]
# for item in list02:
#     print(item)

# 做法 1次
def print_list_elements(list_target):
    for item in list_target:
        print("元素是:"+str(item))

# 用法 2次
list01 = [1,2,3,4]
list02 = [5,65,76,8,90]
print_list_elements(list01)
print_list_elements(list02)