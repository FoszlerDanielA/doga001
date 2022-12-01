#t = [5,3,6,2,1]

#maxElem = t[0]
#for elem in t:
#    if elem > maxElem:
#        maxElem = elem
#print(maxElem)
##########################
#t = [5,3,6,2,1]

#maxElem = t[0]
#for i in range(1,len(t)):
#    if t[i] > maxElem:
#        maxElem = t[i]
#        maxhely = i
#print(maxElem,maxhely)
####################################################
#ebben a feladatban a plussz kicserélhető bármire
#t = [3,8,2,4,5,1,6]

#osszeg = 0
#for num in t:
#    osszeg = osszeg + num
#
#print("Összeg:",osszeg)
##########################
#t = [5,3,6,2,1]
#
#minElem = t[0]
#for i in range(1,len(t)):
#    if t[i] < minElem:
#        minElem = t[i]
#        minhely = i
#print(minElem,minhely)
##########################
#t = [3,-8,2,4,5,11,6]
#
#count = 0
#for num in t:
#    if num < 0:
#        count = count + 1
#
#print("negatív számok:", count)
######################################
t = [3,8,2,4,5,1,6]
n = len(t)
ker = 5
i = 0
while i < n and t[i] != ker:
    i = i + 1
if i<n:
    print("Van ilyen:",ker)
else:
    print("Nincs ilyen elem",ker)