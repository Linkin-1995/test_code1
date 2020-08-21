"""
    函数设计理念
        崇尚小而精,拒绝大而全

    返回值
        函数定义者 给 调用者 传递的信息

        def 函数名():
            ....
            return 数据

        变量 = 函数名()
    练习:exercise04~06
"""

# 需求:定义函数,美元转换为人民币.

def usd_to_cny(usd):
    cny = usd * 7.0733
    # 返回 数据
    return cny


# 接收 结果
result = usd_to_cny(10)
print("结果是:" + str(result))
