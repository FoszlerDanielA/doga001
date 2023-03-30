print("1. feladat")
a = int(input("Add meg az első számot"))
b = int(input("Add meg a második számot"))
if a > b:
    print("A nagyobbik szám a(z):", a)
if b > a:
    print("A nagyobbik szám a(z):", b)
if a == b:
    print("A két érték egyenlő!")


print("2. feladat")
def kodolas(mondat,betu,darab):
    cserel = ""
    db = 0
    for i in mondat:
        if i == betu and db < darab:
            cserel=cserel+str(ord(i))
            db = db+1
        else:
            cserel = cserel + i
    return cserel

szoveg = kodolas("Cognito ergo sum.", "o",3)
print(szoveg)
