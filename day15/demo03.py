"""
    导包是否成功的唯一标准
        导入路径 + 系统路径 = 真实路径
        导入路径：import xxx
                from xxxx
        系统路径：sys.path
                [路径1,路径2,....]
                第一个路径是项目根目录
                根目录：第一次执行的模块所在目录
        导入包的搜索顺序：系统路径
"""
import sys

print(sys.path)

# 练习：在终端中从skill_manager.py运行
#   cd /home/tarena/month01/day15/my_project/skill_system
#   python3 skill_manager.py