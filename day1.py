import os
os.mkdir('vips')
os.chdir('vips')

for x in range(21):
    os.mkdir('participant_' + str(x))
    os.chdir('participant_' + str(x))
    for y in range(20):
        os.mkdir('day_' + str(y))
    os.chdir('../')
