import copy
import sys
sys.stdin = open('마법사상어와파이어볼.txt')

N, M, K = map(int,input().split())
fireball = [list(map(int,input().split())) for _ in range(M)]
print(fireball)

 # i 번 파이어볼의 위치는 (r,c) 질량은 m 방향은 d 속력은 s
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
lst2 = [[0] * N for _ in range(N)]
cnt = 0
while cnt != K:

    for r, c, m ,s ,d in fireball:
            if s > N:
                s = s % N
            elif s == N:
                s = 0

            dx = r-1 + (dir[d][0] * s)
            dy = c-1 + (dir[d][1] * s)
            if dx > N:
                dx = dx % N

            if dy > N:
                dy = dy % N

            if lst2[dx][dy] == 0:

                lst2[dx][dy] = [m, d, 1]
            else:
                lst2[dx][dy][0] += m
                lst2[dx][dy][1] += d
                lst2[dx][dy][2] +=1
    print(lst2)
    new_fireball = []
    for i in range(N):
        for j in range(N):
            if type(lst2[i][j]) != int:

                if lst2[i][j][0] // 5 != 0:
                    new_m = lst2[i][j][0] // 5
                    new_s = lst2[i][j][1] // lst2[i][j][2]
                    if lst2[i][j][1] % 2 == 0: # 짝수:
                        for w in (0, 2, 4, 6):
                            new_fireball.append([i+1, j+1, new_m, new_s, w])
                    elif lst2[i][j][1] % 2 == 1: # 홀수

                        for w in (1, 3, 5, 7):
                            new_fireball.append([i + 1, j + 1, new_m, new_s, w])
                lst2[i][j] = 0

    fireball = new_fireball[:]
    cnt +=1
    # print(lst2)
    # print(fireball)