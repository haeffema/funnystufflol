import type

spez = "Special"


class Move(object):
    def __init__(self, name, damage, damagetyp, type, accuracy):
        self.name = name
        self.damage = damage
        self.damagetyp = damagetyp
        self.type = type
        self.accuracy = accuracy


# implementation
ShadowBall = Move("Shadow Ball", 80, spez, type.Ghost, 100)
