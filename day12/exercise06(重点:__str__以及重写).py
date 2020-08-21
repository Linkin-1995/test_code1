"""
    改变父类行为 __str__
        对象 -> 字符串
            手机: xxx手机xx颜色的价格是xx.

        拷贝:Phone/与Employees对象,修改拷贝前数据,打印拷贝后数据.
"""
class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def __str__(self):
        return f"{self.brand}手机{self.color}颜色的价格是{self.price}."

    def __repr__(self):
        return f"Phone('{self.brand}',{self.price},'{self.color}')"


class Employees:
    def __init__(self, eid, did, name, money):
        self.money = money
        self.name = name
        self.did = did # 部门编号
        self.eid = eid # 员工编号

    def __str__(self):
        return f"{self.eid}--{self.did}--{self.name}--{self.money}"

    def __repr__(self):
        return f"Employees({self.eid}, {self.did}, '{self.name}', {self.money})"

p01 = Phone("华为1", 5999, "蓝")
print(p01)

p02 = eval(p01.__repr__())
p01.brand = "华为"
print(p02.brand) # ? 华为1

e01 = Employees(1001, 9002, '师父', 60000)
print(e01)

e02 = eval(e01.__repr__())
e01.name = "大师"
print(e02.name) # ? 师父
