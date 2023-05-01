import sys
num = []
ans = []


for i in range(9):
    num.append(int(sys.stdin.readline()))



num.sort()
sum = sum(num)



for i in range(len(num)):
    for j in range(len(num)):
        if sum - num[i] - num[j] == 100 and not ans:
            for k in range(len(num)):
                if k == i or k == j: continue
                ans.append(num[k])




for e in ans:
    print(e)
