import Type
class Stats(object):
    def __init__(self, hp, ):
        self.hp = hp

class Pokemon(object):
    def __init__(self, name, firstType, secondType):
        self.name = name
        self.firstType = firstType
        self.secondType = secondType

Gengar = Pokemon("Gengar", Type.Ghost, Type.Poison)