
from functions import *
print()
try:
    """Una distribución binomial describe el número de veces que aparece el éxito en los n experimentos realizados. Dado que el número de éxitos obtenidos es un valor aleatorio, una distribución binomial se describe dando las probabilidades de que el éxito se produzca precisamente k veces en los n ensayos."""
    n = int(input("Total de ensayos        : "))
    k = int(input("Casos de exito          : "))
    P = float(input("Probabilidad de Exito : "))
    result = binProbability(n,k,P)
    print()
    print("La probabilidad es del: " + str(round(result*100,2)) + " %")

except:
    print()
    print("Algo salio mal con alguno de los valores introducidos")

finally:
    print()
    print("Fin del programa")

