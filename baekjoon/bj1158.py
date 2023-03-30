# import sys
#
# N, K = map(int, (sys.stdin.readline()).split()) #n개 숫자, K번째 삭제
# arr = []
# ans = []
#
# for i in range(1, N+1):
#     arr.append(i)
#
#
# cnt = 1
# while len(arr) < 0:
#     if(cnt != K):
#         temp = arr.pop(0)
#         arr.append(temp)
#         cnt += 1
#     else:
#         temp = arr.pop(0)
#         ans.append(temp)
#         cnt = 1
#
#
# cnt = 0
# print("<", end="")
# for e in ans:
#     print(e, end=", ")
#
#     if cnt == N:
#         print(e, ">")
#     else:
#         cnt += 1


from collections import deque

n, k = map(int, input().split())

# 1~n번 사람
people = deque()
for i in range(1, n+1): people.append(i)
result = []

while people:
  for _ in range(k-1):
    people.append(people.popleft())

  result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))


#풀이2
n, k = map(int,input().split())
queue = [i for i in range(1,n+1)]

result = []
count = 0

for i in range(n):
    count += k-1
    if count >= len(queue):
        count = count%len(queue)
    result.append(str(queue.pop(count)))
print("<", ", ".join(result), ">", sep = '')