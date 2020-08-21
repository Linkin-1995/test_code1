class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # + ：创建新数据
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    # +=：尽量在原有基础上改变(不可变对象只能创建新,可变对象不创建新)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


v01 = Vector2(1, 2)
v02 = Vector2(3, 4)
print(id(v01))
v01 += v02  # v01.__iadd__(v02)
print(id(v01))
print(v01.__dict__)

# +=：可变对象不创建新
list01 = [1]
print(id(list01))
list01+=[2]
print(id(list01))

# +=：不可变对象创建新
tuple01 = (1,)
print(id(tuple01))
tuple01+=(2,)
print(id(tuple01))