"""
    作用域
        在局部作用域修改全局变量,需要使用global声明
"""
b = 20


def func01():
    # 声明全局变量,否则认为是局部变量
    global b
    b = 200


func01()
print(b)



c = [30]

def func02():
    # 读取全局变量,修改列表元素. 无需使用global修饰
    c[0] = 300

func02()
print(c) # [300]
