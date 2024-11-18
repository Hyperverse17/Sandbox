
import math

def getMB(mainMatrix):
    sigmaX       = 0
    sigmaY       = 0
    sigmax2      = 0
    SigmaXY      = 0
    matrixLenght = len(mainMatrix)
    n            = matrixLenght-1 # Se resta 1 para descontar la primer linea del archivo (header)
    result       = []

    for matrixRow in range(1, matrixLenght):
        dataRow = mainMatrix[matrixRow]
        x = float(dataRow[0])
        y = float(dataRow[1])
        sigmaX  += x
        sigmaY  += y
        sigmax2 += (x**2)
        SigmaXY += (x*y)

    M = ((n * SigmaXY) - (sigmaX * sigmaY)) / ((9 * sigmax2) - (abs(sigmaX)**2))
    B = ((sigmaY * sigmax2) - (sigmaX * SigmaXY)) / ((n * sigmax2) - (abs(sigmaX)**2))

    result.append(M)
    result.append(B)
    
    return(result)




