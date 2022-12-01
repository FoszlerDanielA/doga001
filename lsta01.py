lista1=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

elem = 0
for num in lista1:
    if num:
        elem = elem+1

print("Ennyi eleme van a listának:",elem)

count = 0
for num in lista1:
    if num < 0:
        count = count + 1
print("A listában van negatív szám")

paros = 0
for num in lista1:
    if num%2 == 0:
        paros = paros + 1

print("Páros számok mennyisége:", paros)

maxElem = lista1[0]
for i in range(1,len(lista1)):
    if lista1[i] > maxElem:
        maxElem = lista1[i]
        maxhely = i
print("A legnagyobb elem",maxElem)

tizes = 0
for num in lista1:
    if num%10 == 0:
        tizes = tizes + 1

print("tízzel osztható számok mennyisége:", tizes)