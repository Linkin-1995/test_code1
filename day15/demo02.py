"""
    包

根目录
    包(文件夹)
        模块
            类
                函数(方法)
                    语句
案例：
1.	根据下列结构，创建包与模块。
my_project /
    main.py
    common/
        __init__.py
        list_helper.py
        skill_system/
                __init__.py
                skill_deployer.py
                  skill_manager.py
2.	在main.py中调用skill_manager.py中实例方法。
3.	在skill_manager.py中调用skill_deployer.py中实例方法。
4.	在skill_deployer.py中调用list_helper.py中类方法。
"""
# 路径从根目录写起
# 方式1：
# 语法：import 路径.模块 as 别名
# 使用：别名.成员
# import package01.package02.m02 as m
#
# m.func01()

# 方式2：
# 语法：from 路径.模块 import 成员
# 使用：成员
from package01.package02.m02 import func01

func01()


