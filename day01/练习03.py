"""
    在day01中创建文件exercise03.py
    汇率转换器
"""

# 1. 获取数据 - 美元
usd = input("请输入美元：")
# 2. 逻辑处理 - 美元 * 7.0733
cny = float(usd) * 7.0733
# 3. 显示结果 - xx美元=xx人民币
print(usd + "美元=" + str(cny) + "人民币")
