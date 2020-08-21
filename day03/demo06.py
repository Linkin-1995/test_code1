"""
    if elif

    调试Debug
        定义：
            让程序中断,逐语句排查错误(审查变量取值)的过程。
        步骤：
            1. 添加断点(在可能出错的行)
            2. 开始调试
            3. 逐语句执行(F8)
"""
number = int(input("请输入数字："))
if number > 0:
    print("正数")
elif number < 0:
    print("负数")
else:
    print("零")
