import sys
sys.stdin = open("retire.txt")

N = int(input())
lst = []

for i in range(N):
    lst.append(list(map(int,input().split())))

for i in range(N):
    if i + lst[i][0] > N:
        lst[i][0] = 0
        lst[i][1] = 0

day = 0
result = []

for i in range(N):
    count = 0
    day_pass = 0
    day = 0
    for j in range(i,N):
        if day_pass != 0:
            day_pass = day_pass -1
        elif lst[j][0] + day < N+1:
            day = day + (lst[j][0])
            count = count + lst[j][1]
            day_pass += (lst[j][0]) -





    result.append(count)

print(max(result))
