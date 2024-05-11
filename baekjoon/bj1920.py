import sys



# 반복문



n = sys.stdin.readline()
data = list(map(int, sys.stdin.readline().split(" ")))
m = sys.stdin.readline()
find_data = list(map(int, sys.stdin.readline().split(" ")))

data.sort()


# def binary_search(target, data):
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return 1
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return 0



def binary_search(target, data, start, end):
    if start > end:
        return 0 # 존재하지 않음

    mid = (start + end) // 2

    if data[mid] == target:
        return 1 # 존재
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return binary_search(target, data, start,  end)

start = 0
end = len(data) -1

for t in find_data:
    print(binary_search(t, data, start, end))



