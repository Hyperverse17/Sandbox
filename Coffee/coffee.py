import random

coffeePouchLevel = 2
coffeeCupLevel   = 3
class coffeePouch:
    def Level():
        global coffeePouchLevel
        if coffeePouchLevel == 0:
            message = "Error: There's no more coffee"
            print(message)
            print()
        return coffeePouchLevel

class coffeeMachine():
    def Brew():
        global coffeePouchLevel
        coffeePouchLevel -= 1
        message = "Grind"
        print(message)
        message = "Brew"
        print(message)

class coffeeCup:
    def RunningOut():
        global coffeeCupLevel
        coffeeCupLevel -= 1
        
    def NoCoffeeLeft():
        global coffeeCupLevel
        if coffeeCupLevel == 0:
            value = True
            message = "Warning: Time to brew some coffee"
            print(message)
            print()
        else:
            value = False
            
        return value
    
    def Fill(message):
        global coffeeCupLevel
        coffeeCupLevel = 3
        message = "Refill"
        print(message)
        print()

    