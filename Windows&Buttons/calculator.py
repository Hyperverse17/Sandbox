
import tkinter as tk

def suma():
    a = int(entry1.get()) # De esta forma se extrae lo ingresado en los objetos entry
    b = int(entry2.get())
    c = a + b
    result.config(text=str(c)) # De esta forma se asigna texto a la etiqueta previamente creada
    symbol1.config(text="+")

def resta():
    a = int(entry1.get())
    b = int(entry2.get())
    c = a - b
    result.config(text=str(c))
    symbol1.config(text="-")

def mult():
    a = int(entry1.get())
    b = int(entry2.get())
    c = a * b
    result.config(text=str(c))
    symbol1.config(text="x")

def div():
    a = int(entry1.get())
    b = int(entry2.get())
    if b != 0:
        c = round((a / b),2)
        result.config(text=str(c))
    else:
        equal.config(text="!")
        result.config(text="El divisor debe ser distinto a cero!")
    
    symbol1.config(text="/")

# Propiedades de colores
white = "#FFFFFF"
blue1 = "#0093D0" #Azul bx+
green1 = "#B5D334" #Verde bx+

foreground1 = blue1

background1 = white
background2 = green1

#"#1e1e1e" gris vscode


# Creación de la ventana
myWindow = tk.Tk()
myWindow.title("Calculadora Pro") # Este es literalmente el nombre de la ventana

# Estilo visual básico
myWindow.config(bg=background1) # bg es el color de fondo
mainTitle = ("Arial", 16, "bold") # Tupla con las especificaciones que se usarán
font1 = ("Arial", 12, "bold") # Tupla con las especificaciones que se usarán

etiqueta1 = tk.Label(myWindow, text="Ingresa dos números enteros y elige una opción: ", fg=blue1, bg=background1, font=mainTitle)
etiqueta1.pack(pady=20) # pad sobre el eje y

# Frame para entradas y resultados
resultsFrame = tk.Frame(myWindow, bg=background1)
resultsFrame.pack(pady=1)

# Entrada de información 
entry1 = tk.Entry(resultsFrame, fg=foreground1, bg=background1, font=font1, width=5) # width es la cantidad de caracteres que se recibirán
entry1.pack(side=tk.LEFT, padx=3)

# Símbolo de operación
symbol1 = tk.Label(resultsFrame, text=" ", fg=foreground1, bg=background1, font=font1)
symbol1.pack(side=tk.LEFT, padx=3)

entry2 = tk.Entry(resultsFrame, fg=foreground1, bg=background1, font=font1, width=5)
entry2.pack(side=tk.LEFT, padx=3)

# Símbolo =
equal = tk.Label(resultsFrame, text="=", fg=foreground1, bg=background1, font=font1)
equal.pack(side=tk.LEFT, padx=3)

# Mensaje de resultado
result = tk.Label(resultsFrame, text="", fg=foreground1, bg=background1, font=font1)
result.pack(side=tk.LEFT, padx=3)

# Creación de un contenedor para albergar varios botones
buttonFrame = tk.Frame(myWindow, bg=background1)
buttonFrame.pack(pady=10)

# Botones para operar
sumButton = tk.Button(buttonFrame, text="Suma", command=suma, bg=background2, fg=foreground1, font=font1)
sumButton.pack(side=tk.LEFT, padx=5) # Pad sobre el eje x

resButton = tk.Button(buttonFrame, text="Resta", command=resta, bg=background2, fg="#E0E722", font=font1)
resButton.pack(side=tk.LEFT, padx=5)

multButton = tk.Button(buttonFrame, text="Multiplica", command=mult, bg=background2, fg="#E0E722", font=font1)
multButton.pack(side=tk.LEFT, padx=5)

divButton = tk.Button(buttonFrame, text="Divide", command=div, bg=background2, fg="#E0E722", font=font1)
divButton.pack(side=tk.LEFT, padx=5)

# Ejecutar ventana con todos los elementos creados hasta el momento
myWindow.mainloop()
