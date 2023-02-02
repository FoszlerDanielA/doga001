def ter(a,b):
    t= a*b
    return t
def ker(a,b):
    k = 2*(a+b)
    return k
a = [5, 4, 3]
b = [9, 10, 12]
teruletek = []
keruletek = []

for i,j in zip(a,b):
    teruletek.append(ter(i,j))