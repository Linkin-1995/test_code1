"""
    温度转换器：
        摄氏度 = （华氏度 - 32） 除以 1.8
        (1)在终端中录入摄氏度，计算华氏度
"""
# 公式转换：华氏度 = 摄氏度 × 1.8 + 32
degree_centigrade = float(input("请输入摄氏度："))
fahrenheit_degree = degree_centigrade * 1.8 + 32
print("摄氏度是：" + str(fahrenheit_degree))
