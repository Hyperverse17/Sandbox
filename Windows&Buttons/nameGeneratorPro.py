
import tkinter as tk

def name_style(text):
    if text != "":
        return text.capitalize() + " of the Fractal Abyss"
    else:
        etiqueta_guardado.config(text="⚠️ Debes ingresar alguna palabra clave")


def mostrar_nombre():
    nombre = entrada.get()
    resultado = name_style(nombre)
    if resultado:
        etiqueta_resultado.config(text=f"Tu banda se llama:\n{resultado}")
        ultimo_nombre.set(resultado)

def guardar_nombre():
    nombre = ultimo_nombre.get()
    if nombre:
        with open("nombres_banda.txt", "a", encoding="utf-8") as archivo:
            archivo.write(nombre + "\n")
        etiqueta_guardado.config(text="✅ Nombre guardado")
    else:
        etiqueta_guardado.config(text="⚠️ Nada que guardar")

# Ventana
ventana = tk.Tk()
ventana.title("Generador de Nombres de Banda")
ventana.config(bg="#002D74")

# Variables
ultimo_nombre = tk.StringVar() # Variable que se usa para guardar los nombres generados

# Widgets
etiqueta = tk.Label(ventana, text="Escribe tu palabra clave:", fg="white", bg="#002D74")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

frame_botones = tk.Frame(ventana, bg="#002D74")
frame_botones.pack(pady=10)

boton_generar = tk.Button(frame_botones, text="Generar", command=mostrar_nombre, bg="#A3C940")
boton_generar.pack(side=tk.LEFT, padx=5)

boton_guardar = tk.Button(frame_botones, text="Guardar", command=guardar_nombre, bg="#A3C940")
boton_guardar.pack(side=tk.LEFT, padx=5)

etiqueta_resultado = tk.Label(ventana, text="", fg="#A3C940", bg="#002D74", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=10)

etiqueta_guardado = tk.Label(ventana, text="", fg="white", bg="#002D74")
etiqueta_guardado.pack(pady=5)

ventana.mainloop()
