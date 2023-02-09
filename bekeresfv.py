def harommal_oszthatok(lista):
    db = 0
    for i in elista:
        if i % 3 == 0:
            db = db + 1
    return db
def negativ(lista):
    if beszam < 0:
        return True
    else:
        return False
elista = []
while True:
    beszam = int(input())
    if negativ(beszam):
        break
    else:
        elista.append(beszam)
        db = harommal_oszthatok(beszam)
        print(db)






