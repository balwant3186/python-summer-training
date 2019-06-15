items = ['egg', 'milk', 'butter', 'peanuts', 'oats', 'honey']
for i in enumerate(items):
    print(i, end = ',')
print('a')
items = ['cup', 'pen', 'book']

for i in enumerate(items, 100):
    print(i, end = ',')
