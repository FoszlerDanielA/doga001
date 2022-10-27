homerseklet = float(input("Add meg az alap hőfokot!"))
print("Add meg a mértékegységet C=celsius F=farenheit K=kelvin")
mertekegyseg = input()
print("Kérlek add meg, hogy mire szeretnél átváltatni c=celsius f=farenheit k=kelvin")
kivantme = input()

if mertekegyseg == "C":
    if kivantme == "f":
        F = homerseklet*1.8+32
        print("A hőmérséklet Celsiusban", homerseklet)
        print("A hőmérséklet Farenheitben", F)
    elif kivantme == "k":
        K = homerseklet + 273.15
        print("A hőmérséklet Celsiusban", homerseklet)
        print("A hőmérséklet Kelvinben", K)
elif mertekegyseg == "F":
    if kivantme == "c":
        C = (homerseklet-32)/1.8
        print("A hőmérséklet Farenheitben", homerseklet)
        print("A hőmérséklet Celsiusban", C)
    elif kivantme == "k":
        C = (homerseklet - 32) / 1.8
        K = C+273.15
        print("A hőmérséklet Farenheitben", homerseklet)
        print("A hőmérséklet Kelvinben", K)

elif mertekegyseg == "K":
    if kivantme == "c":
        C = homerseklet-273.15
        print("A hőmérséklet Kelvinben", homerseklet)
        print("A hőmérséklet Celsiusban", C)
    elif kivantme == "f":
        C = homerseklet - 273.15
        F = C*1.8+32
    print("A hőmérséklet Kelvinben", homerseklet)
    print("A hőmérséklet Farenheitben",F)