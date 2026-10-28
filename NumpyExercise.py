# Implement two ways to compute the NxN distance matrix for N points in 3D

import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

# Version loop
def distancia(x, y, z):
    n = len(x)
    d = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            d[i,j] = np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2+(z[i]-z[j])**2)
    return d



# Version vectorizado 
def distancia_vec(pts):
    A = pts[:,np.newaxis,:]
    B = pts[np.newaxis, :, :]

    delta = A-B

    delta2 = delta**2
    D2 = np.sqrt(np.sum(delta2, axis= 2))

    return D2


# Parametros para comparar
Ns = [200, 500, 1000]
Tloop = []
Tvec = []


for N in Ns:
    pts = np.random.random((N, 3))

    x = pts[:, 0]
    y = pts[:, 1]
    z = pts[:, 2]

    start = perf_counter(); D = distancia(x, y, z); t_loop = perf_counter() - start
    Tloop.append(t_loop)

    start = perf_counter(); D2 = distancia_vec(pts); t_vec = perf_counter() - start
    Tvec.append(t_vec)

#print(D2.shape)
#print(np.allclose(D, D2)) # demostrar si son las mismas
#print(np.allclose(D, D.T)) # debe demostrar que es simetrica 
#print(np.allclose(np.diag(D), 0)) #  que su diagonal sea nula

print("N:", Ns)
print("Tiempo con bucles:", Tloop)
print("Tiempo vectorizado:", Tvec)


# graficar para comparar
plt.plot(Ns, Tloop, marker= "o", label = "Bucles")
plt.plot(Ns, Tvec, marker= "o", label = "vectorizado")

plt.xlabel("Numeros de N")
plt.ylabel("Tiempo de ejecución")
plt.title("Comparacion de tiempos")
plt.legend()
plt.grid(True)

plt.show()