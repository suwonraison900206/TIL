from collections import deque
import heapq
def solution(N, road, K):
    answer = 0
    N_lst = [float('inf') for i in range(N + 1)]
    N_lst[1] = 0
    road_lst = [[] for __ in range(N + 1)]

    w = [float('inf')] * 10
    print(w)
    heap = []
    heapq.heappush(heap, 1)
    print(heap)
    for u, v, d in road:
        road_lst[u].append([v, d])
        road_lst[v].append([u, d])

    # queue = deque([1])
    # print(road_lst)

    while heap:

        q = heapq.heappop()
        print(q)


    # while queue:
    #     q = queue.popleft()
    #     for destination, count in road_lst[q]:
    #         if N_lst[destination] > N_lst[q] + count:
    #             N_lst[destination] = N_lst[q] + count
    #             queue.append(destination)

    for i in range(1, N + 1):
        if N_lst[i] <= K:
            answer += 1

    print(N_lst)

    return answer


N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
k = 4

solution(N, road, k)