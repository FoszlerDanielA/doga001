a = 1
logikai = True

a = int(input("Írja ide a bekérendő számot:"))
for i in range(2,a,1):
    if a % i == 0:
        logikai = False
if logikai == False:
    if a%2==0:
        print("Ура(Hurrá)!")
    elif a%3==0:
        print("Három a magyar igazság.")
if a <= 10:
    if a == 1:
        print("I")
    elif a == 2:
        print("II")
    elif a == 3:
        print("III")
    elif a == 4:
        print("IV")
    elif a == 5:
        print("V")
    elif a == 6:
        print("VI")
    elif a == 7:
        print("VII")
    elif a == 8:
        print("VIII")
    elif a == 9:
        print("IX")
    elif a == 10:
        print("X")
else:
    print("Nem nyert!")
