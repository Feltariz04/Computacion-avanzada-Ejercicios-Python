#1. Generar un paseo aleatorio: utilizar la función random_walk que aparece en la sección 6 de tus apuntes.
#2. Simular 1000 paseos: cada paseo debe tener 100 pasos.
#3. Calcular el promedio del cuadrado de la posición final: para cada paseo, obtener \(x_N^2\) 
# y después calcular la media de los 1000 resultados:
#\[
#\langle x_N^2\rangle = \frac{1}{M}\sum_{i=1}^{M}(x_N^{(i)})^2
#\]
#4. Comparar con la teoría: el valor esperado es \(N=100\).

import random as rd
import itertools

M = 1000 # Número de paseo
N = 100 #Pasos por paseo

def random_walk(x0=0, p=0.5):
    """ infinite 1D random walk: yields the successive positions of the walker
    """
    x = x0
    while True:
        yield x
        x += 1 if rd.random() < p else -1

cuadrado = []

for i in range(M):
    paseo = list(itertools.islice(random_walk(), N+1)) 

    x_final = paseo[-1]
    x2 = x_final**2

    cuadrado.append(x2)

media = sum(cuadrado)/len(cuadrado)

print(f"Media experimental: {media}")
print(f"Valor teorico: {N}")