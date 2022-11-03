#lista = [1,2,3,4,5,6,7]
#lista[0] = 100
#print(lista[0])
#
#for i,j in enumerate(lista):
#    print(i,j)
#    lista[i] = lista[i]+100
#    print(i,lista[i])
#    print(lista.sort)

lista=[]
osszeg = 0
maximum  = -1
for i in range(5):
    a = int(input())
    lista.append(a)
    osszeg = osszeg+a
    if maximum < a:
        maximum = a
print(lista)
print(osszeg/len(lista))
print(maximum,lista.index(maximum))


