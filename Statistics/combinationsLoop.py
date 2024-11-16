
import math

print()
total = int(input("Ingresa un limite: "))
for split in range(total+1):
    result = math.comb(total,split)
    print("las formas de tomar " + str(split) + " elementos de " + str(total)+" son: " + str(result))
    


