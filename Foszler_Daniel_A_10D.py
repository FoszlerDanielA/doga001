def rendeznov(lista):
    for i in range(len(lista), 0, -1):
        for j in range(0, i - 1):
            if lista[j] > lista[j+1]:
                a = lista[j+1]
                lista[j + 1] = lista[j]
                lista[j] = a
    return lista

lista = [1, 9, -6, 11, 7, 12, 120, -96, 55, 42, 300, 15, -1]
lista = rendeznov(lista)
legnagy = lista[11]
legkis = lista[0]
print("Legkisebb szám értéke:", legnagy)
print("Legnagyobb szám értéke", legkis)
