import random

class NewCharacter(object):
    def __init__(self, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) :
        self.strength = Strength
        self.dexterity = Dexterity
        self.constitution = Constitution
        self.intelligence = Intelligence
        self.wisdom = Wisdom
        self.charisma = Charisma
        self.hitpoint = Constitution * 30 + 50

    def PrintPlayerStats(self):
        print('%-10s' % "Strength:", '%-4s' % self.strength, end = "")
        print('%-10s' % "Dexterity:", '%-4s' % self.dexterity, end = "")
        print('%-10s' % "Constitution:", '%-4s' % self.constitution, end = "")
        print('%-10s' % "Intelligence:", '%-4s' % self.intelligence, end = "")
        print('%-10s' % "Wisdom:", '%-4s' % self.wisdom, end = "")
        print('%-10s' % "Charisma:", '%-4s' % self.charisma, end = "")
        print('%-10s' % "Hitpoint:", '%-4s' % self.hitpoint, end = " |\n")
        
    def PrintHitpoints(self):
        print('%-10s' % "Hitpoint:", self.hitpoint, end = " |\n")

    def Attack(self):
        return random.randint(1, self.strength)
   
    def Defense(self, value):     
        value = random.randint(1, 20)
        if(value > self.dexterity):
            self.hitpoint -= value 
    
    def Heal(self, value):
        self.hitpoint += value

if __name__ == "__main__":
    print("START GAME".center(140,"-"))
    Alice = NewCharacter(7, 18, 10, 13, 14, 17)
    Ben = NewCharacter(18, 11, 17, 10, 9, 12)
    Monster = NewCharacter(15, 5, 10, 3, 3, 3)

    print("| ",'%-15s' % "Alice: ", end = "")
    Alice.PrintPlayerStats()
    print("| ",'%-15s' % "Ben: ", end = "")
    Ben.PrintPlayerStats()
    print("| ",'%-15s' % "Monster: ", end = "")
    Monster.PrintPlayerStats()

    print("FIGHT".center(140,"-"))
    Alice.Defense(Monster.Attack())
    Ben.Defense(Monster.Attack())
    print("FIGHT OVER".center(140,"-"))
    print("| ",'%-15s' % "Alice: ", end = " ")
    Alice.PrintHitpoints()
    print("| ",'%-15s' % "Ben: ", end = " ")
    Ben.PrintHitpoints()
    print("HEAL BEN".center(140,"-"))
    Ben.Heal(5)
    print("| ",'%-15s' % "Alice", end = " ")
    Alice.PrintHitpoints()
    print("| ",'%-15s' % "Ben", end = " ")
    Ben.PrintHitpoints()