def harommal_oszthatok(lista):
    db = 0
    for i in lista:
        if i % 3 ==0:
            db = db+1
    return db
lista= [1,3,8,4,9,2,6,2,65,8,4,2,5,7,3,3,56,4,23,5,7,4,2,4,7,5,34,2,2,45,7,78,54,3,5,7,653,34,7,5,4,]

db = harommal_oszthatok(lista)
print(db)