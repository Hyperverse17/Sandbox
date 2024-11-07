
import os

print()
counter = 0
while True:
    try:
        password = input("Ingresa la palabra secreta: ")
        if password == "pez":
            os.system("cls")
            print("Bienvenido! ")
            break
        else:
            counter += 1
            print("Numero de intentos restantes: " + str(3-counter))
    
        if counter >= 3:
            raise SystemError # raise SystemError # Esta es una forma de forzar a que ocurra un error en específico (para este ejemplo se usa systemError, pero se puede invocar cualquiera).
        
    except SystemError: # Gestión del error invocado
        os.system("cls")
        print("Error: Numero de intentos agotado!")
        break

    finally:
        pass

