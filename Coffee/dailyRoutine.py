# Daily Routine
from coffee import *

# Daily Routine
while coffeePouch.Level() > 0:
    if coffeeCup.Empty():
        coffeeCup.Fill(coffeeMachine.Brew())

    me.DrinkCoffee(coffeeCup.Dispense())
    me.GetSomeShitDone()

me.GetAngry()

