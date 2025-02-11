
import functools
from typing import Union

logPath = "./Logging/logs/"
fileName = "log.txt"
filePointer = logPath + fileName

def logger(filePointer): # Permite recibir parámetros extr a(en este caso el filepointer)
    def decorator(func): # Decorador
        @functools.wraps(func) # sirve para que la función decorada conserve su identidad original (nombre, docstring, etc.). Sin él, la función decorada parecería ser la función wrapper en lugar de la original.
        def wrapper(*args, **kwargs): # un kwarg es una variable a la que se le da nombre funcion(variable1 = valor1, variable2 = valor2)
            result = func(*args, **kwargs) # En result se guarda el retorno de la función
            message = f"[LOG] {func.__name__} | args={args}, kwargs={kwargs} | Result: {result}" # Construcción del mensasje que se escribirá. N+otese el uso de func.__name__ (@functools.wraps)
            #print(message)
            with open(filePointer, "a") as file:
                file.write(message + "\n")
            return result
        return wrapper
    return decorator

@logger(filePointer)
def multiply(a:int, b:int) -> int:
    """Función que multiplica dos números enteros"""
    result = a * b
    return result

@logger(filePointer)
def divide(a:int, b:int) -> Union[int, float, None]:
    """Función que divide dos números enteros"""
    if b != 0:
        result = round((a / b),2)
    else:
        result = None

    return result
