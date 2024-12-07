
# check wether a given number is even or odd using recursion

def isEven(number):
    if number == 0:
        return True
    elif number == 1:
        return False
    else:
        return(isEven(number - 2)) # Recursión

try: 
    print()
    number = int(input("Ingresa un numero natural: "))
    even = isEven(number)

    if even == True:
        print("El número "+ str(number) + " es par")
    else:
        print("El número "+ str(number) + " es impar")
except(RecursionError):
    print("Error: No es posible tanta recursión")

