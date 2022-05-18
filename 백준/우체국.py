n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst2 = []
result = []
end_count = 0
for i, (x, y) in enumerate(lst):

    lst2.append( i * y)
print(lst2)
start = 0
mid = 0
for i in range(len(lst)):
    if i == 0:
        end_count -= lst[i][1]
        mid = lst[i][1]
        result.append([start, end_count, i])
    else:
        start += mid
        end_count -= lst[i][1]
        mid = lst[i][1]
        result.append([start, end_count, i])
result.sort(key=lambda x: (abs(x[1]-x[0]), x[2]))
print(result[0][2]+1)


