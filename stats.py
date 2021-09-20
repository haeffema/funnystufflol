class Stats(object):
    def __init__(self, hp, physattack, physdef, spezattack, spezdef, speed):
        self.hp = hp
        self.attack = physattack
        self.physdef = physdef
        self.spezattack = spezattack
        self.spezdef = spezdef
        self.speed = speed

# TODO: Stats je nach Level des Pokemon ausrechnen

# implementation
GengarBase = Stats(261, 149, 156, 359, 187, 350)
DragoranBase = Stats(323, 367, 226, 212, 237, 284)
TestStats = Stats(1, 1, 1, 1, 1, 1)