"""
    实例成员
        实例变量
            核心价值:每个对象存储一份,表达不同对象的[不同]数据
            在构造函数中定义下列代码:
                对象.变量名
            调用:
                对象.变量名

        实例方法
            在类中定义下列代码:
                def 方法名(self):
                    方法体
            调用:
                对象.实例方法()
        总结: 对象.成员名
"""


class Wife:
    def __init__(self, name):
        # 创建实例变量:对象.变量名 = 数据
        self.name = name

    def work(self):
        pass


w01 = Wife("建宁")
# 修改实例变量: 对象.变量名 = ?
w01.name = "建宁公主"
# 读取实例变量: ? = 对象.变量名
print(w01.name)
# 调用实例方法:对象.实例方法()
w01.work()  # 自动传递w01给self  -->   work(w01)
# (不建议)通过类名调用实例方法:类名.实例方法(w01)
Wife.work(w01)

# 系统定义的变量__dict__中,记录着当前对象所有实例变量
print(w01.__dict__)

# 不建议:类中成员应该由类的定义者决定
# class Wife:
#     pass
#
# w01 = Wife()
# # 创建实例变量:对象.变量名 = 数据
# w01.name = "建宁公主"
# # 读取实例变量
# print(w01.name)

# 不建议:创建实例变量应该在构造函数中
# class Wife:
#     def set_name(self, name):
#         # 创建实例变量:对象.变量名 = 数据
#         self.name = name
#
# w01 = Wife()
# w01.set_name("建宁")
# # 读取实例变量
# print(w01.name)
