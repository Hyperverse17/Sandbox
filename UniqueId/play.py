
import unique

uniqueBaseId1 = unique.timeMarkId("OGALICIA") #Se crea objeto generador invocando a la función
uniqueBaseId2 = unique.bitsNoId(32) #Se crea objeto generador invocando a la función

print()
for _ in range(0,100):
    print(next(uniqueBaseId1))
    print(next(uniqueBaseId2))
    print()
print()
