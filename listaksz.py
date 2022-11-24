nev = ["Cony","Arnold Svárcenegger","Czigány Dezdemóna","Lakatos Dzsiglipuff"]

szul_ev = [2006,1988,2005,1999]

kor = []

for i,j in zip (nev,szul_ev):
    print(i,"  ",j)
    print(i, "  ",2022-j)
    kor.append(2022 - j)