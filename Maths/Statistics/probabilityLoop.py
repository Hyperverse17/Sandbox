
from functions import binProbability

print()
try:
    """Una distribución binomial describe el número de veces que aparece el éxito en los n experimentos realizados. Dado que el número de éxitos obtenidos es un valor aleatorio, una distribución binomial se describe dando las probabilidades de que el éxito se produzca precisamente k veces en los n ensayos."""
    n = int(input("Total de ensayos        : "))
    P = float(input("Probabilidad de Exito : "))
    print()
    accumulate = 0
    for k in range(n+1):
        result = binProbability(n,k,P)
        accumulate += result
        resultFmt = round(result*100,2)
        print("P(" + str(k)+ " exitos en " + str(n)+" ensayos) = " + str(resultFmt))
    
    print()
    print(accumulate)
        
except:
    print()
    print("Algo salio mal con alguno de los valores introducidos")

finally:
    print()
    print("Fin del programa")
    print()
