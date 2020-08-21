"""
    练习1: -- 用
        下载代码common/iterable_tools
        在手机列表中查找所有白色手机
        for 变量 in IterableHelper.find_all(手机列表, 条件函数):
            ...

    练习2: -- 做 + 用
        将day17/exercise09中find函数
        定义到IterableHelper类中,命名find_single
        在手机列表中查找品牌是"苹果2"的手机
"""
class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]
