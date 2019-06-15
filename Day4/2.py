fo = open(r'C:\Python\Python Summer Training VIPS\hello.txt', 'w')
print('Name of file: ', fo.name)
print('Closed or not? ', fo.closed)
print('Opening mode: ', fo.mode)

fo.close()
print('Closed or not? ', fo.closed)
