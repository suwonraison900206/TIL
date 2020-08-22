import sys
sys.stdin = open("05. 볼링공 고르기.txt")

N, M = input().split()
ball = list(map(int,input().split()))
cnt = 0

for i in range(len(ball)-1):
    for j in range(i+1, len(ball)):
        if ball[i] != ball[j]:
            cnt = cnt + 1

print(cnt)
