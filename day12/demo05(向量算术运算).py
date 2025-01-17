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

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

v01 = Vector2(1, 2)
v02 = Vector2(3, 4)
v03 = v01 + v02  # v01.__add__(v02)
print(v03.__dict__)


