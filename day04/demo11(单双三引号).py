"""
    字符串字面值
"""
# 双引号（建议）
data01 = "字符串"
# 单引号
data02 = '字符串'
# 三引号（可见即所得）
data03 = '''字符串'''
data03 = """
字
     符
串"""
print(data03)

# 1. 单引号内的双引号不算结束符
data04 = '我是"孙悟空".'
# 2. 双引号内的单引号不算结束符
data05 = "我是'孙悟空'."

# 转义字符:改变 原始含义的特殊字符
# \"  \'   \n换行   \\
data06 = "我是\"孙悟空\"."
data07 = "我是\n孙悟空."
url = "a\\b\\c\\d.txt"
url = r"a\b\c\d.txt"
print(url)






