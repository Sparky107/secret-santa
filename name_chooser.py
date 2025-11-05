import names
import random

blocked = {}
assigned = {}
scrambled = [1,2,3,4]
unscrambled = [1,2,3,4]

for i in range(1,5):
    isnumber = False
    while not isnumber:
        entry = input(names.names_[i] + ', choose one person to block.\n1-Bjarmi ::: 2-Benjamin\n3-Elias  ::: 4-Helgi\n')
        if entry == '':
            blocked[i] = 0
            isnumber = True
        elif not entry.isdigit():
            print('Try again...')
        else:
            blocked[i] = int(entry)
            isnumber = True

fine = False
while not fine:
    random.shuffle(scrambled)
    for i in unscrambled:
        if i == scrambled[i-1] or blocked[i] == scrambled[i-1]:
            fine = False
            break
        elif i == 4:
            fine = True

for i in unscrambled:
    assigned[i] = scrambled[i-1]

text_file = open('Python\\Misc\\SecretSanta\\names_list.txt', 'w')
for i in assigned.keys():
    text_file.write(names.names_[assigned[i]] + '\n')

text_file.close()