n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst2 = []
result = []
end_count = 0
for x, y in lst:
    lst2.append(x*y)
    end_count += y
start_count = 0
start, end = 0, sum(lst2)
print(lst2)
idx = 0

while idx < len(lst2):

    if idx == 0:
        end_count -= lst[idx][1]
        start_count += lst[idx][1]
        end = end - lst[idx][1] - end_count
        result.append([start, end, idx])
        idx += 1
    else:
        start = start_count
        end_count -= lst[idx][1]
        end = end - lst[idx][1] - end_count
        result.append([start, end, idx])
        start_count = (start * (idx+1)) + lst[idx][1]
        idx += 1
print(result)
result.sort(key=lambda x: (abs(x[1] - x[0]), x[2]))
print(result)
print(result[0][2] + 1)

1 3

0 2
2 0









