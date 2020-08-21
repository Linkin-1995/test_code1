# 方式1:"我过去" - "用变量找你"
# import usl
# view = usl.StudentView()
#
# view.main()

# 方式2:"你过来" - "导入到当前模块作用域"
from usl import StudentView

# 快捷键:main + 回车
if __name__ == '__main__':
    # 全局异常处理:
    # try:
        view = StudentView()
        view.main()
    # except:
    #     print("出错啦")
