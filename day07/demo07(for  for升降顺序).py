"""
    基础算法：
        1. 变量交换
              a,b=b,a
        2. 计算极值
             max_value = list01[0]
             for i in range(1,len(list01)):
                if max_value  < list01[i]:
                    max_value = list01[i]
            print(max_value)
        3. 排序
"""
# 降序：大 --> 小
# 核心思想：每个元素之间进行比较
#  规律：用第一个元素与后面元素依次比较，发现更大则交换.
#       用第二个元素与后面元素依次比较，发现更大则交换.
#       用第...个元素与后面元素依次比较，发现更大则交换.
# 步骤：取数据/作比较/发现更大就交换
list01 = [43, 2, 45, 65, 76, 8, 9]
# 1. 取数据(不要最后一个)
for r in range(len(list01) - 1):
    # 2. 作比较(从下一个开始)
    for c in range(r + 1, len(list01)):
        # 3. 如果发现更大则交换
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)

# 升序：小 --> 大
