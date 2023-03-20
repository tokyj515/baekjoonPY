import sys

dic = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four",
       "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
arr = []
N, M = map(int, sys.stdin.readline().split())

for i in range(N, M+1):
    temp = []
    S = str(i)
    for j in S:
        temp.append([dic[j], j]) #영어로된 숫자, 원래 숫자
    arr.append(temp)

arr.sort()


for i in range(len(arr)):

    temp = ""
    for a, b in arr[i]:
        temp += b
    print(temp, end=" ")

    if i%10 == 9:
        print()



