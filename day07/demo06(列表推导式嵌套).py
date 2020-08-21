"""
    列表推导式嵌套
        将两个列表中所有元素合并在一起
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["牛奶", "雪碧", "可乐", "咖啡"]
# 拿出list01第一个元素
# 拿出list02第一个元素   拿出list02第二个元素   拿出list02第...个元素
# 拿出list01第二个元素
# 拿出list02第一个元素   拿出list02第二个元素   拿出list02第...个元素

# 拿出list01第...个元素
# 拿出list02第一个元素   拿出list02第二个元素   拿出list02第...个元素


# for c in list02:
#     print(list01[0] + c)
#
# for c in list02:
#     print(list01[1] + c)
#
# for c in list02:
#     print(list01[2] + c)

# list_result = []
# for r in list01:  #        香蕉                    苹果
#     for c in list02:  # 牛奶,雪碧,可乐,咖啡  牛奶,雪碧,可乐,咖啡
#         list_result.append(r + c)
# print(list_result)

list_result = [r + c for r in list01 for c in list02]
print(list_result)
