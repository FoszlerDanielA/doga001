hossz = float(input("Add meg az alap hosszt!"))
if hossz == (-1):
    print("A program vége")
else:
    while hossz < 0:
        hossz = float(input("Add meg az alap hosszt!"))

    print("Add meg a mértékegységet C=centiméter M=méter K=Kilométer")
    mertekegyseg = input()
    print("Kérlek add meg, hogy mire szeretnél átváltatni c=centiméter m=méter k=kilométer")
    kivantme = input()
    if mertekegyseg == "C":
        if kivantme == "m":
            M = hossz/100
            print("Hossz centiméterben", hossz)
            print("A hossz méterben", M)
        elif kivantme == "k":
            Km = hossz/100000
            print("Hossz centiméterben", hossz)
            print("A hossz Kilométerben", Km)
        else:
            print(hossz)
    elif mertekegyseg == "M":
        if kivantme == "c":
            Cm = hossz*100
            print("A hossz méterben", hossz)
            print("A hossz centiméterben", Cm)
        elif kivantme == "k":
            Km = hossz/1000
            print("A hossz méterben", hossz)
            print("A hossz kilométerben", Km)
        else:
            print(hossz)

    elif mertekegyseg == "K":
        if kivantme == "c":
            Cm = hossz*100000
            print("A hossz kilométerben", hossz)
            print("A hossz centiméterben", Cm)
        elif kivantme == "m":
            M = hossz*1000
            print("A hossz kilométerben", hossz)
            print("A hossz méterben", M)
        else:
            print(hossz)