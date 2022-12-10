f = open("day6_input.txt").read().strip()

sop = []
som = []
for i in range(len(f)):
    if len(set(f[i:i + 4])) == 4: #set -> multiple chars added only once,
                                  # i:i+4 -> e.g.: 2:6 -> char 3 - 6 appears because 2:
                                  # remove first 3 chars and :6 let only first 6 appears
                                  #s/o to RainbowDashLabs from GitHub
        sop.append(i+4)
    if len(set(f[i:i + 14])) == 14:
        som.append(i+14)

print(sop[0])
print(som[0])