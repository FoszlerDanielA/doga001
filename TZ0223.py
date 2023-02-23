def rendezo(parameter1):
    for i in range(len(parameter1)-1):
        for j in range(i+1, len(parameter1)):
            if parameter[i] < parameter1[j]:
                parameter[i] , parameter1[j] = parameter1[j] , parameter[i]












lista = []

while True:
    szam = int(input())
    if szam == -1:
        break
    else:
        lista.append(szam)
print(lista)
rendezett = rendezo(lista)
print(rendezett)
