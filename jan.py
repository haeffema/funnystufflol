class Type (object):
    def __init__(self,name):
        self.name=name
    weaknesses = []


Normal =Type("Normal")
Fighting=Type("Fighting")
Flying=Type("Flying")
Poison=Type("Poison")
Ground=Type("Ground")
Rock=Type("Rock")
Bug=Type("Bug")
Ghost=Type("Ghost")
Steel=Type("Steel")
Fire=Type("Fire")
Water=Type("Water")
Grass=Type("Grass")
Electric=Type("Electric")
Psychic=Type()
Ice = Type()
Dragon=Type()
Dark=Type()
Fairy=Type()

Normal.weaknesses =[Fighting,Poison]
print(Normal.weaknesses)