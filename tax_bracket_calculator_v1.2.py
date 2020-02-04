#Tax Bracket Calculator 1.2
print("Tax Bracket Calculator 1.2")

limits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

bracket_count = int(input("Enter the number of brackets (limit 10): "))

for x in range (0, bracket_count):
    limits[x] = int(input("Enter the limit of bracket " + str(x+1) + ": "))
    rates[x] = float(input("Enter the tax rate of bracket " + str(x+1) + " (period followed by number): "))

income = int(input("Enter income: "))

ceiling = limits[0]

x = 0
result = 0.0

while income > ceiling:
    x = x + 1
    ceiling = limits[x]

#calculations for initial brackets
for y in range (0, x):
    result = result + (limits[y] - limits[y - 1]) * (1 - rates[y])

#calculation for last bracket
result = result + (income - limits[x - 1]) * (1 - rates[x])

print("Net income: " + str(result))
