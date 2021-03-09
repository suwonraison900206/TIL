import heapq


def solution(jobs):
    answer = 0
    jobs.sort(reverse=True)
    L = len(jobs)
    start = 0
    cnt = 0
    heap = []

    while jobs :

        while jobs and jobs[-1][0] <= start:
            heapq.heappush(heap , [jobs[-1][1] +(start - jobs[-1][0]), jobs[-1]])
            jobs.pop()
        print(heap)

        while heap:
            print(heap ,'before')
            q = heapq.heappop(heap)
            print(q)
            start += q[1][1]
            cnt = cnt + q[0]

            for i in heap:
                i[0] = i[0] + q[1][1]

        start += 1
    return int(cnt // L)



jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)
