import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, least_squares

# Modelo: suma de dos gaussianas
def gauss_model(x, A1, mu1, sigma1, A2, mu2, sigma2):
    g1 = A1 * np.exp(-((x - mu1)**2) / (2 * sigma1**2))
    g2 = A2 * np.exp(-((x - mu2)**2) / (2 * sigma2**2))
    return g1 + g2


# Generacion del espectro
np.random.seed(42)

x = np.linspace(0, 1, 500)

# Parametros verdaderos
p_true = [1.0, 0.30, 0.035, 0.7, 0.70, 0.06]

y_true = gauss_model(x, *p_true)

# Añadir ruido gaussiano
sigma_noise = 0.1
y_noise = y_true + np.random.normal(
    0, sigma_noise, size=len(x)
)

# ajuste con Curve fit
p0 = [0.9, 0.28, 0.05, 0.6, 0.72, 0.08]

popt, pcov = curve_fit(
    gauss_model,
    x,
    y_noise,
    p0=p0,
    sigma=np.full_like(x, sigma_noise),
    absolute_sigma=True,
    maxfev =10000
)

perr = np.sqrt(np.diag(pcov))
y_fit = gauss_model(x, *popt)

nombres = ["A1", "mu1", "sigma1", "A2", "mu2", "sigma2"]



# Ajuste con least_squares

def residuos(p, x, y):
    return (gauss_model(x, *p) - y) / sigma_noise



resultado = least_squares(
    residuos,
    p0,
    args=(x, y_noise),
    max_nfev=10000
)

popt_ls = resultado.x



# Matriz de covarianza aproximada
J = resultado.jac

pcov_ls = np.linalg.pinv(J.T @ J)

# Errores estandar de 1 sigma
perr_ls = np.sqrt(np.diag(pcov_ls))



print("\nComparacion de resultados")
print(f"{'Parametro':10s} {'curve_fit':>14s} {'Error CF':>12s} "
      f"{'least_squares':>16s} {'Error LS':>12s}")

for i, nombre in enumerate(nombres):
    print(
        f"{nombre:10s} "
        f"{popt[i]:14.6f} {perr[i]:12.6f} "
        f"{popt_ls[i]:16.6f} {perr_ls[i]:12.6f}"
    )



# Grafica del espectro
plt.figure(figsize=(9, 5))
plt.plot(x, y_true, label="Espectro verdadero")
plt.scatter(x, y_noise, s=8, alpha=0.5, label="Datos con ruido")
plt.plot(x, y_fit, label="Ajuste con curve_fit")
plt.xlabel("x")
plt.ylabel("Intensidad")
plt.title("Ajuste de dos gaussianas con curve_fit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
