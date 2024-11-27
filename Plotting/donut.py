
import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels = labels, autopct='%1.1f%%') # Esto por sí solo genera una gráfica de pastel (A)
circle = plt.Circle((0, 0), 0.8, color = 'white') # Esto genera un círculo blanco (B)
plt.gca().add_artist(circle) # Con esta instrucción se añade el círculo blanco al gráfico A
plt.title('Donut Chart')
plt.show()
