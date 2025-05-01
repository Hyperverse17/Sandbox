import tkinter as tk
import random

# Listas de palabras épicas
adjetivos = ["Abyssal", "Cryptic", "Malignant", "Chaotic", "Ethereal", "Obsidian", "Fractal", "Necrotic", "Pestilent", "Geometric", "Infinitesimal", "Complex", "Dark", "Negative", "Dissonant", "Mortal", "Digital", "Nuclear", "Radiactive", "Accelerating", "Chemical"]
sustantivos = ["Dominion", "Aeon", "Algorithm", "Monolith", "Codex", "Spiral", "Sanctum", "Void", "Matter", "Spirit", "Theory", "Darkness", "Noise", "Vector", "Technology", "Density", "Gravity", "Implosion", "Deformity", "Radiation", "Emanations"]
modificadores = ["of Entropy", "from Beyond", "of the Infinite Void", "of Oblivion", "of the 7th Singularity", "from the Black Hole", "of Infinity", "from Chernobyl"]

# Función para generar el nombre
def generar_nombre():
    nombre = f"{random.choice(adjetivos)} {random.choice(sustantivos)} {random.choice(modificadores)}"
    etiqueta_nombre.config(text=nombre)
    ultimo_nombre.set(nombre)
    etiqueta_resultado.config(text="")

def guardar_nombre():
    nombre = ultimo_nombre.get()
    if nombre:
        with open("nombres_banda.txt", "a", encoding="utf-8") as archivo:
            archivo.write(nombre + "\n")
            etiqueta_resultado.config(text="It Rocks! 💀")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Metal Band Name Generator")

# Estilo visual básico
ventana.config(bg="#1e1e1e")
fuente = ("Courier", 14, "bold")

# Variable que se usa para guardar los nombres generados
ultimo_nombre = tk.StringVar() # Este tipo de objetos deben crearse después de la ventana principal

# Título
titulo = tk.Label(ventana, text="Metal Band Name Generator", fg="white", bg="#1e1e1e", font=("Courier", 16, "bold"))
titulo.pack(pady=10)

# Etiqueta para mostrar el nombre
etiqueta_nombre = tk.Label(ventana, text="", fg="#ff6666", bg="#1e1e1e", font=fuente, wraplength=400, justify="center")
etiqueta_nombre.pack(pady=20)

# Frame para los botones
buttonFrame = tk.Frame(ventana, bg="#1e1e1e")
buttonFrame.pack(pady=1)

# Botón para generar nombre
boton = tk.Button(buttonFrame, text="Generate Name", command=generar_nombre, bg="#444", fg="white", font=fuente)
boton.pack(side=tk.LEFT, padx=3)

# Botón para guardar nombre
boton = tk.Button(buttonFrame, text="Save", command=guardar_nombre, bg="#444", fg="white", font=fuente)
boton.pack(side=tk.LEFT, padx=3)

etiqueta_resultado = tk.Label(ventana, text="", fg="white", bg="#1e1e1e", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
