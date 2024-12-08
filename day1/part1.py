file = open("input.txt", "r")

leftList = []
rightList = []

for line in file.readlines():
    lineParts = line.split(" ")
    left = lineParts[0]
    right = lineParts[-1]
    leftList.append(left)
    rightList.append(right)
    
leftList.sort()
rightList.sort()

total = 0

for counter in range(len(leftList)):
    left = leftList[counter]
    right = rightList[counter]

    total += abs(int(left) - int(right))

file.close()

print(total)