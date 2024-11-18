
import csv
from properties import *


def getFileData(fileName):
    """procesa un archivo de entrada .csv y devuelve la información en una matriz"""
    mainMatrix = []
    
    mainFileName = inPath + fileName + sExt1
    with open(mainFileName,'r') as csvfile:
        matrixInFile = csv.reader(csvfile)
        for row in matrixInFile:
            floatRow   = []
            for value in row:
                floatRow.append(float(value))

            mainMatrix.append(floatRow)
    
    return mainMatrix
