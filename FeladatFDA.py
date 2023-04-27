import copy as coo
adat = {}
zene = []
teljeshosz = []
with open("playlist.csv", "r", encoding="utf-8") as file:
    for sor in file:
        adat["eloado"] = sor.strip().split(";")[0]
        adat["cim"] = sor.strip().split(";")[1]
        adat["mufaj"] = sor.strip().split(";")[2]
        adat["hossz"] = sor.strip().split(";")[3]
        zene.append(coo.deepcopy(adat))
print(zene)
print(teljeshosz)

for i in range(len(teljeshosz)):
    teljeshosz[i][3] = int(teljeshosz[i][3])


#def perc(lista):
#    for i in lista:
#        x = 0
#        x = x+i/60
#        print(x)
#        return x
def teljes_hossz(lista):
    le = 0
    for i in lista:
        le = sum(lista)
        return le
a = (teljes_hossz(teljeshosz))
print(a)