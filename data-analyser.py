

armsPulls = [0] * 10
armsSuccess = [0] * 10

file = open("dataset.txt", "r")
for line in file:
    content = line.split(" ")
    arm = int(content[0]) - 1
    result = int(content[1])
    armsPulls[arm] += 1
    armsSuccess[arm] += result

print(armsPulls)
print(armsSuccess)
print([float(armsSuccess[i]) / armsPulls[i] for i, v in enumerate(armsSuccess)])

