import sys
sys.stdin = open('톱니바퀴.txt')

# 1은 시계방향 -1은 반시계방향
wheel = [list(map(int,input())) for _ in range(4)]
k = int(input())
rotates = []
for i in range(k):
    rotates.append(list(map(int,input().split())))


for rotate in rotates:
    idx, dir = rotate[0], rotate[1]
    print(idx, dir)
    for i in range(len(wheel)-1):

        if wheel[i][idx-1] != wheel[i+1][idx-1]:
           if dir == 1:
                for j in range(len(wheel[i])):
                    if j+1 == 8:
                        wheel[i][0] = wheel[i][7]
                    else:
                        wheel[i][j+1] = wheel[i][j]
                print(wheel[i])

