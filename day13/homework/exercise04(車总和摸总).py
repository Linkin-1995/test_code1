"""
    -- (3)玩家攻击(攻击力)敌人，敌人(血量)受伤(减血)后可能死亡(播放死亡动画)
"""

"""
class Player:
    def __init__(self,atk):
        self.atk = atk

    def attack(self,target):
        # 对象.实例方法(参数)
        target.damage(self.atk)

class Enemy:
    def __init__(self,hp):
        self.hp = hp

    def damage(self,value):
        print("额,受伤")
        self.hp -= value
        if self.hp <=0:
            # 对象.实例方法()
            self.death()

    def death(self):
        print("播放死亡动画")

p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
"""

"""
    (4)敌人还能攻击玩家,玩家受伤(减血+碎屏)后可能死亡(游戏结束)
        # 缺点1：两个类代码重复度高
        # 缺点2：两个类紧耦合
"""
class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        # 对象.实例方法(参数)
        target.damage(self.atk)

    def damage(self, value):
        print("碎屏")
        print("额,受伤")
        self.hp -= value
        if self.hp <=0:
            self.death()

    def death(self):
        print("游戏结束")


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("头顶爆字")
        print("额,受伤")
        self.hp -= value
        if self.hp <= 0:
            # 对象.实例方法()
            self.death()

    def death(self):
        print("播放死亡动画")

    def attack(self, target):
        target.damage(self.atk)


p01 = Player(500,50)
e01 = Enemy(100,10)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)
