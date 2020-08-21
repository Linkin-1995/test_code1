"""
    # 练习:实现向量减法/乘法运算
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # type(对象) == 类型
        if type(other) == Vector2:
            return Vector2(self.x * other.x, self.y * other.y)
        if type(other) == int:
            return Vector2(self.x * other, self.y * other)


v01 = Vector2(1, 2)
v02 = Vector2(3, 4)
v03 = v01 - v02
v04 = v01 * v02
v05 = v01 * 2
print(v05.__dict__)
