"""
    可迭代对象工具模块
    价值1:
        自定义高阶函数类,功能比内置高阶函数多的多.
    价值2:
        真正领悟函数式编程思想:
            分
            隔
            做
    价值3:
        面试吹牛:精通函数式编程
            开发步骤:
                *1. 根据需求实现功能
                *2. "封装":将所有变化点定义为函数,通用代码定义函数
                *3. "继承":用参数隔离变化
                *4. "多态":调用通用函数,传递变化点(lambda).

                5. 将通用代码定义到IterableHelper类中
                6. 用lambda代替变化点

            源于微软Linq(语言集成查询)框架
    编程范式
        面向过程:考虑实现步骤

        面向对象:考虑实现的人(软件架构)
        函数式:将函数作为参数传递(功能)
"""


class IterableHelper:
    """
        集成操作框架(可迭代对象助手类)
    """

    # 静态方法:表达一种工具,不能(需要)操作对象或类成员
    # 使用方式:类.静态方法名()
    @staticmethod
    def find_all(iterable, func_condition):
        """
            在可迭代对象中根据条件查找满足的元素
        :param iterable: 可迭代对象
        :param func_condition: 查找条件
        :return: 生成器,推算满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable, func_condition):
        """
            在可迭代对象中根据条件查找满足的单个元素
        :param iterable: 可迭代对象
        :param func_condition: 查找条件
        :return: 满足条件的元素
        """
        for phone in iterable:
            if func_condition(phone):
                return phone

    @staticmethod
    def select(iterable, func_handle):
        """

        :param iterable:
        :param func_handle:
        :return:
        """
        for item in iterable:
            yield func_handle(item)

    @staticmethod
    def delete_all(iterable, func_condition):
        for i in range(len(iterable) - 1, -1, -1):
            # if iterable[i].color == "蓝色":
            if func_condition(iterable[i]):
                del iterable[i]

    @staticmethod
    def get_count(iterable, func_condition):
        count = 0
        for phone in iterable:
            # if phone.color == "白色":
            if func_condition(phone):
                count += 1
        return count

    @staticmethod
    def get_max(iterable, func_condition):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            # if max_value.price < iterable[i].price:
            if func_condition(max_value) < func_condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def is_exists(iterable, func_condition):
        for item in iterable:
            # if item.brand == "三星2":
            if func_condition(item):
                return True
        return False

    @staticmethod
    def order_by(iterable, func_condition):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                # if iterable[r].price > iterable[c].price:
                if func_condition(iterable[r]) > func_condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
