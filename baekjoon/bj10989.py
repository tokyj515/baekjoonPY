
import sys

N = int(sys.stdin.readline())
numList = [0] * 10001

for i in range(N):
    j = int(sys.stdin.readline())
    numList[j] += 1

for i in range(10001):
    if numList[i] != 0:
        for _ in range(0,numList[i]):
            print(i)
