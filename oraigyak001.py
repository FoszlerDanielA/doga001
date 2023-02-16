a = "abcde"

for i in a:
    print(i, end=" ")

print()
for j in range(0,len(a),2):
    print(a[j], end=" ")

print()
for i in a:
    print(ord(i), end=" ")