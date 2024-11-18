
from matrix import *
from functions import *

print()
print(" ✨ Algoritmo de Mímimos Cuadrados 🚀")
print()

try:
    print()
    inputFile = input("Nombre del archivo de carga: ")
    if inputFile == "":
        inputFile = "input"
        
    mainMatrix = getFileData(inputFile)
    print()
    print("Procesando información 🔥")
    print()
    getMB(mainMatrix)
    matrixPlot(mainMatrix)
    
except:
    print()
    print("Something went wrong...")

finally:
    print()
    print("Fin del programa")
    print()

