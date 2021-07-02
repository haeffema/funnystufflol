class Pokemon(object):
    def __init__(self, name, firstType, secondType, stats):
        self.name = name
        self.firstType = firstType
        self.secondType = secondType
        self.stats = stats

    def calculateEffecticityForPokemon(self, type):
        effect = self.firstType.calculateEffectivity(type)
        effect2 = self.secondType.calculateEffectivity(type)
        return effect * effect2
