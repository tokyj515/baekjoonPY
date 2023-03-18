N = int(input())
numList = [0 for i in range(N)]

for i in range(N):
    j = int(input())
    numList[j] += 1

for i in range(0,len(numList)):
    for _ in range(0,numList[i]):
        print(i)
