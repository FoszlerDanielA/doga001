def min_keres(lista):
    for i in lista:
        if i < min:
            min = i
    return min
nums = []
while True:
    a = int(input("Aztán a számot is én találjam ki?!?!?!?!?!?!?!?!?!?!?!!?!?!?!?!"))
    if a != 0:
        nums.append(a)
    else:
        break

minimum = min_keres(nums)
print(minimum)

