def csokeno(lista):
    for i in range(0, len(lista)-1):
        for j in range(i, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
a = []
with open("egysoros.txt", "r", encoding="utf-8") as file:
    for sor in file:
        a = sor.strip().split(";")

for i in range(len(a)):
    a[i] = int(a[i])

csokeno(a)
print("EGYSOROS")
print(a)

b = []
with open("többsoros.txt", "r", encoding="UTF-8")as file:
    for sor in file:
        b.append(sor.strip().split(";"))

for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])

print("Többszörös")
for i in range(len(b)):


egy = ""
for i in a:
    egy = egy+str(i)+";"

with open("egysoros_eredmeny.txt", "w") as file:
    file.write(egy)

with open("többsoros_eredmeny.txt", "w") as file:
    for i in b:
        sor = ""
        for j in i:
            sor =
