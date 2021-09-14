import heapq


def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x:(x[1], x[1] - x[0]))
    heap = []
    print(jobs)

    start = 0
    end = 0
    cnt = 0
    w = len(jobs)
    while jobs:
        q = jobs.pop(0)
        print(q)
        print(start, end,cnt, '123213')
        if start == 0:
            end = q[0] + start + q[1]
            cnt = q[0] + start + q[1]
            start = end
        else:
            cnt = cnt + (end - q[0]) + q[1]
            end += q[1]
    print(cnt)
    print(cnt//w)

    return cnt // w


jobs =[[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]

solution(jobs)