# 练习:将下列面向过程的代码改为面向对象代码.
#     备注:参照下列思想完成
# 步骤:1. 根据字典创建类
#     2. 修改商品列表(字典 -> 自定对象)
#     3. 修改函数(对数据的操作)

# 面向过程:
# list_orders = [
#     {"cid": 1001, "count": 1},
#     {"cid": 1002, "count": 3},
#     {"cid": 1005, "count": 2},
# ]
# def print_orders():
#     for order in list_orders:
#         print("商品编号是:%d,购买数量是:%d"%(order["cid"],order["count"]))
# 面向对象:
class Order:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count


list_orders = [
    Order(1001, 1),
    Order(1002, 3),
    Order(1005, 2),
]


def print_orders():
    for order in list_orders:
        print("商品编号是:%d,购买数量是:%d" % (order.cid, order.count))


# -----------------------练习开始-------------------------------
class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


# 商品列表
list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1001, "屠龙刀", 10000),
]


def print_single_commodity(commodity):
    # 容器['键']  -->  对象.变量名
    print(f"编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.price}")


# 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)
print_commodity_infos()

# 2.  定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)
print_price_in_2w()

# 3. 查找最贵的商品(使用自定义算法,不使用内置函数)
def commodity_max_by_price():
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value.price < list_commodity_infos[i].price:
            max_value = list_commodity_infos[i]
    return max_value
#print_single_commodity(commodity_max_by_price())
result=commodity_max_by_price()
print(result.__dict__)

# 4. 根据单价对商品列表降序排列
def descending_order_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price < list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
    return list_commodity_infos
result=descending_order_by_price()
for item in result:
    print(item.__dict__)

