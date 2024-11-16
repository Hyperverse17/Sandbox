# Daily Routine
from coffee import *

while coffeePot.Level() > 0:
    if coffeeCup.Empty():
        coffeeCup.Fill(coffeePot)

    coffeeCup.Drink()
    work.GetSomeStDone()
    
me.GetAngry()
