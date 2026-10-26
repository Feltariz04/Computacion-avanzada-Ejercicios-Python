# Ejercicio zip()

Nombres = ["Marta", "Gabriel", "Juan", "Felipe"]
Telefonos = ["456789767", "567899133", "513679123", "152367898"]

#print(Nombres)
#print(Telefonos)
def tuplas(Name, Tel):
    DP = tuple(zip(Name, Tel))
    return DP

DP = tuplas(Nombres, Telefonos)

dictionary = {ni: tel for ni , tel in DP}

print( dictionary)