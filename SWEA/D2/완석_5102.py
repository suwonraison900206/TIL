import sys
sys.stdin = open("5102.txt")

T = int(input())
for t in range(1, T + 1):
    V, E = list(map(int, input().split()))
    visited = [0] * (V + 1)
    A = [[0] for _ in range(V + 1)]  # 연결된 리스트

    for e in range(E):
        a, b = list(map(int, input().split()))
        A[a].append(b)
        A[b].append(a)

    start, end = list(map(int, input().split()))


    stack = [start]
    visited[start] = 0


    p = 0
    while stack:
        go = stack.pop()
        while len(A[go]) > 1 and A[go][-1] != 0:
            k = A[go].pop()
            if k == end:
                visited[go] +=1
                print(visited)
                print(f'#{t} {visited[go]}')
                p = 1
                break
            else:
                stack.append(k)
                visited[k] = visited[go] + 1
                print(visited)
        if p == 1:
            break
    if p == 0:
        print(f'#{t} {0}')