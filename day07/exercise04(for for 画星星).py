""" 5行   7列
*******
#######
*******
#######
*******　
"""

for r in range(5):  # 0       1      2
    for c in range(7):  # 01234  01234  01234
        if r % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()  # 换行