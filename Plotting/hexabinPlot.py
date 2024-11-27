import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000) # Devuelve una muestra (o muestras) de la distribución “normal estándar”
y = np.random.randn(1000)

colormaps = ['cool']

plt.figure(figsize=(15, 15))

for i, cmap in enumerate(colormaps, 1): # Es una formas de extraer valores de un arreglo
    plt.subplot(4,3,i)
    plt.hexbin(x, y, gridsize = 30, cmap = cmap)
    plt.colorbar(label = 'Density')
    plt.title(f'Colormap: {cmap}')

plt.tight_layout()
plt.show()
    