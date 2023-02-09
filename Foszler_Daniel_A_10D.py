def rendeznov(lista):
    for i in range(len(lista), 0, -1):
        for j in range(0, i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
#                a = lista[j+1]
#                lista[j + 1] = lista[j]
#                lista[j] = a
    return lista
def minkeres(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    return minimum
def maxkeres(lista):
    maximum = lista[0]
    for i in lista:
        if i > maximum:
            maximum = i
    return maximum

lista = [1, 9, -6, 11, 7, 12, 120, -96, 55, 42, 300, 15, -1]
lista = rendeznov(lista)
legnagy = maxkeres(lista)
legkis = minkeres(lista)
print("Legkisebb szám értéke:", legkis)
print("Legnagyobb szám értéke", legnagy)
