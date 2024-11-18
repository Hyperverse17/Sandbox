
import csv
from properties import *

mainMatrix = []
def getFileData(fileName):
    """procesa un archivo de entrada .csv y devuelve la información en una matriz"""
    mainFileName = inPath + fileName + sExt1
    with open(mainFileName,'r') as csvfile:
        matrixInFile = csv.reader(csvfile)
        for rRow in matrixInFile:
            mainMatrix.append(rRow)
    
    return mainMatrix
