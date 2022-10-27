# F to C = (F-32)/1.8
# C to F = C*1.8+32


homerseklet = float(input("Add meg az alap hőfokot!"))
print("Add meg a mértékegységet C=celsius F=farenheit K=kelvin")
mertekegyseg = input()

if mertekegyseg == "C":
    #Alaphőmérséklet celsius egységben van
    F = homerseklet*1.8+32
    K = homerseklet+273.15
    print("A hőmérséklet Celsiusban",homerseklet)
    print("A hőmérséklet Farenheitben",F)
    print("A hőmérséklet Kelvinben", K)
elif mertekegyseg == "F":
    # Alaphőmérséklet farenheit egységben van
    C = (homerseklet-32)/1.8
    K = C+273.15
    print("A hőmérséklet Farenheitben",homerseklet)
    print("A hőmérséklet Celsiusban",C)
    print("A hőmérséklet Kelvinben",K)

elif mertekegyseg == "K":
    # Alaphőmérséklet kelvin egységben van
    C = homerseklet-273.15
    F = C*1.8+32
    print("A hőmérséklet Kelvinben",homerseklet)
    print("A hőmérséklet Celsiusban",C)
    print("A hőmérséklet Farenheitben",F)

