"""
    重写 __str__
"""


# 任何类都直接或者间接继承 object 类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 改变父类(object)对象转换为字符串的功能
    # 父类格式:<__main__.Person object at 0x7f5becd1feb8>

    # 对象->字符串:没有语法限制
    def __str__(self):
        return "我叫%s,今年%d." % (self.name, self.age)

    # 对象->字符串:格式必须满足python语法
    def __repr__(self):
        return "Person('%s', %d)" % (self.name, self.age)


p01 = Person("悟空", 25)
print(p01)
# 本质:
# message = p01.__str__() # 自定义对象 --> 字符串
# print(message)

# 拷贝自定义对象:
# 价值:将字符串作为python代码执行
message = p01.__repr__()  # "Person('悟空', 25)"
p02 = eval(message)  # 执行(  "Person('悟空', 25)" )

p01.name = "大圣"  # 修改其中之一
print(p02.name)  # 不影响另外一个
