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
Psychic=Type("Psychic")
Ice = Type("Ice")
Dragon=Type("Dragon")
Dark=Type("Dark")
Fairy=Type("Fairy")

Normal.weaknesses =[Fighting]
Fighting.weaknesses =[Flying,Psychic,Fairy]
Flying.weaknesses =[Rock,Electric,Ice]
Poison.weaknesses =[Ground,Psychic]
Ground.weaknesses =[Water,Grass,Ice]
Rock.weaknesses =[Fighting,Ground,Water,Grass,Steel]
Bug.weaknesses =[Flying,Rock,Fire]
Ghost.weaknesses =[Ghost,Dark]
Steel.weaknesses =[Fighting,Ground,Fire]
Fire.weaknesses =[Rock,Ground,Water]
Water.weaknesses =[Electric,Grass]
Grass.weaknesses =[Flying,Poison,Bug,Fire,Ice]
Psychic.weaknesses =[Bug,Ghost,Dark]
Ice.weaknesses =[Fighting,Rock,Steel,Fire]
Dragon.weaknesses =[Ice,Dragon,Fairy]
Dark.weaknesses =[Fighting,Bug,Fairy]
Fairy.weaknesses =[Poison,Steel]

