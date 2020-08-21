"""
6. 一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)   13 次
    -- 全过程总共移动多少米?
"""
height = 100
count = 0
distance = height  # 开始落下 -- 计算初始高度
# 判断弹之前的高度height
# 判断弹之后的高度height / 2
# 0.01 弹起来的最小高度
while height / 2 > 0.01:
    # 弹起来
    height /= 2
    count += 1
    distance += height * 2  # 弹起过程 -- 累加起落距离
    # print("第" + str(count) + "次弹起来的高度是" + str(height))
    print("第%d次弹起来的高度是%f" % (count, height))

# print("总共弹起" + str(count) + "次")
print("总共弹起%d次" % count)
print("全过程总共移动%f米" % distance)  # 最终落地 -- 获取最终距离
