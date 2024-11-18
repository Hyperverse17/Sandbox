
import math
import numpy as np
import matplotlib.pyplot as plt

def getMB(mainMatrix):
    sigmaX       = 0
    sigmaY       = 0
    sigmax2      = 0
    SigmaXY      = 0
    n            = len(mainMatrix)
    
    for matrixRow in range(0, n):
        global M
        global B
        dataRow = mainMatrix[matrixRow]
        x = float(dataRow[0])
        y = float(dataRow[1])
        sigmaX  += x
        sigmaY  += y
        sigmax2 += (x**2)
        SigmaXY += (x*y)

    M = ((n * SigmaXY) - (sigmaX * sigmaY)) / ((9 * sigmax2) - (abs(sigmaX)**2))
    B = ((sigmaY * sigmax2) - (sigmaX * SigmaXY)) / ((n * sigmax2) - (abs(sigmaX)**2))

def matrixPlot(mainmatrix):
    figure, ejes = plt.subplots()
    mainmatrix = np.array(mainmatrix)
    xValues = mainmatrix[:,0]
    yValues = mainmatrix[:,1]
    
    minX = int(min(xValues))
    maxX = int(max(xValues))

    xValues2 = []
    yValues2 = []

    for x in range(minX,maxX+1):
        y = (M * x) + B
        xValues2.append(x)
        yValues2.append(y)

    ejes.plot(xValues, yValues, marker='*', color='b', linestyle='', label='Puntos Originales')
    ejes.plot(xValues2, yValues2, marker='', color='g', linestyle='-', label='Aproximacion por Recta')

    ejes.set(xlabel='X', ylabel='Y', title='Aproximacion de puntos por Minimos Cuadrados')
    ejes.legend()
    
    plt.show()





