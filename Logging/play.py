
import random
from functions import *

x: int = random.randint(0,99)
y: int = random.randint(0,99)

print()
print(f"El resultado de {x} x {y} es: {multiply(x,y)}")
print(f"El resultado de {x} / {y} es: {divide(x,y)}")
print()
