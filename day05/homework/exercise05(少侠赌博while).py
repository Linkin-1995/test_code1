"""
    玩家的身家初始10000，实现下列效果：
        少侠请下注: 30000
        超出了你的身家，请重新投注。
        少侠请下注: 8000
        你摇出了5点,庄家摇出了3点
        恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
        少侠请下注: 18000
        你摇出了6点,庄家摇出了6点
        打平了，少侠，在来一局？
        少侠请下注: 18000
        你摇出了4点,庄家摇出了6点
        少侠,你输了，身家还剩 0
        哈哈哈，少侠你已经破产，无资格进行游戏
"""
import random

money = 10000
while money > 0:
    bet = int(input("少侠请下注: "))
    if bet > money:
        print("超出了你的身家，请重新投注。")
        continue  # 短路思想(满足xx条件,后续代码不在执行)
    dealer = random.randint(1, 6)
    player = random.randint(1, 6)
    # print("你摇出了" + str(player) + "点,庄家摇出了" + str(dealer) + "点")
    print("你摇出了%d点,庄家摇出了%d点" % (player, dealer))
    if dealer > player:
        money -= bet
        # print("少侠,你输了，身家还剩" + str(money))
        print("少侠,你输了，身家还剩%d" % money)
    elif dealer < player:
        money += bet
        # print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩" + str(money))
        print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩%d" % money)
    else:
        print("打平了，少侠，在来一局？")
print("哈哈哈，少侠你已经破产，无资格进行游戏")
