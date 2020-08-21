"""
    lambda 语法
        定义:匿名方法
        语法:
            lambda 参数:函数体
"""

# 普通函数
# def func01(p1, p2):
#     return p1 > p2
#
#
# print(func01(1, 2))

# 匿名方法写法1:有参数有返回值
func01 = lambda p1, p2: p1 > p2

print(func01(1, 2))

# 匿名方法写法2:有参数无返回值
# def func02(p1):
#     print("参数是:", p1)
#
# func02(100)

func02 = lambda p1: print("参数是:", p1)

func02(100)

# 匿名方法写法3:无参数有返回值
# def func03():
#     return "ok"
#
# print(func03())


func03 = lambda: "ok"

print(func03())

# 匿名方法写法4:无参数无返回值
# def func04():
#     print("hello world")
#
# func04()

func04 = lambda: print("hello world")

func04()


# 普通函数可以,但是lambda不支持的写法
# def func05():
#     for i in range(5):
#         print(i)
#
# func05()

# 注意1:python语言的lambda函数体只能有一句话
# lambda :for i in range(5):print(i)

def func06(p1):
    p1[0] = 10


list01 = [1]
func06(list01)
print(list01)  # [10]

# 注意2:python语言的lambda函数不支持赋值语句
# lambda p1:p1[0] = 10