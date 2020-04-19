import sys
sys.stdin = open("castle.txt")

def backtrack(a, k, N):
    if k == N:
        if sum(a) == 6:
            archer.append(a[:])
    else:
        a[k] = 0
        backtrack(a, k+1, N)
        a[k] = 2
        backtrack(a, k+1, N)

N, M, D = list(map(int, input().split()))
list_k = []
for i in range(N):
    list_k.append(list(map(int, input().split())))

print(list_k)

archer = []
q = [0] * M

backtrack(q,0,5)

print(archer)
for i in range(len(archer)):
    result = list_k[:] + [archer[i]]
    for time in range(5):




