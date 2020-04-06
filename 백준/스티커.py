import sys
sys.stdin = open("put.txt")

N , M , K  = map(int,input().split())



lst = [[0] * M for _ in range(N)]

for i in range(1):
    stick = []
    R , C = map(int,input().split())
    for j in range(R):
        stick.append(list(map(int,input().split())))
        print(stick)
    for j in range(N - R):
        for k in range(M - C):
            for q in range(R):
                for w in range(C):
                    lst[j][k] = stick[q][w]

