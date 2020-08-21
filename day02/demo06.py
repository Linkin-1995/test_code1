"""
    核心数据类型
        Python变量没有类型 

"""
# 1. 字符串str:存储文本
name = "悟空"
str_number = "100" + "1"  # 文字拼接
print(str_number)  # "1001"

# 2. 整形int:存储整数
number01 = 100 + 1  # 数学运算
print(number01)

# 3. 浮点型float:存储小数
number02 = 100.1

# 4. 类型转换
#        结果 = 数据类型(待转数据)
"""
引入
# input的结果是字符串str,如果需要数学运算,则需要类型转换。
str_age = input("请输入年龄：")
# "18" -->  18
int_age = int(str_age)
result = int_age + 1
# 如果需要将数值以某种格式显示,则必须类型转换。
print("明年您的年龄是：" + str(result))
"""

# str --> int
result = int("18")  # 18
# int --> str
result = str(18)  # "18"
# float --> int
result = int(1.99)  # 1  截断删除
# int --> float
result = float(18)  # 18.0
# float --> str
result = str(1.23)  # "1.23"
# str--> float
result = float("1.23")  # 1.23

# 注意：
# 字符串转换为其他类型类型时,字符串必须"长得像"目标类型.
# result = int("abc")  # 报错
# result = float("abc")  # 报错
# result = int("1.23")  # 报错
