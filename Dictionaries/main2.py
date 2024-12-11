
people=[{"name":"Otelo", "age":33},{"name":"Valeria","age":28}]

# Imprime los diccionarios
for prueba in people:
  print(prueba)

print("----------------------")
# Imprime nombres
for prueba in people:
  print (prueba["name"])
  # Imprime las llaves de cada diccionario
  for llave in prueba:
    print(llave)

print("----------------------")
# Imprime los elementos llave-valor de cada diccionario
for prueba in people:
  for llave, value in prueba.items():
    print(llave,":",value)

# Método Keys

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
