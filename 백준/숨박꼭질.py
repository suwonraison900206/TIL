def hide():

    global queue
    cnt = 0

    queue1 = []
    while queue:

        x = queue.pop(0)
        if x == K:
            return visited[K]
        elif 0 <= x <= 100002:
            if N > K and visited[x-1] == 0:
                queue1.append(x - 1)
                visited[x - 1] = cnt + 1
            else:
                if visited[x+1] == 0:
                    queue1.append(x+1)
                    visited[x+1] = cnt + 1
                if visited[x-1] == 0:
                    queue1.append(x-1)
                    visited[x-1] = cnt + 1
                if (2 * x) < 100002 and visited[2 * x] == 0:
                    queue1.append(2 * x)
                    visited[2 * x] = cnt + 1
        if len(queue) == 0:

            queue = queue1[:]
            cnt = cnt + 1
            queue1 = []





N , K = map(int,input().split())
visited = [0] * 200002
queue = []
queue.append(N)
result = hide()
print(result)





