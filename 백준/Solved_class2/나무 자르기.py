N, M = map(int,input().split())
trees = list(map(int,input().split()))

start , end =1,  max(trees)

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for tree in trees:

        if tree - mid >= 0:
            cnt += tree - mid

    if cnt >= M:
        start = mid +1
    elif cnt < M:
        end = mid - 1

print(end)

