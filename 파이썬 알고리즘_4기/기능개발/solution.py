from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    lst = []

    while progresses:
        work = progresses.popleft()
        speed = speeds.popleft()
        cnt = 0

        while work < 100:
            work += speed
            cnt += 1

        if len(lst) == 0:
            lst.append(cnt)
        else:

            if cnt > max(lst):
                answer.append(len(lst))
                lst = [cnt]
            else:
                lst.append(cnt)

    return answer + [len(lst)]


progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)