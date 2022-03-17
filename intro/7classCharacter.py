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
        print("Strength:", self.strength, end = "\t")
        print("Dexterity:", self.dexterity, end = "\t")
        print("Constitution:", self.constitution, end = "\t")
        print("Intelligence:", self.intelligence, end = "\t")
        print("Wisdom:", self.wisdom, end = "\t")
        print("Charisma:", self.charisma, end = "\t")
        print("Hitpoint:", self.hitpoint)
        
    def PrintHitpoints(self):
        print("Hitpoint:", self.hitpoint)

    def Attack(self):
        return random.randint(1, self.strength)
   
    def Defense(self, value):     
        value = random.randint(1, 20)
        if(value > self.dexterity):
            self.hitpoint -= value 
    
    def Heal(self, value):
        self.hitpoint += value

if __name__ == "__main__":
    Alice = Character(7, 18, 10, 13, 14, 17)
    Ben = Character(18, 11, 17, 10, 9, 12)
    Monster = Character(15, 5, 10, 3, 3, 3)
    print("Alice stats:")
    Alice.PrintPlayerStats()
    print("Ben stats:")
    Ben.PrintPlayerStats()
    print("Monster stats:")
    Monster.PrintPlayerStats()

    print("---FIGHT---")
    Alice.Defense(Monster.Attack())
    Ben.Defense(Monster.Attack())
    print("---FIGHT OVER---")
    print("Alice", end = " ")
    Alice.PrintHitpoints()
    print("Ben", end = " ")
    Ben.PrintHitpoints()
    print("---HEAL BEN---")
    Ben.Heal(5)
    print("Alice", end = " ")
    Alice.PrintHitpoints()
    print("Ben", end = " ")
    Ben.PrintHitpoints()




    




