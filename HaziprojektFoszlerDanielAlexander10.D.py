hofok = []

for i in range(1, 31):
    ho = float(input("adja meg a hőfokát a(z) " + str(i) + ". napnak: "))
    hofok.append(ho)

avg = sum(hofok) / len(hofok)
min_ho = min(hofok)
min_nap = hofok.index(min_ho) + 1
max_ho = max(hofok)
max_nap = hofok.index(max_ho) + 1
ice = []
fd = 0
for i in hofok:
    if i < 0:
        ice.append(i)
    fd = len(ice)

print("Átlagos hőfok:", avg,"C°")
print("Minimum hőfok", min_ho, "C° volt a", min_nap,". napon")
print("Maximum hőfok", max_ho, "C° volt a", max_nap,". napon")
print(fd,"napnyi fagy volt")