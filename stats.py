class Stats(object):
    def __init__(self, hp, physattack, physdef, spezattack, spezdef, speed):
        self.hp = hp
        self.attack = physattack
        self.physdef = physdef
        self.spezattack = spezattack
        self.spezdef = spezdef
        self.speed = speed


# implementation
GengarBase = Stats(60, 65, 60, 130, 75, 110)
