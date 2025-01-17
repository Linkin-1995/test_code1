# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 1.打印所有商品信息,
# 格式：商品编号xx,商品名称xx,商品单价xx.
for cid, info in dict_commodity_infos.items():
    print("商品编号%d, 商品名称%s, 商品单价%d." % (cid, info["name"], info["price"]))

# 2. 打印商品单价小于2万的商品信息
#  格式：商品编号xx,商品名称xx,商品单价xx.
for cid, info in dict_commodity_infos.items():
    if info["price"] < 20000:
        print("商品编号%d, 商品名称%s, 商品单价%d." % (cid, info["name"], info["price"]))

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
# 3. 查找数量最多的订单(使用自定义算法,不使用内置函数)
max_value = list_orders[0]
for i in range(1, len(list_orders)):
    if max_value["count"] < list_orders[i]["count"]:
        max_value = list_orders[i]
print(max_value)

# 4. 根据购买数量对订单列表降序(大->小)排列
for r in range(len(list_orders) - 1):
    for c in range(r + 1, len(list_orders)):
        if list_orders[r]["count"] < list_orders[c]["count"]:
            list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
print(list_orders)
