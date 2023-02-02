lista = [10, -2, 1, 25, 22, 30, 60, -99, -1252, 3000, 2123, 16, 12]
lista1 = [10, -2, 1, 25, 22, 30, 60, -99, -1252, 3000, 2123, 16, 12]
for i in range(len(lista)-1):
    mind = i

    for j in range(i + 1, len(lista)):
        if lista[j] < lista[mind]:
            mind = j
        if i != mind:
            lista[i], lista[mind] = lista[mind], lista[i]

for i in range(len(lista1)-1):
    mind = i

    for j in range(i + 1, len(lista1)):
        if lista1[j] > lista1[mind]:
            mind = j
        if i != mind:
            lista1[i], lista1[mind] = lista1[mind], lista1[i]
print(lista)
print(lista1)
print("legkisebb érték", lista[0])
print("legnagyobb érték", lista[12])