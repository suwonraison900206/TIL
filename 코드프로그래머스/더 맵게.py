import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while True:
        count = count + 1
        a, b = heapq.heappop(scoville) , heapq.heappop(scoville)

        heapq.heappush(scoville, a + (b*2))
        c = heapq.heappop(scoville)


        if c >= K:

            answer = count

            return answer
        elif len(scoville) == 1 and c < K:
            answer = -1
            return answer
        heapq.heappush(scoville, c)




scoville = [1, 2, 3, 9, 10, 12]
K = 7

solution(scoville,K)
#
# def solution(scoville, K):
#     scoville.sort()
#     t = 0
#     while min(scoville) < K:
#         if len(scoville) > 1:
#             scoville[0] += scoville[1] * 2
#             scoville.pop(1)
#             scoville.sort()
#             t += 1
#         else:
#             t = -1
#             break
#     return t