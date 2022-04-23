import random

class NewCharacter(object):
    def __init__(self, Name, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) :
        self.name = Name
        self.strength = Strength
        self.dexterity = Dexterity
        self.constitution = Constitution
        self.intelligence = Intelligence
        self.wisdom = Wisdom
        self.charisma = Charisma
        self.hitpoint = Constitution * 30 + 50

    def PrintPlayerStats(self):
        print("| ",'%-15s' % self.getName(), end = "")
        print('%-10s' % "Strength:", '%-4s' % self.strength, end = "")
        print('%-10s' % "Dexterity:", '%-4s' % self.dexterity, end = "")
        print('%-10s' % "Constitution:", '%-4s' % self.constitution, end = "")
        print('%-10s' % "Intelligence:", '%-4s' % self.intelligence, end = "")
        print('%-10s' % "Wisdom:", '%-4s' % self.wisdom, end = "")
        print('%-10s' % "Charisma:", '%-4s' % self.charisma, end = "")
        print('%-10s' % "Hitpoint:", '%-4s' % self.hitpoint, end = " |\n")
        
    def PrintHitpoints(self):
        print("| ",'%-15s' % self.getName(), end = " ")
        print( '%-10s' % "Hitpoint:", self.hitpoint, end = " |\n")

    def Attack(self):
        print("| ",'%-15s' % "Note: ", self.getName(), "attacked ",end = "")
        return random.randint(1, self.strength)
   
    def Defense(self, value):    
        print(self.getName()+"!")
        if(value > self.dexterity):
            self.hitpoint -= value 
    
    def Heal(self):
        self.hitpoint += random.randint(1, self.constitution)

    def getName(self):
        return self.name

class MagicCharacter(NewCharacter):
    pass