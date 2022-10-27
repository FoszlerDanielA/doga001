#a = range(5)
#print(a)
#
#for i in range(6):
#    print(i)
#
#a = 5
#b = 7
#
#while a<b:
#
#    print(a)
#    a = a+1
#
#print("конец фильма!")
#a = 10
#b = 0
#while b >= 0:
#    b = float(input())
#
#print(a/b)

jomegoldas = "abcd"
megoldas = "abc"
a = False
b = False
c = False
d = False
for i in jomegoldas:
    for j in megoldas:

        if j == i:
            if i == "a":
                a = True
            if i == "b":
                b = True
            if i == "c":
                c = True
            if i == "d":
                d = True
if a and b and c and d:
    print("GOOD!!")
else:
    print("bad")