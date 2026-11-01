
class Vector:

    def __init__(self, components):
        self.components = list(components)

    def __repr__(self):
        return f"Vector({self.components})"

    def __len__(self):
        return len(self.components)

    def __getitem__(self, i):
        return self.components[i]

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

        return Vector([a - b for a, b in zip(self, other)])

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.components == other.components

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.components])

    def __rmul__(self, scalar):
        return self * scalar

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

        return sum(a * b for a, b in zip(self, other))

    def __abs__(self):
        return sum(x**2 for x in self.components)**0.5