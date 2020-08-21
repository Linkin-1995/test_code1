"""
    参照day14/infos_system 与　day10/exercise04
    完成商品管理系统
        1. 实现添加商品信息
              V -M-> C
        2. 将View与Controller类中成员私有化
        3. 实现打印商品信息
              V负责打印,C提供只读属性
        4. 实现删除商品信息功能
              V负责xx,C提供xx
        5. 实现修改商品信息功能
              V负责xx,C提供xx
        6. 为所有公开方法添加文档注释
        7. 实现输入5键获取最贵商品功能
              V负责xx,C提供xx
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
        self.__controller = CommodityController()

    def __display_menu(self):
        print("1) 获取商品信息")
        print("2) 显示商品信息")
        print("3) 删除商品信息")
        print("4) 修改商品信息")
        print("5) 显示最贵商品信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            # 对象.实例方法()
            self.__input_commodity()
        elif item == "2":
            self.__show_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__update_commodity()
        elif item == "5":
            self.__show_commodity_by_max_price()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))
        # 对象.实例变量.实例方法(参数)
        self.__controller.add_commodity(commodity)

    def __show_commoditys(self):
        for commodity in self.__controller.list_commoditys:
            print(commodity.__dict__)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __delete_commodity(self):
        cid = int(input("请输入商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __update_commodity(self):
        commodity = CommodityModel()
        commodity.cid = input("请输入商品编号：")
        commodity.name = input("请输入商品名称：")
        commodity.price = input("请输入商品单价：")
        if self.__controller.modify(commodity):
            print("修改成功")
        else:
            print("需改失败")

    def __show_commodity_by_max_price(self):
        commodity = self.__controller.get__commodity_by_max_price()
        print(commodity.__dict__)


class CommodityController:
    """
        逻辑控制器：负责处理业务逻辑(存储/查询)
    """

    def __init__(self):
        self.__list_commoditys = []
        self.__start_cid = 1001

    @property
    def list_commoditys(self):
        """
            商品列表
        """
        return self.__list_commoditys

    def add_commodity(self, commodity_target):
        """
            添加商品信息
        :param commodity_target:CommodityModel类型的商品
        """
        # 设置学生的编号(自增长)
        commodity_target.cid = self.__start_cid
        self.__start_cid += 1
        self.__list_commoditys.append(commodity_target)

    def remove_commodity(self, cid):
        """
            移除商品信息
        :param cid:int类型商品编号
        :return:是否移除成功
        """
        for commodity in self.__list_commoditys:
            if commodity.cid == cid:
                self.__list_commoditys.remove(commodity)
                return True
        return False

    def modify(self, commodity):
        """
            修改商品信息
        :param commodity:CommodityModel类型的商品
        :return:是否修改成功
        """
        for item in self.__list_commoditys:
            if item.cid == commodity.cid:
                item.name = commodity.name
                item.price = commodity.price
                return True
        return False

    def get__commodity_by_max_price(self):
        """
            获取价格最高的商品
        :return: 商品对象
        """
        max_value = self.__list_commoditys[0]
        for i in range(1, len(self.__list_commoditys)):
            if max_value.price < self.__list_commoditys[i].price:
                max_value = self.__list_commoditys[i]
        return max_value


view = CommodityView()
view.main()
