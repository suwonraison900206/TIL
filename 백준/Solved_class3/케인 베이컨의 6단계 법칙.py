from collections import deque

N, M = map(int,input().split())
friends = [list(map(int,input().split())) for __ in range(M)]
lst = [[float('inf')] * (N) for __ in range(N)]
nodes = {}
result = []

for x,y in friends:

    if x not in nodes:
        nodes[x] = [y]
    else:
        nodes[x].append(y)

    if y not in nodes:
        nodes[y] = [x]
    else:
        nodes[y].append(x)

for i in range(N):

    lst[i][i] = 0
    queue = deque()
    queue.append(i)

    while queue:

        w = queue.popleft()
        for j in nodes[w+1]:

            if lst[i][j-1] > lst[i][w] + 1:
                lst[i][j-1] = lst[i][w] + 1
                queue.append(j-1)

    result.append([i, sum(lst[i])])

result.sort(key=lambda x:(x[1], x[0]))
print(result[0][0]+1)