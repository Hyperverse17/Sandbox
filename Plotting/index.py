
import numpy as np
import matplotlib.pyplot as plt

figura, ejes = plt.subplots() #Primero se define el marco y los ejes. Todo el gráfico estará contenido dentro de fig

xValues1 = [1,2,3,4,5]
yValues1 = [3,4,5,6,7] # y = x+2

xValues2 = [3,4,5,6,7]
yValues2 = [9,11,13,15,17] # y = 2x+3

ejes.plot(xValues1,yValues1) # Una vez definidos los ejes , se puede graficar pares ordenados con el método plot de ax
ejes.plot(xValues2,yValues2) # El método plot se puede invocar n veces

# plt.show()  # Usa siempre este comando para que el gráfico aparezca

# Se pueden agregar marcadores y otros detalles a los gráficos:

ejes.plot(xValues2,yValues2, marker = 'o', color = 'b', linestyle = '--', label = 'y = 2x+3')
plt.show()  # Usa siempre este comando para que el gráfico aparezca
