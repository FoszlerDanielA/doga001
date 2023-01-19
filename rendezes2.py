lista = [1,3,6,87654321,-8765498765048765654212345,2,-98765432100123456789876543210987654321012346799876543210,6727372,5,30,42,81,12345678654321234567876543212349876543210123456789012345678012345678901234567890123456789876543210,-7,-25,92,-52,914,71,-6013,9,26,935,9254,52,653,76543,4321,65432,235,8731]


for i in range(len(lista)-1):
    minind = i
    for j in range(i+1 ,len(lista)):
        if lista[j] < lista[minind]:
            minind = j
            print("Új minimum találat")
        else:
            print("")
    if i != minind:
        print("csere")
        lista[i],lista[minind] = lista[minind],lista[i]

print(lista)