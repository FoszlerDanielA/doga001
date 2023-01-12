lista = []
minimum = 99999999999999999999999999999999999999999999999999999999999999999999999
maximum = -9999999999999999999999999999999999999999999999999999999999999999999999
for i in range(5):
    a = int(input())
    lista.append(a)
    if maximum < a:
        maximum = a
        maxhely = lista.index(a)
    if minimum > a:
        minimum = a
        minhely = lista.index(a)
print("A legnagyobb elem:",maximum,"helye:",maxhely )
print("A legkisebb elem:",minimum,"helye:",minhely)
