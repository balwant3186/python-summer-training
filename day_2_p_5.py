#Amount calculation

year = int(input("Enter no. of years: "))
sum = 100
for x in range(year):
    sum += sum * 0.05
compound = sum * (1 + 0.05 ** (1 * year))
print("Amount using simple interest: ", round(sum, 2))
print("Amount using compound interest: ", round(compound, 2))
