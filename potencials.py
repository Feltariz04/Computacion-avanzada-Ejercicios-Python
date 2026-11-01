from abc import ABC, abstractmethod


class Potential1D(ABC):

    @abstractmethod
    def V(self, x):
        pass

    def force(self, x, h=1e-5):
        return -(self.V(x + h) - self.V(x - h)) / (2 * h)


class Harmonic(Potential1D):

    def __init__(self, k):
        if k <= 0:
            raise ValueError("k must be positive")
        self.k = k

    def V(self, x):
        return 0.5 * self.k * x**2


class Gravity(Potential1D):

    def __init__(self, m, g=9.81):
        if m <= 0 or g <= 0:
            raise ValueError("m and g must be positive")
        self.m = m
        self.g = g

    def V(self, x):
        return self.m * self.g * x


harmonic = Harmonic(k=2)
gravity = Gravity(m=3)

x = 1


numerical = harmonic.force(x)
analytical = -harmonic.k * x

print(
        f"x = {x:2d} | "
        f"Numerical = {numerical:.6f} | "
        f"Analytical = {analytical:.6f}"
    )

numerical = gravity.force(x)
analytical = -gravity.m * gravity.g

print(
        f"x = {x:2d} | "
        f"Numerical = {numerical:.6f} | "
        f"Analytical = {analytical:.6f}"
    )