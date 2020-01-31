print("Tax Bracket Calculator");

bracket_1_limit = int(input("Enter the limit of bracket 1 (lowest bracket): "));
bracket_1_percentage = float(input("Enter the percentage of bracket 1 (period followed by number): "))
bracket_2_limit = int(input("Enter the limit of bracket 2:"));
bracket_2_percentage = float(input("Enter the percentage of bracket 2 (period followed by number): "))
bracket_3_limit = int(input("Enter the limit of bracket 3:"));
bracket_3_percentage = float(input("Enter the percentage of bracket 3 (period followed by number): "))

income = int(input("Enter income: "));

if income <= bracket_1_limit:
    result = int(income * (1 - bracket_1_percentage));
elif income <= bracket_2_limit:
    remainder = income - bracket_1_limit;
    result = int((bracket_1_limit * (1 - bracket_1_percentage)) + (remainder * (1 - bracket_2_percentage)));
else:
    remainder = income - (bracket_1_limit + bracket_2_limit);
    result = int((bracket_1_limit * (1 - bracket_1_percentage)) + (bracket_2_limit * (1 - bracket_2_percentage ))+ (remainder * (1 - bracket_3_percentage)));

print("Post tax income: " + str(result));