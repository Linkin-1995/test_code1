"""
    MVC: 软件架构
        Model：数据模型
        View：负责处理界面逻辑
        Controller:负责处理业务逻辑
"""
# 餐饮服务流程：
# 迎宾(接待) -- 服务员(点餐) -- 厨师(做菜) -- 送餐员(送)

class XXModel:
    def __init__(self,参数1,参数2):
        self.数据1 = 参数1
        self.数据2 = 参数2

class XXView:
    def __init__(self):
        self.__controller = XXController()

    def __显示菜单(self):
        pass

    def __获取输入(self):
        pass

    def __功能1(self):
       self.__controller.核心功能1()

    def __功能2(self):
        pass

    def main(self):
        pass

class XXController:
    def 核心功能1(self):
        pass

    def 核心功能2(self):
        pass

view = XXView()
view.main()
