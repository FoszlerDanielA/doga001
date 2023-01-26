lista = [1, 3, 6, 87654321, 6727372, 5, 30, 42, 81, -7, -25, 92, -52, 914, 71, -6013, 9, 26, 935, 9254, 52, 653]

for i in range(len(lista), 0, -1):
    for j in range(0, i-1):
        if lista[j] > lista[j+1]:
            b = lista[j+1]
            lista[j+1] = lista[j]
            lista[j] = b

print(lista)
