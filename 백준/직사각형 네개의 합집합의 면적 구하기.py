temp = list(map(int,input().split()))
k = [[0]*10 for _ in range(10)]
print(k)
print(k[1][2])

cnt = 0
for j in range(1,4):
    for q in range(2,4):
        k[j][q] = 1

print(k)
for u in range(2,5):
    for q in range(3,7):
        k[u][q] = 1
print(k)
for x in range(3,6):
    for q in range(1,5):
        k[x][q] = 1
print(k)
for y in range(7,8):
    for q in range(3,6):
        k[y][q] = 1
print(k)
for o in range(10):
    for p in range(10):
        if k[o][p] == 1:
            cnt = cnt +1
print(cnt)