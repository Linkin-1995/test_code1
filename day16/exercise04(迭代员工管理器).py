"""
    迭代员工管理器
    要求:自行推导
"""


class EmployeeIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index >= len(self.data) - 1:
            raise StopIteration()
        self.index += 1
        return self.data[self.index]


class EmployeeController:
    def __init__(self):
        self.__list_employees = []

    def add_employee(self, graphic):
        self.__list_employees.append(graphic)

    def __iter__(self):
        return EmployeeIterator(self.__list_employees)


controller = EmployeeController()
controller.add_employee("程序员")
controller.add_employee("销售员")
controller.add_employee("测试员")

for item in controller:
    print(item)
