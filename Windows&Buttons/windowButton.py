
import tkinter as tk
import random

def randomColor():
    """Retorna un código de color aleatorio"""
    colors = ["#FF66CC", "#39FF14", "#4D4DFF", "#E0E722", "#FFAD00", "#D22730", "#DB3EB1"]
    chosenOne = random.choice(colors)
    return chosenOne

def rollingDice():
    """Simula un lanzamiento de dado"""
    RandomNumber = random.randint(1,6) 
    string = f"Dice result: {RandomNumber}"
    textFunction.config(text=string)

# Crear ventana principal
myWindow = tk.Tk()
myWindow.title("Titulo 1") # Este es literalmente el nombre de la ventana

# Estilo visual básico
myWindow.config(bg="#1e1e1e")
font = ("Courier", 14, "bold") # Tupla con las especificaciones que se usarán
font2 = ("Courier", 20, "bold") # Tupla con las especificaciones que se usarán

# Título 2
title2 = tk.Label(myWindow, text="Titulo 2", fg=randomColor(), bg="#1e1e1e", font=("Courier", 16, "bold"))
title2.pack(pady=10) # pady=n agrega n pixeles de separación arriba y abajo de la etiqueta

# fg > foreground (color de la fuente)
# bg > color del fondo
# #1e1e1e es un gris obscuro como el que usa VSCode
# Rosa Neón: #FF66CC 
# Verde neón: #39FF14
# Azul neón: #4D4DFF
# Amarillo neón: #E0E722
# Naranja neón: #FFAD00
# Rojo neón: #D22730
# Fucsia neón: #DB3EB1

# Título 3 con más parámetros
title3 = tk.Label(myWindow, text="Titulo 3", fg=randomColor(), bg="#1e1e1e", font=font, wraplength=400, justify="center")
title3.pack(pady=10)

# Título 4. Esta parte está estrechamente relacionada con el botón y la función definida al principio
textFunction = tk.Label(myWindow, text="", fg=randomColor(), bg="#1e1e1e", font=font2, wraplength=400, justify="center")
# Nótese que text = "", pero este parámetro del objeto textFunction es modificado dentro de la función definida al inicio. Obviamente el objeto textFunction debió haber sido definido antes de llamar a la función
textFunction.pack(pady=10)

# rollingDice() # Si la función se ejecuta en este momento y modificaría el valor del objeto textFunction

# Botón para generar nombre
myButton = tk.Button(myWindow, text="Click Here!", command=rollingDice, bg="#444", fg=randomColor(), font=font)
myButton.pack(pady=10)

# Ejecutar ventana con todos los parámetros cargados hasta el momento
myWindow.mainloop()


