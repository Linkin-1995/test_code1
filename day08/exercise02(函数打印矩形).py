# 练习:定义函数,在终端中打印矩形
# 参照day07/demo07.py

# 做法(变化) + 用法
# for r in range(3):
#     for c in range(5):
#         print("#", end=" ")
#     print()
#
# for r in range(2):
#     for c in range(4):
#         print("*", end=" ")
#     print()

# 做法
def print_rectangular(r_count, c_count, char):
    """
        打印矩形
    :param r_count:行数量
    :param c_count:列数量
    :param char:填充字符
    """
    for r in range(r_count):
        for c in range(c_count):
            print(char, end=" ")
        print()


# 王八的屁股  -- 规定
# 用法
print_rectangular(3, 5, "#")
print_rectangular(2, 4, "*")
