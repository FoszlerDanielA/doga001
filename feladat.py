hofok = []

for i in range(1, 31):
    ho = float(input("Enter the temperature for day " + str(i) + ": "))
    hofok.append(ho)

atlag = sum(hofok) / len(hofok)
min_ho = min(hofok)
min_nap = hofok.index(min_ho) + 1
max_ho = max(hofok)
max_nap = hofok.index(max_ho) + 1

print("Átlagos hőfok:", atlag,"C°")
print("Minimum hőfok", min_ho, "C° volt a", min_napnap,". napon)
print("Maximum hőfok", max_ho, "C° volt a", max_nap". napon)
