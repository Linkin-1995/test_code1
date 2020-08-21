"""

"""
# 语法：from 包 import *
# 定义可导出成员：
#   在包的__init__.py模块中设置__all__变量
# from package01 import *
#
# m2.func02()

#　语法：import　包
import package01
#   在包的__init__.py模块中导入需要使用的模块
#    import package01.m2
#    import package01.m3

# package01.m2.func02()
# package01.m3.func03()

#     from package01.m2 import func02
#     from package01.m3 import func03
package01.func02()
package01.func03()
