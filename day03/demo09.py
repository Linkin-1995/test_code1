"""
    变量交换算法
        本质：借助第三方(桌子)
            左手 = 杯子
            右手 = 手机
            桌子 = 左手
            左手 = 右手
            右手 = 桌子
        python：
            a,b = b,a
"""
bridegroom_name = "武大郎"
bride_name = "潘金莲"

# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp

bridegroom_name, bride_name = bride_name, bridegroom_name

print("交换后的新郎：" + bridegroom_name)  #
print("交换后的新娘：" + bride_name)  #
