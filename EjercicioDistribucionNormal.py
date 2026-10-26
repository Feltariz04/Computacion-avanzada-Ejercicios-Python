# Ejercicio de la distribucion normal
# a) Generar \(n\) puntos aleatorios \((x,y)\), con coordenadas extraídas de una distribución normal de media \(0\) 
# y desviación típica \(1\). Después, calcular la distancia de cada punto al origen.

import random as rd
import math

puntos = []
distancia = []

# puntos aleatorios
for n in range(10):
    x = round(rd.gauss(0,1), 4)
    y = round(rd.gauss(0,1), 4)  
    f = (x, y)
    puntos.append(f)

# Distancias
for x, y in puntos:
    r = round(math.sqrt(x**2 + y**2), 4)
    distancia.append(r)

#print(distancia)

# b) Ordenar los puntos por su distancia al origen.

Pd = list(zip(puntos, distancia))
PdOrden = sorted(Pd, key= lambda elemento: elemento[1])

#print(Pd)
#print(PdOrden)


#c) Seleccionar los puntos que cumplan \(r>1\) y que estén en el primer cuadrante.
filtrados = []

for punto , r in PdOrden:
    x, y = punto
    
    if r > 1 and x > 0 and y > 0:
        filtrados.append((punto, r))

print(filtrados)