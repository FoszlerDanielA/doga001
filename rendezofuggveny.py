lista = [1, 3, 6, 87654321, 6727372, 5, 92, -52, 914, 71, -6013, 9, 26, 935, 9254, 52, 653]
def rendezcsokk(lista, irany):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[j] > lista[j+1]:
                lista[i], lista[j] = lista[j], lista[i]


rendezcsokk(lista,"nov")
print(lista)