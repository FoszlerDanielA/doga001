print("Kérek add meg az első számot:")
elso = float(input())
e = 0
for i in range(5):
    print("Kérek adj számot:")
    b = float(input())
    e = e+b

if elso < e:
    print("ön az átlagolást választotta, az eredmény:",e/5)
else:
    print("ön a négyzet funkciót választotta, az eredmény:",e**2)