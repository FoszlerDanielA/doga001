import math
a = int(input())
b = int(input())

muvelet = input()

eredmeny = -1

if muvelet == "+":
    eredmeny = a+b
elif muvelet == "-":
    eredmeny = a-b
elif muvelet == "*":
    eredmeny = a*b
elif muvelet == "/":
    eredmeny = a/b
elif muvelet == "négyzet":
    eredmeny = a**b
elif muvelet == "gyök":
    eredmeny = math.sqrt(a)
print(eredmeny)