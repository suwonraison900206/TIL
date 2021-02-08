from collections import deque

def solution(N, road, K):
    answer = 0
    N_lst = [float('inf') for i in range(N + 1)]
    N_lst[1] = 0
    road_lst = [[] for __ in range(N + 1)]

    for u, v, d in road:
        road_lst[u].append([v, d])
        road_lst[v].append([u, d])

    queue = deque([1])
    while queue:
        q = queue.popleft()

        for destination, count in road_lst[q]:
            if N_lst[destination] > N_lst[q] + count:
                N_lst[destination] = N_lst[q] + count
                queue.append(destination)

    for i in range(1, N + 1):
        if N_lst[i] <= K:
            answer += 1

    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
k = 3

solution(N, road, k)