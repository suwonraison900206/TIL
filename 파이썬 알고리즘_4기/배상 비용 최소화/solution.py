import heapq


def solution(no, works):
    heap =[]
    answer = 0

    for work in works:
        heapq.heappush(heap,(-work, work))

    while no > 0:
        q = heapq.heappop(heap)[1]
        if q == 0:
            break

        heapq.heappush(heap, (-(q-1), q-1))
        no -= 1

    for number1, number2 in heap:
        answer += number2 ** 2

    return answer


N =4
works = [4,3,3]
solution(N, works)