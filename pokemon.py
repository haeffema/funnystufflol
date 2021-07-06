import stats
import type

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


# implementation
Gengar = Pokemon("Gengar", type.Ghost, type.Poison, stats.GengarBase)
Dragoran = Pokemon("Dragoran", type.Dragon, type.Flying, stats.DragoranBase)
Test = Pokemon("Test", type.Normal, None, stats.TestStats)