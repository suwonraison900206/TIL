V = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
Q = [1, 2, 3, 4, 5, 6, 7]

stack = []

node_list = [[0] * (len(Q)+1) for _ in range((len(Q)+1))]

visit = [0] * (len(Q) + 1)

for i in range((len(V) // 2)):
    node_list[V[2*i]][V[(2*i)+1]] = 1
    node_list[V[(2 * i) + 1]][V[(2 * i)]] = 1

stack.append(1)

while len(stack) > 0:
    v = stack.pop()
    if visit[v] == 0:
        visit[v] = 1
        print(v)
        for j in range(len(node_list)):
            if node_list[v][j] == 1 and visit[j] == 0:
                stack.append(j)



