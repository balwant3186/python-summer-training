import os

os.mkdir('Vips')
os.chdir('Vips')

for x in range(21):
    os.mkdir('participants_' + str(x))
    os.chdir('participants_' + str(x))
    for y in range(20):
        os.mkdir('day_' + str(y))
    os.chdir('../')
