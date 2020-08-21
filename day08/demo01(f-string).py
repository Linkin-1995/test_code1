"""
    f-string
"""
player = 5
dealer = 3
# print("你摇出了%d点,庄家摇出了%d点" % (player, dealer))
# 直接在需要占位的地方放置变量,结果更加清晰.
print(f"你摇出了{player}点,庄家摇出了{dealer}点")

# 格式比较复杂时,百分号占位符代码可读性更高
print("%d+%d=%d" % (player, dealer, player + dealer))
# print(f"{player}+{dealer}={player + dealer}")
