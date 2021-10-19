import heapq

N = int(input())
N_lst = [int(input()) for __ in range(N)]
heap = []

for i in N_lst:
    if i != 0:
        heapq.heappush(heap, i)
    elif i == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
