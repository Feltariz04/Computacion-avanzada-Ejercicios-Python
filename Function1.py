"""Define a function to compute the mean and the variance of a list of numbers, without numpy. Check the result with numpy."""

import numpy as np

Datos = [2, 3, 4, 2, 7, 6, 4, 2, 6, 8]

#Funcion de la media
def mean(x):
    suma = 0
    media = 0

    for i in range(len(x)):
        suma += x[i]

    N = len(x)
    media = suma/N

    return media

# Varianza de los datos
def Varianza(x, xm):
    suma = 0
    N = len(x)

    for i in range(len(x)):
        suma += (x[i] - media)**2

    Var2 = suma/(N-1)

    return Var2

media = mean(Datos)
var = Varianza(Datos, media)


#funcion de numpy
medianumpy = np.mean(Datos)
varnumpy = np.var(Datos, ddof=1)

print(f"Resultado media de Numpy: {medianumpy}")
print(f"Resultado media de function: {media}")

print(f"Resultado Varianza de Numpy: {varnumpy:.3f}")
print(f"Resultado Varianza de function: {var:.3f}")
