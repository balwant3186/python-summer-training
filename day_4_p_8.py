filename = r'C:\Python\Python Summer Training VIPS\student1.txt'

for line in open(filename):
    str1 = line
    print('String is: ', str1)
    words = str1[:-1].split(',')
    print(words)

    if words[-1][-1] == '\n':
        words[-1] = words[-1][:-1]
    print(words)
    print('-' * 30)
