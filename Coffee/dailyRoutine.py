
from me import *
from coffee import *

# Daily Routine
while coffeePouch.Level() > 0:
    if coffeeCup.NoCoffeeLeft():
        coffeeCup.Fill(coffeeMachine.Brew())
    
    me.DrinkCoffee(coffeeCup.RunningOut())
    me.GetSomeTaskDone()
        
me.GetAngry()
#raise SystemError
