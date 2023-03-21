import sys

N = int(sys.stdin.readline())
arr = []

# Junkyu 50 60 100
# 이름 국 영 수


for i in range(N):
    temp = (sys.stdin.readline()).split()
    arr.append(temp)

newArr = sorted(arr, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for e in newArr:
    print(e[0])

