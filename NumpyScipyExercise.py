# ejecicio numero 2 scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, optimize

np.random.seed(42)

#funcion de la señal
def gauss_model(x, p):
    A, mu1, sigma1, mu2, sigma2 = p
    return A * np.exp(-((x-mu1)**2)/(2*sigma1**2)) + 0.7 * np.exp(-((x-mu2)**2)/(2*sigma2**2))

# variables de la señal
x = np.linspace(0, 1, 500)
p_true = [1, 0.30, 0.035, 0.70, 0.06]
y_true = gauss_model(x, p_true)

# funcion ruido con una muestra de 500
sigma_noise = 0.1
e = np.random.normal(0, sigma_noise, size=len(x))
y_noise = y_true + e

# funcion riudo con una muestra seleccionada removiendo el 40%
n_keep = int(0.6*len(x))
indices = np.random.choice(len(x), size=n_keep, replace=False)
indices = np.sort(indices)

x_sample = x[indices]
y_sample = y_noise[indices]

# interpolacion linear/cubica , smoothing spline, basis regression
f_linear = interpolate.interp1d(x_sample, y_sample, kind="linear", bounds_error=False,
    fill_value="extrapolate")
y_linear = f_linear(x)

f_cubica = interpolate.interp1d(x_sample, y_sample, kind="cubic", bounds_error=False,
    fill_value="extrapolate")
y_cubica = f_cubica(x)

spline = interpolate.UnivariateSpline(x_sample, y_sample, s=len(x_sample)*sigma_noise**2)
y_spline = spline(x)


def gaussian_basis(x, centers, width):
    return np.exp(
        -((x[:, None] - centers[None, :])**2)
        / (2 * width**2)
    )

# Regresión con base gaussiana
centers = np.linspace(0, 1, 20)
width = 0.08

B_sample = gaussian_basis(x_sample, centers, width)
B_full = gaussian_basis(x, centers, width)

# Ajustar los coeficientes por mínimos cuadrados
coeffs, *_ = np.linalg.lstsq(B_sample, y_sample, rcond=None)

# Reconstruir la señal
y_regression = B_full @ coeffs


#Calcular el error de la construción
def calcular_rmse(y_true, y_ajuste):
    return np.sqrt(np.mean((y_true - y_ajuste)**2))

# Calculo del RMSE
rmse_linear = calcular_rmse(y_true, y_linear)
rmse_cubica = calcular_rmse(y_true, y_cubica)
rmse_spline = calcular_rmse(y_true, y_spline)
rmse_regression = calcular_rmse(y_true, y_regression)

print("RMSE de cada metodo:")
print(f"Interpolacion lineal: {rmse_linear:.5f}")
print(f"Interpolacion cubica: {rmse_cubica:.5f}")
print(f"Spline suavizante:    {rmse_spline:.5f}")
print(f"Regresion de gaussiana:  {rmse_regression:.5f}")

# Grafico de la señal
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
axes = axes.ravel()

# Datos comunes para todas las graficas
graficas = [
    ("Señal original", None),
    ("Interpolación lineal", y_linear),
    ("Interpolación cúbica", y_cubica),
    ("Spline suavizante", y_spline),
    ("Regresión con base gaussiana", y_regression)
]

for i, (titulo, ajuste) in enumerate(graficas):
    ax = axes[i]

    ax.plot(x, y_true, "--", label="Señal original")
    ax.plot(x_sample, y_sample, ".", markersize=3,
            label="Muestras conservadas")

    if ajuste is not None:
        ax.plot(x, ajuste, "-", label=titulo)

    ax.set_title(titulo)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend(fontsize=8)

# Ocultar el sexto panel, que queda vacío
axes[5].axis("off")

plt.tight_layout()
plt.show()