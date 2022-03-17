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
        pass      
    def PrintHitpoints(self):
        pass
    def Attack(self):
        pass
    def Defense(self):
        pass
    def Heal(self):
        pass

if __name__ == "__main__":
    pass


    




