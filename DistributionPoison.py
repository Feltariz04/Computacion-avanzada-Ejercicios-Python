import math
import numpy as np

#Funcion factorial
def nfactorial(n):
    """ returns n! = n*(n-1)*...*1
    """
    if (n <= 1 ):
        return 1
    return n * nfactorial(n-1)

#Parametros
mu = 5
n = 50

def Poison(mu):
    def fn(n):
        return ((mu**n)*np.exp(-mu))/nfactorial(n)
    return fn

f = Poison(mu)

sumP = 0

for i in range(n+1):
    sumP += f(i)


print(f"La propabilidad de la muestra es: {f(n)}")
print(f"La suma de la propabilidades: {sumP}")
