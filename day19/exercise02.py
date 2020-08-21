"""
    在插入和删除数据功能上,增加验证权限
    使用装饰器实现
    通过调试体会拦截的作用
"""


def verif_permissions(func):
    def wrapper():
        print("验证权限")
        func()
    return wrapper

@verif_permissions
def insert():
    print("插入数据")

@verif_permissions
def delete():
    print("删除数据")

insert()
delete()
