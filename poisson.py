import math
import numpy as np

def poisson(n, mu):
    return (mu**n * np.exp(-mu)) / math.factorial(n)
