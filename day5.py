f = open("day5_input.txt").read().splitlines()


stacks = [[],[],[],[],[],[],[],[],[]]
word = []


for i in range(len(f)):
    if i < 10:
        letter = 2
        for i2 in range(9):
            add = f[i][:letter][-1:]

            if add == ' ' or add == '' or add == ']':
                letter += 4
            else:
                stacks[i2].append(f[i][:letter][-1:])
                letter += 4
for i4 in range(len(stacks)):
    stacks[i4].remove(f'{i4 +1}')
    stacks[i4].reverse()

steps = []
for i5 in range(len(f)):
    if i5 < 10:
        pass
    else: #ToDo BIS HIER GEHT ALLES




for i6 in range(len(stacks)):
    word.append(stacks[i6][len(stacks[i6])-1])

print(''.join(word))

