import heapq

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key= lambda x: x[0])
heap = []
heapq.heappush(heap, lst[0][1])

for i in range(1, n):
    print(heap)
    if heap[0] > lst[i][0]:
        heapq.heappush(heap, lst[i][1])
    else:
        heapq.heappop(heap) #최소값
        heapq.heappush(heap, lst[i][1])

print(len(heap))