"""
    玩家 攻击 敌人,敌人播放受伤动画.
"""


class Player:
    def attack(self, target):
        print("攻击")
        target.damage()

class Enemy:
    def damage(self):
        print("播放动画")

p01 = Player()
e01 = Enemy()
p01.attack(e01)
