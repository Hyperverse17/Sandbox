import random
coffeePouchLevel = 5
counter = 0
class coffeePouch:
    def Level():
        global coffeePouchLevel
        #coffeePouchLevel -= 1
        if coffeePouchLevel == 0:
            message = "Error: There's no more coffee"
            print(message)
            print()
        return coffeePouchLevel

class coffeeMachine():
    def Brew():
        global coffeePouchLevel
        coffeePouchLevel -= 1
        message = "Grinding coffee..."
        print(message)
        message = "Brewing..."
        print(message)

class coffeeCup:
    def Dispense():
        pass

    def Empty():
        global counter
        counter += 1
        values = [True,False]
        if counter == 1:
            value = False
        else:
            value = random.choice(values)

        if value == True:
            message = "Warning: Time to refill the cup"
            print(message)
            print()

        return value 

    def Fill(message):
        message = "Refilling..."
        print(message)
        print()

class me:
    def DrinkCoffee(message):
        message = "Now drinking coffee..."
        print(message)

    def GetSomeShitDone():
        message = "Now working..."
        print(message)
        print()

    def GetAngry():
        message = "Aaaargh!"
        print(message)
    