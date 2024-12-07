
import math

print()
print("Combinaciones ")
print()
try:
    total = int(input("Ingresa el total de elementos: "))
    split = int(input("Ingresa la cantidad a tomar: "))
    if split > total:
        raise SystemError
    result = math.comb(total,split)
    print("las formas de tomar " + str(split) + " elementos de " + str(total)+" son: " + str(result))

except(ValueError):
    print()
    print("Error: Sólo valores enteros")

except(SystemError):
    print()
    print("Hmmm, el resultado es 0")

print()

