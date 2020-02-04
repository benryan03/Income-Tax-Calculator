#Tax Bracket Calculator 1.4
print("Tax Bracket Calculator 1.4")

limits = []
rates = []

#gathering user inputs

bracket_count = int(input("Enter the number of brackets: "))

for x in range (0, bracket_count):
    limits.append(int(input("Enter the limit of bracket " + str(x+1) + ": ")))
    rates.append(float(input("Enter the tax rate of bracket " + str(x+1) + " (period followed by number): ")))

income = int(input("Enter income: "))

#all user inputs complete

max_bracket = limits[x]
max_bracket_index = x
result = 0.0

if income < max_bracket:

    #this loop calculates how many brackets to apply
    x = 0
    ceiling = limits[0]
    while income > ceiling:
        x = x + 1
        ceiling = limits[x]

        #calculations for initial brackets
        for y in range (0, x):
            result = result + (limits[y] - limits[y - 1]) * (1 - rates[y])

        #calculation for final bracket
        result = result + (income - limits[x - 1]) * (1 - rates[x])

else:
    #calculations for initial brackets
    for y in range (0, max_bracket_index):
        result = result + (limits[y] - limits[y - 1]) * (1 - rates[y])

    #calculation for final bracket
    result = result + (income - limits[x - 1]) * (1 - rates[x])

print("Net income: " + str(result))
