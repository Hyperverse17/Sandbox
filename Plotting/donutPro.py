
import matplotlib.pyplot as plt

# Datos para el gráfico
sizes = [25, 35, 20, 20]
labels = ['Category A', 'Category B', 'Category C', 'Category D']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Creación del gráfico de pastel
fig, ax = plt.subplots()
ax.pie(sizes, labels = labels, colors = colors, autopct = '%1.1f%%', startangle = 90, wedgeprops = {'width': 0.4}) # propiedades pro. Nótese cómo el último parámetro que se pasa a la función es un diccionario {}

# La relación de aspecto igual (equal) garantiza que el gráfico circular sea circular
ax.axis('equal')

plt.title('Donut Chart Pro')
plt.show()
