
import random

class me:
    def DrinkCoffee(message):
        message = "Now drinking coffee"
        print(message)

    def GetSomeTaskDone():
        tasks = ["Working","Studying","Playing","Coding","Being"]
        message = "While " + str(random.choice(tasks)) + "..."

        print(message)
        print()

    def GetAngry():
        message = "Aaaargh!"
        print(message)
        print()
