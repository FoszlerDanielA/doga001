temperatures = []

for i in range(1, 31):
    temp = float(input("Enter the temperature for day " + str(i) + ": "))
    temperatures.append(temp)

average = sum(temperatures) / len(temperatures)
min_temp = min(temperatures)
min_day = temperatures.index(min_temp) + 1
max_temp = max(temperatures)
max_day = temperatures.index(max_temp) + 1

print("Average temperature:", average)
print("Minimum temperature of", min_temp, "was on day", min_day)
print("Maximum temperature of", max_temp, "was on day", max_day)
