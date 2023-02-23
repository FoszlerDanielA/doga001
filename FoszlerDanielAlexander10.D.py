def rendeznov(lista):
    for i in range(len(lista), 0, -1):
        for j in range(0, i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
def rendezcsokk(lista):
    for i in range(len(lista), 0, -1):
        for j in range(0, i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def legnagy(lista):
    maxim = lista[0]
    for i in lista:
        if maxim < i:
            maxim = i
    return maxim


lista = []

while True:

    num = int(input("Adj meg egy egész számot:"))
    if num == -1:
        print(rendeznov(lista))
        break
    elif num == 0:
        print(rendeznov(lista))
    elif num == 1:
        print(rendezcsokk(lista))
    else:
        lista.append(num)


#a = lista[j + 1]
#lista[j + 1] = lista[j]
#lista[j] = a