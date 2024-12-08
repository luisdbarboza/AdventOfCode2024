file = open("input.txt", "r")

leftList = []
rightList = []

rightCounterHashTable = {}

for line in file.readlines():
    lineParts = line.split(" ")
    left = lineParts[0]
    right = lineParts[-1]
    leftList.append(left)
    rightList.append(right)

    if not int(int(right)) in rightCounterHashTable:
        rightCounterHashTable[int(right)] = 1
    else:
        rightCounterHashTable[int(right)] += 1


leftList.sort()
rightList.sort()

total = 0

for counter in range(len(leftList)):
    left = leftList[counter]

    if int(left) in rightCounterHashTable:
        total += int(left) * rightCounterHashTable[int(left)]

file.close()

print(total)