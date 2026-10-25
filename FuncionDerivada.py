# funcion de la derivada

import math
import numpy as np

def derivative(f, h = 1e-5, method = "central"):
    def df(x):
        if method == "forward":
            return (f(x+h)-f(x))/(h)
        elif method == "central":
            return (f(x+h)-f(x-h))/(2*h)
        else:
            raise ValueError("Medoto no valido")
    return df

dsin_central = derivative(math.sin, method="central")
dsin_forward = derivative(math.sin, method="forward")
fcos = math.cos(1)

diference1 = np.abs(dsin_central(1) - fcos)/fcos * 100
diference2 = np.abs(dsin_forward(1) - fcos)/fcos * 100

print(f"Derivada del seno por el metodo central evaluada en x = 1 : {dsin_central(1):.14f} Error de : {diference1:.14f}")
print(f"Derivada del seno por el metodo forward evaluada en x = 1 : {dsin_forward(1):.14f} Error de : {diference2:.14f}")
print(f"Valor del coseno en x = 1 : {fcos:.14f}")