#Tax Bracket Calculator v1.5
print("Tax Bracket Calculator v1.5")

limits = []
rates = []

bracket_count = int(input("Enter the number of brackets: "))

for x in range (0, bracket_count):
    limits.append(int(input("Enter the limit of bracket " + str(x+1) + ": ")))
    rates.append(float(input("Enter the tax rate of bracket " + str(x+1) + " (period followed by number): ")))

#I don't know why the lists need to have a an extra zero at the end to work
#I should try to fix this at some point
limits.append(0)
rates.append(0)

income = int(input("Enter income: "))

ceiling = limits[0]
max_bracket = limits[x]
max_bracket_index = x
result = 0.0
z = 0

if income < max_bracket:

    #this loop calculates how many brackets to apply
    while income > ceiling:
        z = z + 1
        ceiling = limits[z]

    #calculations for initial brackets
    for y in range (0, z):
        result = result + (limits[y] - limits[y - 1]) * (1 - rates[y])

    #calculation for final bracket
    result = result + (income - limits[z - 1]) * (1 - rates[z])

else:
    #calculations for initial brackets
    for y in range (0, max_bracket_index):
        result = result + (limits[y] - limits[y - 1]) * (1 - rates[y])

    #calculation for final bracket
    result = result + (income - limits[z - 1]) * (1 - rates[z])

print("Net income: " + str(result))
