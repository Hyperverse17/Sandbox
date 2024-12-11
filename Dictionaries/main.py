
planet3 = {
    "name" : "Earth",
    "satelites" : 1
}

planet4 = {
    "name" : "Mars",
    "satelites" : 2
}

planet5 = {
    "name" : "Jupiter",
    "satelites" : 79
}

# Las llaves no necesariamente deben ser strings

numbers = {
    1:"Uno!",
    2:"Dos!",
    3:"Tres!"
}

# Uso del método get y corchetes para obtener información
number1 = planet4["satelites"]
print(number1)

number2 = planet5.get("satelites")
print(number2)

first = numbers.get(1)
print(first)

# Uso del método update para modificar información existente
print(planet3["name"])

planet3.update({"name":"Earth C-137"})
print(planet3["name"])

# Al inicializar un diccionario no es necesario incluir claves desde el principio
myDict = {
    
}

# Es posible agregar claves sobre la marcha:
myDict["key1"] = "NewValue1"
print(myDict["key1"])

myDict["key2"] = "NewValue2"
myDict["key3"] = "NewValue3"

# Es posible eliminar claves con el método pop
myDict.pop("key2")

print(myDict)

planet3["orbitalPeriod"] = 365
planet4["orbitalPeriod"] = 686.97
planet5["orbitalPeriod"] = 4332.59

print(planet3)

# Datos complejos: Los diccionarios pueden almacenar cualquier tipo de datos, incluidos otros diccionarios:

planet3["diameter"] = { #Diccionario anidado.
    "equatorial":12756,
    "polar":12714
}

planet4["diameter"] = { #Diccionario anidado.
    "equatorial":6794,
    "polar":6750
}

# Para acceder a diccionarios anidados
print(planet3["diameter"]["polar"])

# O con el método get
print(planet4.get("diameter""polar"))

