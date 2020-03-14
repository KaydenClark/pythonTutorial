from random import randint

numList = []


for i in range(1000):
    ranNum = randint(0, 100)
    numList.append(ranNum)

# print(numList)

biggestNum = 0

for i in range(len(numList)):
    # print(numList[i])
    if numList[i] >= biggestNum:
        biggestNum = numList[i]

print(biggestNum)

numList.sort()

for i in numList:
    while numList.count(i) > 1:
        # print(numList.count(i))
        numList.remove(i)

print(len(numList))