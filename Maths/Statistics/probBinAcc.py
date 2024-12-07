

from functions import binProbAcc

print()
try:
    """Una distribución binomial describe el número de veces que aparece el éxito en los n experimentos realizados. Dado que el número de éxitos obtenidos es un valor aleatorio, una distribución binomial se describe dando las probabilidades de que el éxito se produzca precisamente k veces en los n ensayos."""
    n = int(input("Total de ensayos                 : "))
    x = int(input("Cantidad minima de exitos        : "))
    P = float(input("Probabilidad de Exito          : "))

    result = binProbAcc(n,x,P) #!
    resultFmt = round(result*100,2)

    print()
    print("La probabilidad de que en " + str(n) + " ensayos haya al menos " + str(x) + " exitos es: " + str(result) + " %")


    
except:
    print()
    print("Algo salio mal con alguno de los valores introducidos")

finally:
    print()
    print("Fin del programa")
    print()
