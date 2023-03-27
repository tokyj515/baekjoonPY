
import sys

N = int(sys.stdin.readline())
num = list(map(int, (sys.stdin.readline()).split()))

arr = []

for i in range(N):
    arr.insert(i-num[i], i+1)


for e in arr:
    print(e, end=" ")