import sys
num = []


N = int(sys.stdin.readline())
for i in range(N):
    num.append(int(sys.stdin.readline()))

num.reverse()


cnt = 1
max_num = num[0]
for n in num:
    if n > max_num:
        cnt += 1
        max_num = n


print(cnt)

