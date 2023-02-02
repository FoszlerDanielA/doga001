def paros_e(szam):
    if szam % 2 == 0:
        return True
    else:
        return False

print(paros_e(2))
def kilep(szam):
    while szam == 0:
        return True
    else:
        return False

def osszeg_fg(lista):
    osszeg = 0
    for i in lista:
        osszeg = osszeg+i

    return osszeg

def atlag(lista):
    osszeg = osszeg_fg(lista)
    atl = osszeg/len(lista)
    return atl

lista=[]
while True:
    a = int(input())
    if kilep(a):
        break
    else:
        lista.append(a)
        if paros_e(a):
            print("páros")
        else:
            print("páratlan")

atl = atlag(lista)
print(atl)