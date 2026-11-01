import random

class Histogram:

    def __init__(self, nbins, xmin, xmax):
        self.nbins = nbins
        self.xmin = xmin
        self.xmax = xmax

        # Ancho de cada bin
        self.bin_width = (xmax - xmin) / nbins

        # Inicializar todas las cuentas a cero
        self.counts = [0] * nbins

    def fill(self, x):
        # Ignorar valores fuera del rango
        if x < self.xmin or x > self.xmax:
            return

        # Calcular el índice del bin
        index = int((x - self.xmin) / self.bin_width)

        # El extremo xmax pertenece al último bin
        if index == self.nbins:
            index = self.nbins - 1

        # Añadir una entrada al bin correspondiente
        self.counts[index] += 1

    @property
    def entries(self):
        return sum(self.counts)

    def mean(self):
        total = 0

        for i in range(self.nbins):
            center = self.xmin + (i + 0.5) * self.bin_width
            total += center * self.counts[i]

        if self.entries == 0:
            return 0

        return total / self.entries

    def __str__(self):
        result = ""

        for i in range(self.nbins):
            center = self.xmin + (i + 0.5) * self.bin_width
            result += f"{center:6.2f} | {'*' * self.counts[i]}\n"

        return result


# Crear el histograma
hist = Histogram(12, -3, 3)

# Generar y almacenar 1000 valores gaussianos
for _ in range(1000):
    x = random.gauss(0, 1)
    hist.fill(x)

# Imprimir resultados
print(hist)
print("Entries:", hist.entries)
print("Mean:", hist.mean())