c = input()
h = ""
szó = " "
for i in range(len(c)-1,-1,-1):
    h = h+c[i]
for i in c.split(" "):
    print(i)

print(h)

if c == h:
    print(" ",True,",palindrom")
else:
    print(" ",False,",nem palindrom")