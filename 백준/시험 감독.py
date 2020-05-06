import sys
sys.stdin = open("coach.txt")

N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

count = 0

for i in range(N):
    A[i] = A[i] - B
    if A[i] < 0:
        A[i] = 0
    count += 1

for i in range(N):
    k_1 = A[i] // C
    k_2 = A[i] % C
    count = count + k_1
    if k_2 != 0 and k_2 > 0 :
        count = count + 1

print(count)