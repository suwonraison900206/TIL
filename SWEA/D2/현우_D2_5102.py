import sys
sys.stdin = open("5102.txt")

def find_next(g, v, s, goal):
    global queue
    global visited
    global flag
    # g: graph, v: vertex, s: 현재 위치 , goal: G
    for i in range(1, v+1):
        if g[s][i] == 1 and visited[i][0] == 0:
            queue.append(i)
            visited[i][1] = visited[s][1] + 1
            if i == goal:
                flag = 1
                print(visited)
                return visited[i][1]
    else:
        return 0
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인덱스를 1부터 건드리려고 V+1씩 추가함
    graph = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        r, c = map(int, input().split())
        graph[r][c], graph[c][r] = 1, 1
    S, G = map(int, input().split())
    # v[i][0]은 방문여부, v[i][1]은 시작점부터의 길이
    visited = [[0, 0] for _ in range(V+1)]
    queue = [S]
    flag, cnt = 0, 0
    while len(queue) > 0:
        w = queue.pop(0)
        visited[w][0] = 1
        cnt = find_next(graph, V, w, G)
        if flag == 1:
            break
    print("#{0} {1}".format(tc, cnt))