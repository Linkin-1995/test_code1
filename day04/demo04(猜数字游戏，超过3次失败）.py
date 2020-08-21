"""
    猜数字2.0
        增加新功能：最多猜3次.
            如果超过次数提示"游戏失败"

        while 条件1:
            循环体
            if 条件2:
                break
        else:
            条件1不满足才执行执行本行代码
            break执行,不执行本行代码

        判断while循环退出的地点
"""
import random

random_number = random.randint(1, 100)
print(random_number)

count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入数字(1~100):"))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了,总共猜了" + str(count) + "次")
        break # 能执行到本行,说明循环条件满足,意味着循环的else不执行
else:
    print("游戏失败")#  能执行到本行,说明循环条件不满足,意味着循环没有从break退出
