n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
check = {}
count = 0
for x, y in lst:
    if x not in check:
        check[x] = y
    else:
        if check[x] != y:
            count += 1
            check[x] = y
print(count)