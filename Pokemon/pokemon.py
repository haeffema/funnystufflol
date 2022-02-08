import type

NoType = type.Type("None")


class Pokemon(object):
    def __init__(self, name, firstType, secondType, stats, level):
        self.name = name
        self.firstType = firstType
        self.secondType = secondType
        self.stats = stats
        self.level = level

    def calculate_effectivity_for_pokemon(self, type):
        effect = self.firstType.calculateEffectivity(type)
        effect2 = self.secondType.calculateEffectivity(type)
        return effect * effect2

    def calculate_damage(self, move, attacker):
        stab = 1
        if move.type == attacker.firstType or move.type == attacker.secondType:
            stab = 1.5
        modifier = self.calculate_effectivity_for_pokemon(move.type) * stab
        firstpart = (2 * attacker.level + 10) / 250
        secondpart = attacker.stats.spezattack / self.stats.spezdef
        damagemax = (firstpart * secondpart * move.damage + 2) * modifier
        damagemin = damagemax * 0.85
        print(str(round(damagemin / self.stats.hp * 100, 1)) + "% - " + str(
            round(damagemax / self.stats.hp * 100, 1)) + "%")

    def safe_in_txt(self, txt):
        datei = open(txt, 'a')
        if self.secondType != NoType:
            datei.write(
                f' {self.name}: {self.firstType.name}, {self.secondType.name},\n {self.stats.hp}, {self.stats.physattack}, {self.stats.physdef}, {self.stats.spezattack}, {self.stats.spezdef}, {self.stats.speed}, {self.level}\n')
            print(
                f'{self.name}: {self.firstType.name}, {self.secondType.name},\n {self.stats.hp}, {self.stats.physattack}, {self.stats.physdef}, {self.stats.spezattack}, {self.stats.spezdef}, {self.stats.speed}, {self.level}\n')
        else:
            datei.write(
                f' {self.name}: {self.firstType.name},\n {self.stats.hp}, {self.stats.physattack}, {self.stats.physdef}, {self.stats.spezattack}, {self.stats.spezdef}, {self.stats.speed}, {self.level}\n')
            print(
                f'{self.name}: {self.firstType.name},\n {self.stats.hp}, {self.stats.physattack}, {self.stats.physdef}, {self.stats.spezattack}, {self.stats.spezdef}, {self.stats.speed}, {self.level}\n')
        datei.close()


def get_pokemon_from_txt(txt):
    datei = open(txt, 'r', encoding="utf8")
    pokemon = datei.read()
    return pokemon
