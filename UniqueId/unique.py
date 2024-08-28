import random
from datetime import datetime

dateTimeMark = datetime.now() #Objeto tipo date, time
sDateMarkFmt = dateTimeMark.strftime("%y%m%d") # Funcion para dar formato a objetos tipo date y date time. Genera string YY MM DD
sDateTimeMarkFmt = dateTimeMark.strftime("%y%m%d%H%M%S") # Genera string YY MM DD hh mm ss

def bitsNoId(bitsNo):
    seed = random.getrandbits(bitsNo) #Basicamente la cantidad de bits determina la longitud del numero generado
    while True:
       seed += 1 # Colocar un contador de esta forma asegura que cada que se invoque la funcion mediante next, no regrese dos valores iguales  
       sUniqueId = sDateMarkFmt + str(seed)
       yield sUniqueId # Se usa dentro de una funcion cuando no se pone Return. Hace que la funcion se comporte de manera distinta, parece que esta ligado a la funcion next
       
def timeMarkId(sPrefix):
    counter = 0
    while True: # Acciones a realizar cada que se invoque mediante next
       counter += 1
       sUniqueId = sPrefix + sDateTimeMarkFmt + str(counter).zfill(4)
       yield sUniqueId # Se usa dentro de una funcion cuando no se pone Return. Hace que la funcion se comporte de manera distinta, parece que esta ligado a la funcion next
       
