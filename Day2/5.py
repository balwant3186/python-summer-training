year = int(input('Enter period: '))
sum = 100

for i in range(year):
    sum += sum * 0.05

compound = sum * (1 + 0.05 ** (1 * year))

print('Sum after (Simple)', year, ' = ', round(sum, 2))
print('Sum after (Compound)', year, ' = ', round(compound, 2))
