import stats
import type
import moves

NoType = type.Type("None")


class Pokemon(object):
    def __init__(self, name, firstType, secondType, stats, level):
        self.name = name
        self.firstType = firstType
        self.secondType = secondType
        self.stats = stats
        self.level = level

    def calculateEffecticityForPokemon(self, type):
        effect = self.firstType.calculateEffectivity(type)
        effect2 = self.secondType.calculateEffectivity(type)
        return effect * effect2

    def calculate_damage(self, move, attacker):
        stab = 1
        if move.type == attacker.firstType or move.type == attacker.secondType:
            stab = 1.5
        modifier = self.calculateEffecticityForPokemon(move.type) * stab
        damagemax = ((2 * attacker.level + 10) / 250 * (attacker.stats.spezattack / self.stats.spezdef) * move.damage + 2) * modifier
        damagemin = ((2 * attacker.level + 10) / 250 * (attacker.stats.spezattack / self.stats.spezdef) * move.damage + 2) * modifier * 0.85
        print(str(damagemin / self.stats.hp * 100) + "% - " + str(damagemax / self.stats.hp * 100) + "%")

    # implementation


Gengar = Pokemon("Gengar", type.Ghost, type.Poison, stats.GengarBase, 100)
Dragoran = Pokemon("Dragoran", type.Dragon, type.Flying, stats.DragoranBase, 100)
Test = Pokemon("Test", type.Normal, NoType, stats.TestStats, 1)
