import heapq


def solution(scoville, K):

    answer = 0
    heap = []

    for number in scoville:
        heapq.heappush(heap, number)

    while True:
        if heap[0] >= K: # 모든 음식의 스코빌 지수가 K 이상이 된다면
            break
        if len(heap) == 1 and heap[0] < K: # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1

        q = heapq.heappop(heap)
        k = heapq.heappop(heap)
        cnt = q + (2 * k)
        heapq.heappush(heap, cnt)
        answer += 1  # 섞은 횟수 ++

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville,K)