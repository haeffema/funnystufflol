class Stats(object):
    def __init__(self, hp, physattack, physdef, spezattack, spezdef, speed):
        self.hp = hp
        self.physattack = physattack
        self.physdef = physdef
        self.spezattack = spezattack
        self.spezdef = spezdef
        self.speed = speed

# TODO: Stats je nach Level des Pokemon ausrechnen

# implementation
GengarBase = Stats(261, 166, 156, 296, 186, 256)
DragoranBase = Stats(323, 304, 226, 236, 236, 196)
TestStats = Stats(1, 1, 1, 1, 1, 1)