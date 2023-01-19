lista = [1,9,3,6,2,72,5,30,42,81,-7,-25,,92,-52,914,71,-6013,9,26,935,9254,-2438]


for i in range(len(list)-1):
    for j in range(i+1,len(lista)):
        print(lista)
        if lista[i] > lista[j]:
            lista[i] , lista[j] =lista[j] , lista[i]
            print("csere")
        else:
            print(" ")