"""
    定义获取成绩函数
    要求:调用函数一定获得成绩(出错就重复录入)
"""


def get_score():
    while True:  # 死循环
        try:
            # 如果错误,return不执行
            score = float(input("请输入成绩:"))
            return score  # 唯一出口
        except:
            # print("输入有误")
            pass  # 空白


result = get_score()
print("成绩是:", result)
