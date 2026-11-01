import math

class vector:

    def __init__(self, componentes):
        self.componentes = list(componentes) 

    def __len__(self):
        return len(self.componentes)

    def __getitem__(self, i):
        return self.componentes[i]

    def __repr__(self):
        return f"Vector({self.componentes})"

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Los vectores deben tener el mismo tamaño")

        componentes = [
            self[i] + other [i]
            for i in range(len(self))
        ]
        return componentes

    def __sub__(self, other):
            if len(self) != len(other):
                raise ValueError("Los vectores deben tener el mismo tamaño")
    
            componentes = [
                self[i] - other [i]
                for i in range(len(self))
            ]
            return componentes
    
    def __eq__(self, other):
        if not isinstance(other, vector):
            return NotImplemented

        return self.componentes == other.componentes

    def __mul__(self, scalar):
        components = [x * scalar for x in self.componentes]
        return vector(components)

    def __rmul__(self, scalar):
        return self * scalar

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Los vectores deben tener el mismo tamaño")

        return sum(
            self[i] * other[i]
            for i in range(len(self))
        )

    def __abs__(self):
        return math.sqrt(sum(x**2 for x in self.componentes))



v = vector([1, 2, 3, 4])
v2 = vector([1,2,3,8])
print(v)
print(v2)
print(v.__len__())
print(v.__getitem__(3))
print(v + v2)
print(v - v2)
print(v2 - v)
print(v * 2)
print(2 * v)
print(v.dot(v2))
print(abs(v))