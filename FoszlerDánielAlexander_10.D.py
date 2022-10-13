for i in range(5):
    print("Kérem adj meg egy számmot:")
    r = float(input())
    if r ==0:
        a = float(input())
        negy = a**2
        k = 2*3.14*a
        t = 3.14*negy
        d = 2*a
        print("Ön a kör opciót választotta")
        print("A kör kerülete:", round(k), "cm")
        print("A kör területe:", round(t), "cm2")
        print("A kör átmérője:", round(d), "cm")
    elif r%2 == 0:
        negyzet = r**2
        print("Ön a négyzet opciót választotta")
        print(negyzet)
    elif r%2 == 1:
        print("nincs ilyen opció")
