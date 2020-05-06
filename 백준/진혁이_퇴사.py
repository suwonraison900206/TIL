import sys
sys.stdin = open("retire.txt")



def backtrack(k, N, s=0):
    if k > N: return
    global maxV
    global cnt
    cnt.append(maxV)
    maxV = s if s > maxV else maxV
    for i in range(k, N):
        backtrack(i + T[k], N, s + P[k])


N = int(input())
T, P = [0] * N, [0] * N
cnt = []

for i in range(N):
    T[i], P[i] = map(int, input().split())
maxV = -1
for i in range(N):
    backtrack(i, N)

print(cnt)
print(maxV)