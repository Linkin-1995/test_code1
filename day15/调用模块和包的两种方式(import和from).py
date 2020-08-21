# 方式1:"我过去" - "用变量找你"
# import usl
# view = usl.StudentView()
#
# view.main()

# 方式2:"你过来" - "导入到当前模块作用域"
from usl import StudentView

view = StudentView()
view.main()
