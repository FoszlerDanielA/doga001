konyvek = {}
while True:
    cimek = {}
    leírás = {}
    műfaj = {}
    szerzo = input("A Szerző nevét Én TalÁLJam ki?!?!")

    if szerzo == "":
        break
    else:
        while True:
            cim = input("A CíMEt is ÉN ÍRJAM?!?!?!")
            if cim == "":
                break
            else:
                leírás = input("ASSZED Én Írom Le?!?!?!?!?")
                műfaj = input("Add Meg a Műfajt!!!!")
                kiadás = int(input("Add MÁr MEg A KiADást!!!"))
                cimek[cim] = leírás, műfaj, kiadás
        konyvek[szerzo] = cimek
for i, j in konyvek.items():
    print(i, ":", j)
