N = int(input())
num = list(map(int, input().split()))
num = list(set(num))

num.sort()

for n in num:
    print(n, end=" ")


# numList = [0 for i in range(N)]


# for i in inputList:
#     if(numList[i] == 0):
#         numList[i] = 1
#
# for i in range(0,N):
#     if(numList[i] == 1):
#         print(i, end=" ")



