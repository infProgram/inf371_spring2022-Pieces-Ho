import random

class Character(object):
    def __init__(self, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) :
        self.strength = Strength
        self.dexterity = Dexterity
        self.constitution = Constitution
        self.intelligence = Intelligence
        self.wisdom = Wisdom
        self.charisma = Charisma
        self.hitpoint = Constitution * 30 + 50

    def PrintPlayerStats(self):
        print("Strength", self.strength)
        print("Dexterity", self.dexterity)
        print("Constitution", self.constitution)
        print("Intelligence", self.intelligence)
        print("Wisdom", self.wisdom)
        print("Charisma", self.charisma)
        
    def PrintHitpoints(self):
        print("Hitpoint", self.hitpoint)
    def Attack(self):
        return random.randint(1, self.strength)
    def Defense(self, value):
        v = value
        v = random.randint(1, 20)
        if(v > self.dexterity):
            pass


    def Heal(self):
        pass

if __name__ == "__main__":
    pass



    




