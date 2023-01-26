lista = [1, 9, 34, 84, 12, 85, 45, 86, 34, 13, 72, 40, 234]
lista1 = [-2, 64, 83]
lista2 = [42, 531, 201]
lista3 = [lista, lista1, lista2]
minimumok = []
def minKeres(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    print(minimum)
    return minimum


for i in lista3:
    minimumok.append(minKeres(i))