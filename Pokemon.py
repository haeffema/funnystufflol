import Type


class Stats(object):
    def __init__(self, hp, physattack, physdef, spezattack, spezdef, speed):
        self.hp = hp
        self.attack = physattack
        self.physdef = physdef
        self.spezattack = spezattack
        self.spezdef = spezdef
        self.speed = speed


class Pokemon(object):
    def __init__(self, name, firstType, secondType, stats):
        self.name = name
        self.firstType = firstType
        self.secondType = secondType
        self.stats = stats


GengarBase = (60, 65, 60, 130, 75, 110)
Gengar = Pokemon("Gengar", Type.Ghost, Type.Poison, GengarBase)
