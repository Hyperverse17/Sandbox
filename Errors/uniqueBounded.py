
import random
from datetime import datetime

dateTimeMark = datetime.now() #Objeto tipo date, time
sDateMarkFmt = dateTimeMark.strftime("%y%m%d") # Funcion para dar formato a objetos tipo date y date time. Genera string YY MM DD
sDateTimeMarkFmt = dateTimeMark.strftime("%y%m%d%H%M%S") # Genera string YY MM DD hh mm ss
maxIdlenght = 18
       
def timeMarkId(sPrefix):
    counter = 0
    while True: # Acciones a realizar cada que se invoque mediante next
        counter += 1
        sUniqueId = sPrefix + sDateTimeMarkFmt + str(counter).zfill(3)
        if len(sUniqueId) > maxIdlenght:
            sUniqueId = "..."     
            #break
        yield sUniqueId
            
prefix = input("Ingresa prefijo: ").upper()
uniqueId = timeMarkId(prefix)

for _ in range(0,100):
   try:
      print(next(uniqueId))
   except StopIteration:
       print("Error en la genearción de clave de rastreo")
       break

