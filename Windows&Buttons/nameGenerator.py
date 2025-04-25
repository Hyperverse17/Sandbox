import tkinter as tk
import random

# Listas de palabras épicas
adjetivos = ["Abyssal", "Cryptic", "Malignant", "Chaotic", "Ethereal", "Obsidian", "Fractal", "Necrotic", "Pestilent", "Infinitesimal"]
sustantivos = ["Dominion", "Aeon", "Algorithm", "Monolith", "Codex", "Spiral", "Sanctum", "Void", "Matter"]
modificadores = ["of Entropy", "from Beyond", "of the Infinite Void", "of Oblivion", "of the 7th Singularity", "from the Black Hole", "of Infinity"]

# Función para generar el nombre
def generar_nombre():
    nombre = f"{random.choice(adjetivos)} {random.choice(sustantivos)} {random.choice(modificadores)}"
    etiqueta_nombre.config(text=nombre)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Metal Band Name Generator")

# Estilo visual básico
ventana.config(bg="#1e1e1e")
fuente = ("Courier", 14, "bold")

# Título
titulo = tk.Label(ventana, text="Metal Band Name Generator", fg="white", bg="#1e1e1e", font=("Courier", 16, "bold"))
titulo.pack(pady=10)

# Etiqueta para mostrar el nombre
etiqueta_nombre = tk.Label(ventana, text="", fg="#ff6666", bg="#1e1e1e", font=fuente, wraplength=400, justify="center")
etiqueta_nombre.pack(pady=20)

# Botón para generar nombre
boton = tk.Button(ventana, text="Generate Name", command=generar_nombre, bg="#444", fg="white", font=fuente)
boton.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
