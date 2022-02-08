class Type(object):
    weaknesses = []
    resistances = []
    immunities = []

    def __init__(self, name):
        self.name = name

    def calculateEffectivity(self, type):
        effect = 1
        for z in self.immunities:
            if z == type:
                effect = 0
        for x in self.weaknesses:
            if x == type:
                effect = 2
        for y in self.resistances:
            if y == type:
                effect = 0.5
        return effect


Normal = Type('Normal')
Fighting = Type('Fighting')
Flying = Type('Flying')
Poison = Type('Poison')
Ground = Type('Ground')
Rock = Type('Rock')
Bug = Type('Bug')
Ghost = Type('Ghost')
Steel = Type('Steel')
Fire = Type('Fire')
Water = Type('Water')
Grass = Type('Grass')
Electric = Type('Electric')
Psychic = Type('Psychic')
Ice = Type('Ice')
Dragon = Type('Dragon')
Dark = Type('Dark')
Fairy = Type('Fairy')

# Weaknesses:

Normal.weaknesses = [Fighting]
Fighting.weaknesses = [Flying, Psychic, Fairy]
Flying.weaknesses = [Rock, Electric, Ice]
Poison.weaknesses = [Ground, Psychic]
Ground.weaknesses = [Water, Grass, Ice]
Rock.weaknesses = [Fighting, Ground, Water, Grass, Steel]
Bug.weaknesses = [Flying, Rock, Fire]
Ghost.weaknesses = [Ghost, Dark]
Steel.weaknesses = [Fighting, Ground, Fire]
Fire.weaknesses = [Rock, Ground, Water]
Water.weaknesses = [Electric, Grass]
Grass.weaknesses = [Flying, Poison, Bug, Fire, Ice]
Psychic.weaknesses = [Bug, Ghost, Dark]
Ice.weaknesses = [Fighting, Rock, Steel, Fire]
Dragon.weaknesses = [Ice, Dragon, Fairy]
Dark.weaknesses = [Fighting, Bug, Fairy]
Fairy.weaknesses = [Poison, Steel]

# Resistances:

Normal.resistances = [None]
Fighting.resistances = [Rock, Bug, Dark]
Flying.resistances = [Fighting, Bug, Grass]
Poison.resistances = [Fighting, Poison, Bug, Grass, Fairy]
Ground.resistances = [Poison, Rock]
Rock.resistances = [Normal, Flying, Poison, Fire]
Bug.resistances = [Fighting, Ground, Grass]
Ghost.resistances = [Poison, Bug]
Steel.resistances = [Normal, Flying, Rock, Bug, Steel, Grass, Psychic, Ice, Dragon, Fairy]
Fire.resistances = [Bug, Steel, Fire, Ice, Fairy]
Water.resistances = [Steel, Fire, Water, Ice]
Grass.resistances = [Ground, Water, Grass, Electric]
Electric.resistances = [Flying, Steel, Electric]
Psychic.resistances = [Fighting, Ice]
Dragon.resistances = [Fire, Water, Grass, Electric]
Dark.resistances = [Ghost, Dark]
Fairy.resistances = [Fighting, Bug, Dark]

# Immunities:

Normal.immunities = [Ghost]
Flying.immunities = [Ground]
Ground.immunities = [Electric]
Ghost.immunities = [Normal, Fighting]
Steel.immunities = [Poison]
Dark.immunities = [Psychic]
Fairy.immunities = [Dragon]

types = [Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electric, Psychic, Ice,
         Dragon, Dark, Fairy]
