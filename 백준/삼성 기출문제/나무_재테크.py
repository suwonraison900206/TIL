import sys
sys.stdin = open('tree.txt')
N , M , K = map(int,input().split())
A = [list(map(int,input().split())) for __ in range(N)]
map_lst = [[5] * N for __ in range(N)]
tree = []
alive_tree = []
dead_tree = []
for i in range(M):
    x, y, z = map(int,input().split())
    tree.append([x-1,y-1,z])
year = 0
dx =[-1, -1, -1, 0, 1, 1, 1, 0]
dy =[-1, 0, 1, 1, 1, 0, -1, -1]
while year != K:
    tree.sort(key=lambda x: x[2])
    for season in range(1,5):
        if season == 1: # 봄
            for i in range(len(tree)):
                if map_lst[tree[i][0]][tree[i][1]] - tree[i][2] >= 0:
                    map_lst[tree[i][0]][tree[i][1]] = map_lst[tree[i][0]][tree[i][1]] - tree[i][2]
                    tree[i][2] = tree[i][2] + 1
                    alive_tree.append([ tree[i][0], tree[i][1], tree[i][2]])
                else:
                    dead_tree.append(tree[i])
            tree = alive_tree[:]
            alive_tree= []
        elif season == 2: # 여름
            for i in range(len(dead_tree)):
                map_lst[dead_tree[i][0]][dead_tree[i][1]] = map_lst[dead_tree[i][0]][dead_tree[i][1]] + (dead_tree[i][2]) // 2
            dead_tree = []
        elif season == 3: # 가을
            for i in range(len(tree)):
                if tree[i][2] % 5 == 0:
                    for q in range(8):
                        di = tree[i][0] + dx[q]
                        dj = tree[i][1] + dy[q]
                        if 0 <= di < N and 0 <= dj < N:
                            tree.append([di, dj, 1])
        elif season == 4: # 겨울
            for i in range(N):
                for j in range(N):
                    map_lst[i][j] = map_lst[i][j] + A[i][j]
    year = year + 1
print(len(tree))


