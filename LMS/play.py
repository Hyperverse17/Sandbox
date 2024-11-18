
from matrix import *
from functions import *

print()
print(" ✨ Algoritmo de Mímimos Cuadrados 🚀")
print()

try:
    print()
    inputFile = input("Nombre del archivo de carga: ")
    mainMatrix = getFileData(inputFile)
    print()
    print("Procesando información 🔥")
    print()
    result = getMB(mainMatrix)
    print("Valor de M: " + str(result[0]))
    print("Valor de B: " + str(result[1]))
    
            
except:
    print()
    print("Something went wrong...")

finally:
    print()
    print("Fin del programa")
    print()

