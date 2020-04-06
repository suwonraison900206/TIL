arr = [3,6,7,1]

n = len(arr)
final = []

for i in range(1, 1<<n):
    result = []
    for j in range(n+1):
        if i & (1<<j):
            result.append(arr[j])
            if len(result) != 0:
                if result not in final:
                    final.append(result)

print(final)

sum = []

for i in range(len(final)):
    cnt = 0
    for j in range(len(final[i])):
        cnt = cnt + final[i][j]

    sum.append(cnt)

print(sum)