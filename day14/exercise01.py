"""
    参照day14/infos_system 与　day10/exercise04
    完成商品管理系统
        实现添加商品信息
            V -M-> C
"""


class CommodityModel:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    """
        界面视图：负责处理界面逻辑(input/print)
    """

    def __init__(self):
        # 对象.实例变量 = 类名()
        self.controller = CommodityController()

    def display_menu(self):
        print("1) 获取商品信息")
        print("2) 显示商品信息")
        print("3) 删除商品信息")
        print("4) 修改商品信息")

    def select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            # 对象.实例方法()
            self.input_commodity()

    def input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))
        # 对象.实例变量.实例方法(参数)
        self.controller.add_commodity(commodity)


class CommodityController:
    """
        逻辑控制器：负责处理业务逻辑(存储/查询)
    """

    def __init__(self):
        self.list_commoditys = []
        self.start_cid = 1001

    def add_commodity(self, commodity_target):
        # 设置学生的编号(自增长)
        commodity_target.cid = self.start_cid
        self.start_cid += 1
        self.list_commoditys.append(commodity_target)


view = CommodityView()
while True:
    view.display_menu()
    view.select_menu()
