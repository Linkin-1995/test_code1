"""
    扩展重写
        子类重写父类方法时,先通过super()调用父类方法,
        再定义自身功能
"""


class EmployeeManager:
    def __init__(self):
        self.all_employee = []

    def add_employee(self, emp):
        # 传入的是一种员工
        if isinstance(emp, Employee):
            self.all_employee.append(emp)

    def calculate_total_money(self):
        total_money = 0
        for emp in self.all_employee:
            # 先用
            total_money += emp.get_money()
        return total_money


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_money(self):
        return self.base_salary


# --------------------------------

class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    # 后做
    def get_money(self):
        # return self.base_salary + self.bonus

        return super().get_money() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_money(self):
        # return self.base_salary + self.bug_count * 5
        return self.get_money() + self.bug_count * 5


manager = EmployeeManager()
manager.add_employee(Programmer(8000, 100000))
manager.add_employee(Tester(5000, 500))
manager.add_employee(10)
print(manager.calculate_total_money())
