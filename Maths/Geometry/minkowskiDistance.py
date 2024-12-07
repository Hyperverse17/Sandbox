

import numpy as np

def minkowski(x, y, p):
    """Devuelve la distancia de minkowski entre dos puntos dados 'x' e 'y' y p. En esta fórmula, x y y son los dos objetos que se están comparando, n es el número de atributos de los dos objetos y p es un parámetro que se utiliza para controlar la cantidad de influencia que cada atributo tendrá en el resultado."""
    return np.sum(np.abs(x - y) ** p) ** (1/p) # .sum() devuelve la suma de un array

# Usage
#Un array de NumPy es una estructura de datos que forma parte de la librería NumPy, la cual es una mezcla de Python y C que se utiliza para el análisis de datos y el cálculo numérico: Los arrays de NumPy son una alternativa a la programación tradicional en MATLAB. """
x = np.array([0, 0, 0])
y = np.array([1, 1, 1])

# Cálculo usando p = 3
distance = minkowski(x, y, p = 3)
print(distance)
