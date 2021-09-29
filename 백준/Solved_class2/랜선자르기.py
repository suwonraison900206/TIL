K , N = map(int,input().split())
lst = []
[lst.append(int(input())) for __ in range(K)]

start, end = 1, max(lst)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in lst:
        cnt += i // mid

    if cnt >= N:
        start = mid + 1

    else:
        end = mid -1

print(end)