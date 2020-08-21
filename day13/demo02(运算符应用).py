"""

"""


class Skill:
    def __init__(self, name="", atk_rate=0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration

    # 相同的比较规则：技能名称
    def __eq__(self, other):
        return self.name == other.name

    # 大小的比较规则：持续时间
    def __lt__(self, other):
        return self.duration < other.duration


s01 = Skill("乾坤大挪移", 2, 50, 55)
s02 = Skill("乾坤大挪移", 2, 50, 55)
# s01.__eq__(s02)
print(s01 == s02)  # False  比较的是内存地址
list_skills = [
    Skill("乾坤大挪移", 2, 50, 55),
    Skill("九阳神功", 3, 40, 50),
    Skill("九阳神功", 3, 40, 50),
    Skill("玉女心经", 1, 60, 35),
]
print(list_skills.count(Skill("九阳神功", 3, 40, 50)))
print(Skill("玉女心经", 1, 60, 35) in list_skills)
list_skills.remove(Skill("玉女心经", 1, 60, 35))

list_skills.sort()
for item in list_skills:
    print(item.__dict__)
