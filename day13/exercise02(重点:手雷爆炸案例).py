"""
     封装 - 划分变化   【分】
     继承 - 隔离变化   【隔】
     多态 - 实现变化   【做】
"""
class Grenade:
    def explode(self,target):
        print("手雷爆炸")
        # 先确定用法
        target.damage()

class AttackTarget:
    def damage(self):
        pass

class Player(AttackTarget):
    def damage1(self):
        print("玩家受伤")
        print("碎屏")

class Enemy(AttackTarget):
    def damage2(self):
        print("敌人受伤")
        print("头顶爆字")

# 测试
g01 = Grenade()
g01.explode( Player() )
g01.explode( Enemy() )