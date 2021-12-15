n = int(input())
lst = list(map(int,input().split()))
lst.sort()
cnt = 0
time_count = 0
for i in range(len(lst)):
    if i == 0:
        cnt += lst[i]
        time_count += lst[i]

    else:
        cnt = cnt + time_count + lst[i]
        time_count = time_count + lst[i]


print(cnt)